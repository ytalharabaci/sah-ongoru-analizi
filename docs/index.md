# Siber Alemden Havadisler (S.A.H) — Gelecek Tahminleri Analizi

Utku Şen'in YouTube'da sunduğu **"Siber Alemden Havadisler" (S.A.H)** serisini takip edenler bilir, haftalık siber güvenlik haberlerini yorumlarken geleceğe dair sık sık şahsi öngörülerde bulunur.

Bu açık kaynaklı çalışmada 179 bölümlük video arşivinin tüm transkriptleri yapay zekaya taratıldı. Utku'nun haberler haricinde kendi tecrübesiyle dile getirdiği şahsi tahminler ayıklandı ve güncel internet kanıtlarıyla hangilerinin tutup hangilerinin tutmadığı test edildi.

<div class="kpi-grid">
  <div class="kpi-card">
    <div class="kpi-value">179</div>
    <div class="kpi-label">Taranan Video</div>
    <div class="kpi-sub">Bölüm Başına Tekil Bağlam</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-value">370</div>
    <div class="kpi-label">Şahsi Gelecek Tahmini</div>
    <div class="kpi-sub">Haberlerden Ayıklanan İddia</div>
  </div>
  <div class="kpi-card kpi-success">
    <div class="kpi-value">%61.3</div>
    <div class="kpi-label">Doğrulanan Başarı Oranı</div>
    <div class="kpi-sub">150 Tuttu + 77 Kısmen Tuttu</div>
  </div>
</div>

<div class="hero-actions">
  <a href="arsiv/" class="btn-primary">Tüm Tahminleri İncele (370 İddia)</a>
  <a href="metodoloji/" class="btn-secondary">Metodoloji ve Detaylar</a>
</div>

---

## Önemli Not (Yapay Zeka Uyarısı)

!!! warning "Sonuçlara körü körüne güvenmeyin!"
    - **Tamamen Yapay Zeka Tarafından Üretildi:** Bu sitedeki tüm özetler, internet aramaları ve doğruluk kararları insan editör müdahalesi olmadan yapay zeka modelleri tarafından oluşturuldu.
    - **Yüzde Yüz Güvenilirlik Garantisi Yok:** Modeller konuşma dilindeki esprileri veya kinayeli ifadeleri bazen yanlış yorumlayabiliyor, arama motorları da konudan alakasız sayfalar getirebiliyor. Sonuçlar mutlak bir hakikat değil, model değerlendirmesidir.
    - **Amaç:** Bu çalışma Utku Şen'e bir karne çıkarma amacı taşımıyor. Siber güvenlik muhabbetlerini yad etmek ve yapay zeka ajanlarının araştırma kabiliyetini eğlenceli bir senaryoda denemek için hazırlandı.

---

## Genel Sonuç Tablosu (179 Bölümün Özeti)

179 bölümün tamamı tarandı ve toplam **370 adet şahsi gelecek tahmini** değerlendirildi:

| Durum | Adet | Oran | Ortalama Güven | Anlamı |
| :--- | :---: | :---: | :---: | :--- |
| <span class="badge-tuttu">TUTTU</span> | **150** | %40.5 | 6.5 / 10 | İddia somut olarak gerçekleşti, teknik haberlerde ve web kaynaklarında net kanıtı var. |
| <span class="badge-kismen">KISMEN TUTTU</span> | **77** | %20.8 | 4.7 / 10 | İddianın ana yönü doğru çıktı ancak zamanlama veya hedefte kısmi sapma oldu. |
| <span class="badge-tutmadi">TUTMADI</span> | **45** | %12.2 | 6.9 / 10 | İddianın tam tersi gerçekleşti veya aradan geçen yıllara rağmen beklenti gerçekleşmedi. |
| <span class="badge-belirsiz">BELİRSİZ</span> | **98** | %26.5 | 5.6 / 10 | Web bulguları iddiayı doğrulamak ya da çürütmek için yetersiz kaldı veya iddianın vadesi henüz dolmadı. |
| **Toplam** | **370** | **%100** | - | **Doğrulanan Toplam Başarı (Tuttu + Kısmen): %61.3** |

---

## Nasıl Çalışıyor?

```mermaid
flowchart LR
    A["Transkript Taraması<br/>(NotebookLM)"] --> B["Web Araması<br/>(Tavily + DDG)"]
    B --> C["Karar Modeli<br/>(Gemini Decision 1)"]
    C --> D["Canlı Site<br/>(GitHub Pages)"]
```

1. **NotebookLM:** Videolar birbirine karışmadan tek tek taranıyor. Şirketlerin basın bültenleri elenip sadece Utku'nun kendi tahminleri toplanıyor. Taranan 179 videonun transkriptlerini barındıran açık defteri buradan inceleyebilirsiniz: **[Google NotebookLM Defteri](https://notebook.google.com/notebook/f2e75aa1-ef9d-4e1c-a281-95885383785a)**
2. **Tavily ve DuckDuckGo:** Teknik sitelerden doğrudan ilgili makale paragrafları çekiliyor, Türkçe yerel haberlerle kanıt havuzu tamamlanıyor.
3. **Gemini Decision 1:** Model, iddiayı ve web bulgularını inceleyerek olasılık dağılımı üzerinden nihai kararını veriyor.
4. **MkDocs:** Sonuçlar anında web sayfalarına işleniyor ve GitHub Pages üzerinden yayınlanıyor.

Daha fazla teknik detay için **[Metodoloji ve Şeffaflık](metodoloji.md)** sayfasına göz atabilirsiniz.
