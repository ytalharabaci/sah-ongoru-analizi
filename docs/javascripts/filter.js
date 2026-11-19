/* Siber Alemden Havadisler (S.A.H) - Canlı Durum Filtreleme ve Tarih Sıralama */

function initClaimFilter() {
  const filterButtons = document.querySelectorAll(".filter-btn");
  const sortButtons = document.querySelectorAll(".sort-btn");
  if (!filterButtons.length && !sortButtons.length) return;

  let currentFilter = "ALL";
  let currentSort = "asc";

  function applyFilter() {
    const cards = document.querySelectorAll(".claim-card");
    let visibleCount = 0;

    cards.forEach(card => {
      const status = card.getAttribute("data-status");
      if (currentFilter === "ALL" || status === currentFilter) {
        card.style.display = "";
        visibleCount++;
      } else {
        card.style.display = "none";
      }
    });

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
  }

  function applySort(direction) {
    currentSort = direction;
    const groups = Array.from(document.querySelectorAll(".episode-group"));
    if (!groups.length) return;

    const parent = groups[0].parentNode;

    groups.sort((a, b) => {
      const dateA = a.getAttribute("data-date") || "";
      const dateB = b.getAttribute("data-date") || "";
      return direction === "asc"
        ? dateA.localeCompare(dateB)
        : dateB.localeCompare(dateA);
    });

    groups.forEach(group => parent.appendChild(group));
  }

  filterButtons.forEach(btn => {
    btn.addEventListener("click", function () {
      filterButtons.forEach(b => b.classList.remove("active"));
      this.classList.add("active");
      currentFilter = this.getAttribute("data-filter");
      applyFilter();
    });
  });

  sortButtons.forEach(sBtn => {
    sBtn.addEventListener("click", function () {
      sortButtons.forEach(b => b.classList.remove("active"));
      this.classList.add("active");
      const dir = this.getAttribute("data-sort");
      applySort(dir);
    });
  });
}

// Sayfa ilk yüklendiğinde ve anlık sayfa geçişlerinde çalıştır
document.addEventListener("DOMContentLoaded", initClaimFilter);
if (typeof document$ !== "undefined") {
  document$.subscribe(initClaimFilter);
}
