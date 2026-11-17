import asyncio
import json
import os
import re
import time
import requests

try:
    from ddgs import DDGS
except ImportError:
    from duckduckgo_search import DDGS

from google import genai
from notebooklm import NotebookLMClient
from tavily import TavilyClient
from dotenv import load_dotenv

# .env dosyasından anahtarları yükle
load_dotenv()

# ==================== 1. API ANAHTARLARI ====================
NOTEBOOK_ID    = "f2e75aa1-ef9d-4e1c-a281-95885383785a"
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ==================== 2. DOSYA VE HIZ AYARLARI ====================
STATE_FILE      = "sah_hibrit_checkpoint.json"
RAPOR_VITRIN    = "sah_ben_demistim_vitrin.md"
RAPOR_TUM_ARSIV = "sah_tum_kararlar.md"

SLEEP_NOTEBOOKLM = 5    # NotebookLM oturum koruması (sn)
SLEEP_DDG_MIN    = 1.5  # Aynı videonun ardışık iddiaları arası mikro bekleme (sn)
# ==================================================================

gemini_client = genai.Client(
    api_key=GEMINI_API_KEY,
    http_options={"api_version": "v1beta"}
)
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

EXTRACT_PROMPT = """
Sadece seçili olan bu tek videonun transkriptini baştan sona dikkatlice incele.
Bu bir "Siber Alemden Havadisler" yayınıdır. Konuşmacının (Utku Şen) GELECEĞE YÖNELİK yaptığı:
- Şahsi siber güvenlik ve teknoloji tahminlerini ("yakında şu patlar", "göreceksiniz ileride şöyle olacak", "bu teknoloji tutmaz", "şu sektöre saldırılar artacak")
- Şahsi tezlerini ve iddialı gelecek öngörülerini eksiksiz çıkar.

KURALLAR (KESİNLİKLE UYULACAK):
1. HABERİN KENDİSİNİ VEYA ŞİRKET PLANINI ASLA ALMA:
   - Şirketlerin, devletlerin veya hackerların yaptıkları veya yapacaklarını duyurdukları şeyler "tahmin" DEĞİLDİR; sadece haberdir.
   - ÖRNEK (ALMA): "Akamai Linode'u satın aldı ve servis sunacak" -> Bu şirketin haberidir, ALMA.
   - ÖRNEK (ALMA): "X firması yeni bir güvenlik yaması çıkaracakmış" -> Bu haberdir, ALMA.
2. SADECE KONUŞMACININ (UTKU'NUN) KENDİ ŞAHSİ ÇIKARIMLARINI AL:
   - "Bence bu olay ileride şuna yol açacak...",
   - "Göreceksiniz yakında şu sektör patlayacak / şu sistemler çökecek...",
   - "Devletler bu tip sistemleri kesinlikle yasaklayacak / regüle edecek...",
   - "Bu teknoloji asla tutmaz, ileride çok başları ağrıyacak..."
3. ZORLAMA İDDİA ÇIKARMA:
   - Eğer konuşmacı videoda sadece haberleri düz anlatmış ve geleceğe dair hiçbir şahsi öngörüde bulunmamışsa KESİNLİKLE boş liste `[]` döndür.
4. DİL VE ÜSLUP (ÇOK ÖNEMLİ):
   - KESİNLİKLE noktalı virgül (;) kullanma.
   - "öngörülmektedir", "ifade etmiştir", "dile getirmiştir" gibi robotik yapay zeka kalıplarını KESİNLİKLE kullanma.
   - Sanki bir arkadaşına anlatır gibi akıcı, net ve günlük doğal Türkçe kullan (Örn: "Utku, önümüzdeki 5 yıl içinde çoğu AB ülkesinin 4 gün çalışmaya geçeceğini söylüyor").

Çıktıyı SADECE aşağıdaki JSON dizisi formatında ver, başka tek kelime yazma:
```json
[
  {
    "iddia_ozeti": "Geleceğe yönelik şahsi öngörünün tek cümlelik net özeti",
    "orijinal_baglam": "Videoda tam olarak ne söylendiği ve hangi olay/teknoloji üzerine dendiği",
    "arama_sorgusu_en": "BleepingComputer, The Hacker News vb. kaynaklarda doğrulamak için 5-7 kelimelik en net İngilizce arama sorgusu",
    "arama_sorgusu_tr": "Türkiye özelinde veya Türkçe haberlerde aratmak için 4-6 kelimelik Türkçe arama sorgusu"
  }
]
```
"""

DECISION_QUESTIONS = {
    "tahmin_sonucu": {
        "type": "choice",
        "instructions": (
            "Videodaki geleceğe yönelik siber güvenlik tahmininin, Tavily ve DuckDuckGo üzerinden "
            "toplanan güncel web makaleleri ve arama sonuçlarına göre gerçekleşip gerçekleşmediğini sınıflandır.\n"
            "ÖNEMLİ KURAL: Eğer konuşmacı bir olayın OLMAYACAĞINI, TUTMAYACAĞINI veya ENGELLENECEĞİNİ öngörmüşse "
            "ve aradan geçen zamanda o şey gerçekleşmemiş/tutmamışsa bu iddia 'TUTTU' sayılır."
        ),
        "criteria": {
            "TUTTU": "Öngörü, yayından sonraki süreçte somut olarak gerçekleşti (veya olumsuz öngörü haklı çıktı) ve web bulgularında net kanıtı var.",
            "KISMEN_TUTTU": "Öngörünün ana yönü doğru çıktı ancak kapsam, hedef veya zamanlamada kısmi sapma var.",
            "TUTMADI": "Öngörünün tam tersi gerçekleşti veya aradan geçen makul zamana rağmen beklenti boşa çıktı.",
            "BELIRSIZ": "Bulunan içerikler bu iddiayı doğrulamak veya çürütmek için yetersiz ya da öngörünün vadesi henüz dolmadı."
        }
    }
}


def test_apis():
    """Başlamadan önce Tavily ve Gemini Decision 1 anahtarlarını canlı test eder."""
    print("API bağlantıları kontrol ediliyor...")
    try:
        tavily_client.search(query="cybersecurity", search_depth="basic", max_results=1)
        print("  [OK] Tavily AI bağlantısı başarılı (1 kredi kullanıldı).")
    except Exception as e:
        print(f"  [HATA] Tavily bağlantı sorunu: {e}")
        return False

    try:
        res = gemini_client.decisions.create(
            model="gemini-decision-1",
            input="Test: Güneş doğudan doğar.",
            questions={
                "test": {
                    "type": "choice",
                    "instructions": "Doğru mu?",
                    "criteria": {"EVET": "Doğru", "HAYIR": "Yanlış"}
                }
            }
        )
        ans = res.answers["test"]
        val = getattr(ans, "choice", None) or getattr(ans, "value", None)
        print(f"  [OK] Google gemini-decision-1 bağlantısı başarılı (Test yanıtı: {val}).\n")
    except Exception as e:
        print(f"  [HATA] gemini-decision-1 bağlantı sorunu: {e}")
        return False

    return True


def load_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[!] Checkpoint dosyası okunurken hata: {e}")
            bak = STATE_FILE + ".bak"
            if os.path.exists(bak):
                with open(bak, "r", encoding="utf-8") as f:
                    return json.load(f)
    return {"videos": {}}


def save_state(state):
    tmp = STATE_FILE + ".tmp"
    bak = STATE_FILE + ".bak"
    try:
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
        if os.path.exists(STATE_FILE):
            try:
                with open(STATE_FILE, "r", encoding="utf-8") as sf, open(bak, "w", encoding="utf-8") as bf:
                    bf.write(sf.read())
            except Exception:
                pass
        os.replace(tmp, STATE_FILE)
    except Exception as e:
        print(f"[!] State kaydedilirken hata: {e}")


def parse_json_safely(text):
    if not text:
        return None
    text = text.strip()
    match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text)
    if match:
        text = match.group(1).strip()

    for start_ch, end_ch in [('[', ']'), ('{', '}')]:
        s_idx = text.find(start_ch)
        e_idx = text.rfind(end_ch)
        if s_idx != -1 and e_idx != -1 and e_idx > s_idx:
            try:
                return json.loads(text[s_idx:e_idx + 1])
            except json.JSONDecodeError:
                pass
    return None


def fetch_youtube_date(url):
    """YouTube video URL'sinden yayın tarihini (YYYY-AA-GG) çeker."""
    if not url or "youtube.com" not in url:
        return None
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        r = requests.get(url, headers=headers, timeout=6)
        m = re.search(r'itemprop="datePublished" content="([^"]+)"', r.text)
        if m:
            return m.group(1).split("T")[0]
        m2 = re.search(r'"publishDate":"([^"]+)"', r.text)
        if m2:
            return m2.group(1).split("T")[0]
    except Exception:
        pass
    return None


def hybrid_web_search(query_en, query_tr):
    """Aşama 2: Tavily (derin teknik içerik) + DuckDuckGo (geniş/yerel tarama) hibrit araması."""
    combined = []
    seen_urls = set()
    ignore_domains = ("sahibinden.com", "trendyol.com", "hepsiburada.com", "n11.com", "amazon.com.tr")

    # 1. TAVILY ARAMASI (Sadece EN sorguyla 1 kredi harcayarak sayfa içi paragraf çeker)
    primary_q = query_en.strip() if query_en else query_tr.strip()
    if primary_q:
        for attempt in range(3):
            try:
                resp = tavily_client.search(
                    query=primary_q,
                    search_depth="basic",
                    max_results=4,
                    include_raw_content=False
                )
                for r in resp.get("results", []):
                    url = r.get("url", "")
                    if url and url not in seen_urls:
                        if any(ign in url.lower() for ign in ignore_domains):
                            continue
                        seen_urls.add(url)
                        combined.append({
                            "motor": "Tavily",
                            "sorgu": primary_q,
                            "baslik": r.get("title", ""),
                            "icerik": r.get("content", ""),
                            "link": url
                        })
                break
            except Exception as e:
                print(f"    [!] Tavily uyarısı ({e}), 5 sn bekleniyor...")
                time.sleep(5)

    # 2. DUCKDUCKGO ARAMASI (Hız sınırına akıllı geri çekilme; tekil linkler eklenir)
    ddg_queries = [q.strip() for q in [query_en, query_tr] if q and len(q.strip()) > 2]
    for q in ddg_queries:
        for attempt in range(2):
            try:
                with DDGS() as ddgs:
                    for r in ddgs.text(q, max_results=3):
                        url = r.get("href", "")
                        if url and url not in seen_urls:
                            if any(ign in url.lower() for ign in ignore_domains):
                                continue
                            seen_urls.add(url)
                            combined.append({
                                "motor": "DuckDuckGo",
                                "sorgu": q,
                                "baslik": r.get("title", ""),
                                "icerik": r.get("body", ""),
                                "link": url
                            })
                time.sleep(SLEEP_DDG_MIN)
                break
            except Exception as e:
                wait = 6 * (attempt + 1)
                time.sleep(wait)

    return combined


def run_decision_model(video_title, claim, web_results, video_date=None, max_retries=3):
    """Aşama 3: Tavily + DuckDuckGo havuzunu gemini-decision-1 ile değerlendirir."""
    if not web_results:
        return {"sinif": "BELIRSIZ", "guven_skoru": 0.0, "olasiliklar": {}}

    formatted_web = "\n\n".join([
        f"- [{item['motor']}] {item['baslik']} ({item['link']})\n  İçerik: {item['icerik']}"
        for item in web_results
    ])

    shared_input = json.dumps({
        "video_basligi": video_title,
        "video_yayin_tarihi": video_date or "Bilinmiyor",
        "videodaki_tahmin": claim.get("iddia_ozeti"),
        "videodaki_baglam": claim.get("orijinal_baglam"),
        "web_bulgulari": formatted_web
    }, ensure_ascii=False)

    for attempt in range(max_retries):
        try:
            res = gemini_client.decisions.create(
                model="gemini-decision-1",
                input=shared_input,
                questions=DECISION_QUESTIONS
            )
            ans = res.answers["tahmin_sonucu"]
            top_choice = getattr(ans, "choice", None) or getattr(ans, "value", None) or "BELIRSIZ"
            confidence = getattr(ans, "confidence", 0.0)
            probs = dict(ans.probabilities) if hasattr(ans, "probabilities") and ans.probabilities else {}

            return {
                "sinif": str(top_choice).replace("_", " "),
                "guven_skoru": round(float(confidence) * 10, 1),
                "olasiliklar": {k.replace("_", " "): round(float(v), 3) for k, v in probs.items()}
            }
        except Exception as e:
            wait = 8 * (attempt + 1)
            print(f"    [!] Gemini Decision 1 hatası ({e}), {wait} sn bekleniyor...")
            time.sleep(wait)

    return None


async def ask_notebooklm(client, prompt, source_id, retries=3):
    """Aşama 1: NotebookLM'den tek bir videonun öngörülerini çeker."""
    for attempt in range(retries):
        try:
            resp = await client.chat.ask(
                notebook_id=NOTEBOOK_ID,
                question=prompt,
                source_ids=[source_id]
            )
            await asyncio.sleep(SLEEP_NOTEBOOKLM)
            return resp.answer
        except Exception as e:
            wait = 15 * (attempt + 1)
            print(f"    [!] NotebookLM hatası ({e}), {wait} sn bekleniyor...")
            await asyncio.sleep(wait)
    return None


def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]


def clean_natural_text(text):
    """Metinleri yapay zeka jargonu ve noktalı virgüllerden arındırıp doğal Türkçeye çevirir."""
    if not text:
        return ""
    t = text.replace(";", ",")
    t = re.sub(r",\s*,+", ",", t)
    t = re.sub(r",\s*\.", ".", t)
    replacements = [
        (r"\böngörülmektedir\b", "tahmin ediliyor"),
        (r"\böngörülmüştür\b", "tahmin ediliyor"),
        (r"\bdile getirilmiştir\b", "söyleniyor"),
        (r"\bdile getirmiştir\b", "söylüyor"),
        (r"\bifade etmiştir\b", "belirtiyor"),
        (r"\bifade edilmektedir\b", "belirtiliyor"),
        (r"\baktarmıştır\b", "anlatıyor"),
        (r"\baktarılmıştır\b", "anlatılıyor"),
        (r"\bvurgulanmıştır\b", "vurgulanıyor"),
        (r"\bvurgulamıştır\b", "vurguluyor"),
        (r"\bbildirilmiştir\b", "söyleniyor"),
        (r"\bbildirmiştir\b", "söylüyor"),
        (r"\biddia edilmektedir\b", "iddia ediliyor"),
    ]
    for pat, rep in replacements:
        t = re.sub(pat, rep, t, flags=re.IGNORECASE)
    return t.strip()


def write_reports(state):
    """Sonuçları Tüm Tahminler Arşivi olarak Markdown dosyalarına yazar."""
    arsiv = ["# Tahminler Arşivi\n\n179 bölümlük seride yapılan tüm şahsi tahminler, web bulguları ve değerlendirme sonuçları.\n\n"]

    sayac = {"TUTTU": 0, "KISMEN TUTTU": 0, "TUTMADI": 0, "BELIRSIZ": 0}

    sorted_videos = sorted(
        state["videos"].items(),
        key=lambda item: natural_sort_key(item[1].get("title", ""))
    )

    for vid_id, vdata in sorted_videos:
        title = clean_natural_text(vdata.get("title", "Bilinmeyen Video"))
        vdate = vdata.get("publish_date")
        date_str = f" - {vdate}" if vdate else ""
        claims = vdata.get("claims", [])
        if not claims:
            continue

        arsiv.append(f"## {title}{date_str}\n\n")

        for idx, c in enumerate(claims, 1):
            karar = c.get("karar")
            if not karar:
                continue

            sinif = str(karar.get("sinif", "BELIRSIZ")).upper().strip()
            if sinif not in sayac:
                sinif = "BELIRSIZ"
            sayac[sinif] += 1

            skor = karar.get("guven_skoru", 0)
            probs = karar.get("olasiliklar", {})
            prob_str = " | ".join([f"{k}: %{round(v*100, 1)}" for k, v in probs.items()]) if probs else "-"

            web_items = c.get("web_bulgulari", [])
            evidence_lines = []
            for w in web_items[:5]:
                link = w.get("link")
                if not link:
                    continue
                motor = w.get("motor", "Web")
                baslik = clean_natural_text(w.get("baslik", "Bağlantı"))
                baslik = re.sub(r"[\r\n]+", " ", baslik).strip()
                baslik = baslik.replace("[", "(").replace("]", ")").replace("#", "").strip()
                if len(baslik) > 130:
                    baslik = baslik[:130].strip() + "..."

                icerik = clean_natural_text(w.get("icerik", "").strip())
                icerik = icerik.replace("#", "")
                icerik_temiz = re.sub(r"\s+", " ", icerik).strip()
                icerik_temiz = icerik_temiz.replace("[", "(").replace("]", ")").replace('"', "'")
                if len(icerik_temiz) > 350:
                    icerik_temiz = icerik_temiz[:350].strip() + "..."

                item_str = f"  - `[{motor}]` [{baslik}]({link})"
                if icerik_temiz:
                    item_str += f"\n    > *\"{icerik_temiz}\"*"
                evidence_lines.append(item_str)

            link_md = "\n".join(evidence_lines) if evidence_lines else "  - Kanıt linki bulunamadı"

            badge = {
                "TUTTU": '<span class="badge-tuttu">TUTTU</span>',
                "KISMEN TUTTU": '<span class="badge-kismen">KISMEN TUTTU</span>',
                "TUTMADI": '<span class="badge-tutmadi">TUTMADI</span>',
                "BELIRSIZ": '<span class="badge-belirsiz">BELİRSİZ</span>'
            }.get(sinif, sinif)

            ozet = clean_natural_text(c.get("iddia_ozeti", ""))
            baglam = clean_natural_text(c.get("orijinal_baglam", ""))

            blok = (
                f"### {idx}. {ozet}\n"
                f"- **Sonuç:** {badge} (Güven Skoru: **{skor}/10**)\n"
                f"- **Olasılık Dağılımı:** `{prob_str}`\n"
                f"- **Videoda Ne Demişti:** {baglam}\n"
                f"- **İncelenen Web Kanıtları:**\n{link_md}\n\n"
            )
            arsiv.append(blok)

        arsiv.append("---\n\n")

    ozet_ust = (
        f"> **Genel Durum:** "
        f"Tuttu: **{sayac['TUTTU']}** | "
        f"Kısmen Tuttu: **{sayac['KISMEN TUTTU']}** | "
        f"Tutmadı: **{sayac['TUTMADI']}** | "
        f"Belirsiz: **{sayac['BELIRSIZ']}**\n\n---\n\n"
    )

    os.makedirs("docs", exist_ok=True)
    arsiv_content = arsiv[0] + ozet_ust + "".join(arsiv[1:])

    for p in ["docs/arsiv.md", RAPOR_TUM_ARSIV]:
        with open(p, "w", encoding="utf-8") as f:
            f.write(arsiv_content)


async def main():
    if not test_apis():
        print("Lütfen API anahtarlarını kontrol edip tekrar çalıştırın.")
        return

    state = load_state()

    print("NotebookLM defterine bağlanılıyor...")
    async with NotebookLMClient.from_storage() as nlm_client:
        sources = await nlm_client.sources.list(NOTEBOOK_ID)
        total = len(sources)
        print(f"Toplam {total} video bulundu. Hibrit tarama başlıyor...\n")

        for idx, src in enumerate(sources, 1):
            vid_id = src.id
            vid_title = src.title
            vid_url = getattr(src, "url", None)

            if vid_id not in state["videos"]:
                state["videos"][vid_id] = {
                    "title": vid_title,
                    "url": vid_url,
                    "publish_date": None,
                    "extracted": False,
                    "claims": []
                }

            vrec = state["videos"][vid_id]

            # Tarih eksikse YouTube'dan çekip kaydet
            if not vrec.get("publish_date") and vid_url:
                vdate = await asyncio.to_thread(fetch_youtube_date, vid_url)
                if vdate:
                    vrec["publish_date"] = vdate
                    save_state(state)

            vid_date = vrec.get("publish_date")
            date_info = f" ({vid_date})" if vid_date else ""

            # ---------------- AŞAMA 1: NOTEBOOKLM İDDİA TOPLAMA ----------------
            if not vrec.get("extracted", False):
                print(f"[{idx}/{total}] AŞAMA 1 (NotebookLM): {vid_title}{date_info}")
                raw = await ask_notebooklm(nlm_client, EXTRACT_PROMPT, vid_id)
                if raw is None:
                    print("  -> Yanıt alınamadı, sonraki çalıştırmada tekrar denenecek.")
                    continue

                claims = parse_json_safely(raw)
                vrec["claims"] = claims if isinstance(claims, list) else []
                vrec["extracted"] = True
                save_state(state)
                print(f"  -> {len(vrec['claims'])} adet öngörü çıkarıldı.")
            else:
                claim_count = len(vrec.get("claims", []))
                print(f"[{idx}/{total}] AŞAMA 1 tamamlanmış ({claim_count} iddia): {vid_title}{date_info}")

            # ---------------- AŞAMA 2 & 3: HİBRİT ARAMA + KARAR MODELİ ----------------
            for c_idx, claim in enumerate(vrec["claims"], 1):
                if "karar" in claim and claim["karar"]:
                    continue

                ozet = claim.get("iddia_ozeti", "")
                q_en = claim.get("arama_sorgusu_en", "")
                q_tr = claim.get("arama_sorgusu_tr", "")

                print(f"  -> İddia {c_idx}/{len(vrec['claims'])}: {ozet[:55]}...")
                print(f"     AŞAMA 2 (Tavily + DDG): EN='{q_en}' | TR='{q_tr}'")
                web_results = await asyncio.to_thread(hybrid_web_search, q_en, q_tr)

                print("     AŞAMA 3 (Gemini Decision 1): Değerlendiriliyor...")
                karar = await asyncio.to_thread(
                    run_decision_model, vid_title, claim, web_results, vid_date
                )

                if karar:
                    claim["web_bulgulari"] = web_results
                    claim["karar"] = karar
                    save_state(state)
                    write_reports(state)
                    print(f"     => SONUÇ: [{karar.get('sinif')}] - Güven: {karar.get('guven_skoru')}/10")

    write_reports(state)
    print("\nTüm videolar ve iddialar başarıyla işlendi!")
    print(f"- Vitrin Raporu: {RAPOR_VITRIN}")
    print(f"- Tüm Arşiv Raporu: {RAPOR_TUM_ARSIV}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[!] Durduruldu. Kaldığı yer 'sah_hibrit_checkpoint.json' dosyasına kaydedildi.")
