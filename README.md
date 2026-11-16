# Siber Alemden Havadisler (S.A.H) — Gelecek Öngörüleri Doğrulama Arşivi

Bu depo, **Utku Şen** tarafından hazırlanan haftalık siber güvenlik programı **"Siber Alemden Havadisler" (S.A.H)** yayınlarındaki şahsi teknoloji ve güvenlik öngörülerinin incelendiği açık kaynaklı bir yapay zeka araştırma ve doğrulama projesidir.

179 bölümden oluşan video serisinin transkriptleri yapay zeka ile taranmış; konuşmacının haberler üzerine yaptığı şahsi çıkarımlar ayıklanarak Tavily ve DuckDuckGo üzerinden toplanan kanıtlarla denetlenmiştir.

Raporlanan tüm sonuçlar **MkDocs Material** statik site oluşturucusu (SSG) ile GitHub Pages üzerinde sade, açık renkli ve okunabilir bir web sitesi olarak yayınlanmaktadır.

---

## 🏗️ Doğrulama Metodolojisi ve Mimarisi

Sistem, halüsinasyon riskini en aza indirmek ve şeffaflığı sağlamak amacıyla 4 aşamalı deterministik bir boru hattı üzerinden çalışır:

```mermaid
flowchart TD
    subgraph S1["1. Transkript ve Öngörü Taraması"]
        A1["179 Bölüm Transkripti"] --> A2["NotebookLM API"]
        A2 --> A3["Tekil Bağlam (source_ids=[vid_id])"]
        A3 --> A4["Haber / Şirket Duyurusu Filtresi"]
        A4 --> A5["Yapılandırılmış JSON Çıktısı"]
    end

    subgraph S2["2. Hibrit Çift Motorlu Arama"]
        A5 --> B1["Tavily Search API (Temel Derinlik)"]
        A5 --> B2["DuckDuckGo Arama Motoru"]
        B1 --> B3["Teknik Kaynaklardan Derin Paragraf Alıntısı"]
        B2 --> B4["Yerel TR / Alternatif Kaynaklar"]
        B3 --> B5["Tekilleştirilmiş Kanıt Havuzu"]
        B4 --> B5
    end

    subgraph S3["3. Olasılık Tabanlı Karar Modeli"]
        B5 --> C1["Google Gemini Decision 1"]
        A5 --> C1
        C1 --> C2["Ayrık Sınıflandırma (0 Çıktı Tokeni)"]
        C2 --> C3["Kategoriler: TUTTU / KISMEN TUTTU / TUTMADI / BELİRSİZ"]
        C3 --> C4["Matematiksel Güven Skoru (0 - 10)"]
    end

    subgraph S4["4. Kayıt ve Web Sitesi Yayını"]
        C4 --> D1["sah_hibrit_checkpoint.json"]
        D1 --> D2["docs/vitrin.md (Tutanlar)"]
        D1 --> D3["docs/arsiv.md (Tüm Bölümler)"]
        D2 --> D4["GitHub Pages (MkDocs Material)"]
        D3 --> D4
    end
```

### Aşamaların İşleyişi:

1. **Aşama 1 (NotebookLM):** Videolar birbirine karıştırılmadan tek tek (`source_ids=[vid_id]`) taranır. Şirketlerin resmi satın alımları veya ürün duyuruları elenir; yalnızca Utku Şen'in kendi tecrübesiyle dile getirdiği şahsi öngörüler ayıklanır.
2. **Aşama 2 (Tavily + DuckDuckGo Hibrit Arama):**
   - **Tavily:** İddia başına İngilizce sorguyla teknik haber sitelerine (BleepingComputer, The Hacker News vb.) girerek doğrudan ilgili paragrafları (`content`) çeker.
   - **DuckDuckGo:** Yerel Türkçe haberleri ve alternatif küresel kaynakları tarayarak aynı URL'leri eler ve kanıt havuzunu tamamlar.
3. **Aşama 3 (Gemini Decision 1):** Karar modeli, toplanan makale alıntılarını ve video bağlamını okuyarak kalibre edilmiş matematiksel olasılıklarla iddiayı `TUTTU`, `KISMEN TUTTU`, `TUTMADI` veya `BELİRSİZ` olarak etiketler.
4. **Aşama 4 (Statik Site ve Raporlama):** Her iddia işlendiğinde atomik olarak JSON dosyasına kaydedilir ve anında GitHub Pages için Markdown sayfalarına dönüştürülür.

---

## ⚠️ Önemli Sorumluluk Reddi (Yapay Zeka Beyanı)

> [!WARNING]
> **Yapay Zeka Değerlendirmesi Hakkında Bilgilendirme**
> 1. **Tamamen Yapay Zeka Tarafından Üretilmiştir:** Bu depoda ve web sitesinde yer alan tüm iddia ayıklamaları, internet aramaları, kanıt alıntıları ve sınıflandırma kararları **insan müdahalesi olmaksızın otonom yapay zeka modelleri tarafından** üretilmiştir.
> 2. **Yüzde Yüz Güvenilirlik Garantisi Yoktur:** Doğal dil işleme modelleri konuşma dilindeki mecazları, şakaları veya yerel bağlamı zaman zaman yanlış yorumlayabilir; arama motorları ise konuyu tam yansıtmayan kaynaklar döndürebilir. Sonuçlar mutlak gerçeklik değil, bir model değerlendirmesidir.
> 3. **Amaç:** Bu çalışma şahsi bir karne veya bağlayıcı bir doğruluk sicili değildir; açık kaynaklı siber güvenlik arşivciliği ve yapay zeka tabanlı otonom araştırma yöntemlerini test etme amacı taşır.
> 4. **Düzeltmeler:** Hatalı veya eksik değerlendirildiğini düşündüğünüz iddialar için Issue veya Pull Request açabilirsiniz.

---

## 🚀 Kurulum ve Yerel Çalıştırma

### 1. Gereksinimler

```bash
pip install -r requirements.txt
playwright install chromium
```

### 2. Kimlik Doğrulama

NotebookLM oturumu için Google hesabınızla giriş yapın:
```bash
python -m notebooklm login
```

### 3. Pipeline'ı Çalıştırma

Tüm 179 videoyu taramak, arama yapmak ve kararları üretmek için:
```bash
python sah_hibrit_final.py
```
*Script kesintiye uğrasa dahi `sah_hibrit_checkpoint.json` üzerinden kaldığı videodan ve iddiadan devam eder.*

### 4. Web Sitesini Yerel Olarak Önizleme (SSG)

Sade, açık renkli MkDocs arayüzünü yerel tarayıcınızda görmek için:
```bash
python -m mkdocs serve
```
Tarayıcınızda `http://127.0.0.1:8000` adresini açarak siteyi inceleyebilirsiniz.

---

## 🌐 GitHub Pages Otomatik Yayını

Bu depoda `.github/workflows/deploy.yml` GitHub Actions iş akışı hazır bulunmaktadır. Depoyu GitHub'a `main` dalı üzerinden push ettiğinizde site otomatik olarak derlenip GitHub Pages üzerinden yayına alınır.
