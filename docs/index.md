# Gelecek Öngörüleri Analizi

Utku Şen'in YouTube'da sunduğu **"Siber Alemden Havadisler" (S.A.H)** serisini takip edenler bilir, haftalık siber güvenlik haberlerini yorumlarken geleceğe dair sık sık şahsi öngörülerde bulunur.

Bu çalışmada 179 bölümlük serinin tüm konuşma metinleri yapay zekaya taratıldı. Utku'nun haber bültenleri haricinde kendi tecrübesiyle dile getirdiği şahsi tahminler ayıklandı ve güncel internet kanıtlarıyla hangilerinin tutup hangilerinin tutmadığı test edildi.

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
    - **Yüzde Yüz Güvenilirlik Garantisi Yok:** Modeller konuşma dilindeki esprileri veya kinayeli ifadeleri bazen yanlış yorumlayabiliyor, arama motorları da konudan bağımsız sayfalar getirebiliyor. Sonuçlar mutlak kesin bir doğru değil, model değerlendirmesidir.
    - **Amaç:** Bu çalışma Utku Şen'e karne ya da not verme amacı taşımıyor. Eski siber güvenlik muhabbetlerini anmak ve yapay zekanın araştırma yeteneklerini eğlenceli bir senaryoda denemek için hazırlandı.

---

## Genel Sonuç Tablosu (179 Bölümün Özeti)

179 bölümün tamamı incelendi ve toplam **370 şahsi gelecek tahmini** değerlendirildi. Henüz vadesi gelmemiş veya hakkında net bir internet kanıtı bulunmayan 98 belirsiz tahmin ayrı bir grupta tutuldu. Doğrulanan başarı oranı, akıbeti netleşmiş olan 272 tahmin üzerinden hesaplandı:

<div class="progress-section">
  <div class="progress-bar-container">
    <div class="progress-segment seg-tuttu" style="width: 40.5%" title="Tuttu: 150 (%40.5)">%40.5</div>
    <div class="progress-segment seg-kismen" style="width: 20.8%" title="Kısmen Tuttu: 77 (%20.8)">%20.8</div>
    <div class="progress-segment seg-tutmadi" style="width: 12.2%" title="Tutmadı: 45 (%12.2)">%12.2</div>
    <div class="progress-segment seg-belirsiz" style="width: 26.5%" title="Belirsiz: 98 (%26.5)">%26.5</div>
  </div>
  <div class="progress-legend">
    <span class="legend-item"><span class="legend-dot dot-tuttu"></span> Tuttu (150)</span>
    <span class="legend-item"><span class="legend-dot dot-kismen"></span> Kısmen Tuttu (77)</span>
    <span class="legend-item"><span class="legend-dot dot-tutmadi"></span> Tutmadı (45)</span>
    <span class="legend-item"><span class="legend-dot dot-belirsiz"></span> Belirsiz (98)</span>
  </div>
</div>

| Durum | Tahmin Sayısı | Netleşen Oran (272) | Tüm Arşiv Payı (370) | Açıklama |
| :--- | :---: | :---: | :---: | :--- |
| <span class="badge-tuttu">TUTTU</span> | **150** | **%55.1** | %40.5 | Somut olarak gerçekleşti, açık web kaynaklarıyla doğrulandı. |
| <span class="badge-kismen">KISMEN TUTTU</span> | **77** | **%28.3** | %20.8 | Ana fikir doğru çıktı, detay veya zamanda kısmi sapma oldu. |
| <span class="badge-tutmadi">TUTMADI</span> | **45** | **%16.5** | %12.2 | Gerçekleşmedi veya beklentinin tam aksi yönde gelişti. |
| **Doğrulanan Başarı (Tuttu + Kısmen)** | **227 / 272** | **%83.5** | **%61.4** | **Sonucu netleşen 272 tahminin 227'si başarıyla doğrulandı.** |
| <span class="badge-belirsiz">BELİRSİZ</span> | **98** | *Vadesi Dolmadı* | %26.5 | Vadesi henüz dolmadı (ör. 2028-2030) veya kanıtlar yetersiz. |
| **Toplam Değerlendirilen Arşiv** | **370** | - | **%100** | **179 video serisinden ayıklanan tüm şahsi tahmin havuzu.** |

---

## Nasıl Çalışıyor?

![Doğrulama Akışı](assets/akis.svg)

1. **NotebookLM:** Videolar birbirine karışmadan tek tek taranıyor. Şirketlerin basın bültenleri elenip sadece Utku'nun kendi tahminleri toplanıyor. Taranan 179 videonun konuşma metinlerini içeren deftere buradan doğrudan göz atabilirsiniz: **[Google NotebookLM Defteri](https://notebook.google.com/notebook/f2e75aa1-ef9d-4e1c-a281-95885383785a)**
2. **Tavily ve DuckDuckGo:** Teknik sitelerden doğrudan ilgili makale paragrafları çekiliyor, Türkçe yerel haberlerle kanıt havuzu tamamlanıyor.
3. **Gemini Decision 1:** Model, iddiayı ve web bulgularını inceleyerek olasılık dağılımı üzerinden nihai kararını veriyor.
4. **MkDocs:** Sonuçlar anında web sayfalarına işleniyor ve GitHub Pages üzerinden yayınlanıyor.

Daha fazla teknik detay için **[Metodoloji](metodoloji.md)** sayfasına göz atabilirsiniz.
