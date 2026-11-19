/* Siber Alemden Havadisler (S.A.H) - Canlı Durum Filtreleme */

function initClaimFilter() {
  const filterButtons = document.querySelectorAll(".filter-btn");
  if (!filterButtons.length) return;

  filterButtons.forEach(btn => {
    btn.addEventListener("click", function () {
      filterButtons.forEach(b => b.classList.remove("active"));
      this.classList.add("active");

      const filter = this.getAttribute("data-filter");
      const cards = document.querySelectorAll(".claim-card");
      let visibleCount = 0;

      cards.forEach(card => {
        const status = card.getAttribute("data-status");
        if (filter === "ALL" || status === filter) {
          card.style.display = "";
          visibleCount++;
        } else {
          card.style.display = "none";
        }
      });

      // İlgili kategoride hiç iddiası kalmayan bölümleri gizle
      const groups = document.querySelectorAll(".episode-group");
      groups.forEach(group => {
        const visibleInGroup = group.querySelectorAll(".claim-card:not([style*='display: none'])");
        if (visibleInGroup.length === 0) {
          group.style.display = "none";
        } else {
          group.style.display = "";
        }
      });

      const countEl = document.getElementById("filter-count");
      if (countEl) {
        countEl.textContent = "Gösterilen: " + visibleCount + " / 370 Tahmin";
      }
    });
  });
}

// Sayfa ilk yüklendiğinde ve anlık sayfa geçişlerinde çalıştır
document.addEventListener("DOMContentLoaded", initClaimFilter);
if (typeof document$ !== "undefined") {
  document$.subscribe(initClaimFilter);
}
