# Gelecek Öngörüleri Analizi

Utku Şen'in YouTube'da sunduğu **"Siber Alemden Havadisler" (S.A.H)** serisini takip edenler bilir, haftalık siber güvenlik haberlerini yorumlarken geleceğe dair sık sık şahsi öngörülerde bulunur.

Bu açık kaynaklı çalışmada 179 bölümlük serinin tüm video transkriptleri yapay zekaya taratıldı. Utku'nun haberler haricinde kendi tecrübesiyle dile getirdiği şahsi tahminler ayıklandı ve güncel internet kanıtlarıyla hangilerinin tutup hangilerinin tutmadığı test edildi.

<div class="kpi-grid">
  <div class="kpi-card">
    <div class="kpi-value">179</div>
    <div class="kpi-label">Taranan Video</div>
    <div class="kpi-sub">Bölüm Başına Tekil Bağlam</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-value">272</div>
    <div class="kpi-label">Sonuçlanan Tahmin</div>
    <div class="kpi-sub">370 İddia içinden 98'i Belirsiz</div>
  </div>
  <div class="kpi-card kpi-success">
    <div class="kpi-value">%83.5</div>
    <div class="kpi-label">Doğrulanan Başarı Oranı</div>
    <div class="kpi-sub">150 Tuttu + 77 Kısmen Tuttu</div>
  </div>
</div>

<div class="hero-actions">
  <a href="arsiv/" class="btn-primary">Tahminleri İncele (370 İddia)</a>
  <a href="metodoloji/" class="btn-secondary">Metodoloji</a>
</div>

---

## Önemli Not (Yapay Zeka Uyarısı)

!!! warning "Sonuçlara körü körüne güvenmeyin!"
    - **Tamamen Yapay Zeka Tarafından Üretildi:** Bu sitedeki tüm özetler, internet aramaları ve doğruluk kararları insan editör müdahalesi olmadan yapay zeka modelleri tarafından oluşturuldu.
    - **Yüzde Yüz Güvenilirlik Garantisi Yok:** Modeller konuşma dilindeki esprileri veya kinayeli ifadeleri bazen yanlış yorumlayabiliyor, arama motorları da konudan alakasız sayfalar getirebiliyor. Sonuçlar mutlak bir hakikat değil, model değerlendirmesidir.
    - **Amaç:** Bu çalışma Utku Şen'e bir karne çıkarma amacı taşımıyor. Siber güvenlik muhabbetlerini yad etmek ve yapay zeka ajanlarının araştırma kabiliyetini eğlenceli bir senaryoda denemek için hazırlandı.

---

## Genel Sonuç Tablosu (179 Bölümün Özeti)

179 bölümün tamamı tarandı ve toplam **370 adet şahsi gelecek tahmini** değerlendirildi. Tahmin piyasaları metodolojisine uygun olarak, vadesi henüz dolmayan veya açık web kanıtı bulunmayan 98 belirsiz iddia başarı oranını olumsuz etkilememesi için paydadan muaf tutulmuştur:

<div class="progress-section">
  <div class="progress-bar-container">
    <div class="progress-segment seg-tuttu" style="width: 40.5%" title="Tuttu: 150 (%40.5)">%40.5</div>
    <div class="progress-segment seg-kismen" style="width: 20.8%" title="Kısmen Tuttu: 77 (%20.8)">%20.8</div>
    <div class="progress-segment seg-belirsiz" style="width: 26.5%" title="Belirsiz: 98 (%26.5)">%26.5</div>
    <div class="progress-segment seg-tutmadi" style="width: 12.2%" title="Tutmadı: 45 (%12.2)">%12.2</div>
  </div>
  <div class="progress-legend">
    <span class="legend-item"><span class="legend-dot dot-tuttu"></span> Tuttu (150)</span>
    <span class="legend-item"><span class="legend-dot dot-kismen"></span> Kısmen Tuttu (77)</span>
    <span class="legend-item"><span class="legend-dot dot-belirsiz"></span> Belirsiz (98)</span>
    <span class="legend-item"><span class="legend-dot dot-tutmadi"></span> Tutmadı (45)</span>
  </div>
</div>

| Durum | Adet | Sonuçlananlar İçi Oran (272) | Tüm Arşiv İçi Oran (370) | Ortalama Güven | Anlamı |
| :--- | :---: | :---: | :---: | :---: | :--- |
| <span class="badge-tuttu">TUTTU</span> | **150** | **%55.1** | %40.5 | 6.5 / 10 | İddia somut olarak gerçekleşti, teknik haberlerde ve web kaynaklarında net kanıtı var. |
| <span class="badge-kismen">KISMEN TUTTU</span> | **77** | **%28.3** | %20.8 | 4.7 / 10 | İddianın ana yönü doğru çıktı ancak zamanlama veya hedefte kısmi sapma oldu. |
| <span class="badge-tutmadi">TUTMADI</span> | **45** | **%16.5** | %12.2 | 6.9 / 10 | İddianın tam tersi gerçekleşti veya aradan geçen yıllara rağmen beklenti gerçekleşmedi. |
| <span class="badge-belirsiz">BELİRSİZ</span> | **98** | *Kapsam Dışı* | %26.5 | 5.6 / 10 | Web bulguları iddiayı doğrulamak ya da çürütmek için yetersiz kaldı veya iddianın vadesi henüz dolmadı. |
| **Sonuçlanan Tahminler** | **272** | **%100** | **%73.5** | - | **Doğrulanan Başarı (Tuttu + Kısmen): %83.5** |
| **Tüm Arşiv Toplamı** | **370** | - | **%100** | - | **Genel Oran (Belirsizler Dahil): %61.4** |

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

Daha fazla teknik detay için **[Metodoloji](metodoloji.md)** sayfasına göz atabilirsiniz.
