/* Mobile nav + topic reveal */
(function () {
  // GitHub Pages / browser cache often reuse HTML. Bust it on in-site clicks:
  // speakers.html → speakers.html?131
  document.addEventListener(
    "click",
    (e) => {
      const a = e.target.closest("a[href]");
      if (!a) return;
      const raw = a.getAttribute("href");
      if (!raw || raw.startsWith("#") || /^(mailto|tel|javascript):/i.test(raw)) return;
      if (a.hasAttribute("download")) return;
      let url;
      try {
        url = new URL(a.href);
      } catch {
        return;
      }
      if (url.origin !== location.origin) return;
      if (/\.(css|js|png|jpe?g|gif|webp|svg|pdf|xml|txt)$/i.test(url.pathname)) return;
      url.search = String(Math.floor(Math.random() * 1e9));
      a.setAttribute("href", url.pathname + url.search + url.hash);
    },
    true
  );

  const toggle = document.querySelector(".nav-toggle");
  const nav = document.querySelector(".site-nav");

  function closeNav() {
    if (!nav || !toggle) return;
    nav.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
  }

  if (toggle && nav) {
    toggle.addEventListener("click", (e) => {
      e.stopPropagation();
      const open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });

    nav.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => closeNav());
    });
  }

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeNav();
  });

  // Close menu when rotating / resizing up to desktop
  window.addEventListener("resize", () => {
    if (window.matchMedia("(min-width: 1101px)").matches) closeNav();
  });

  const items = document.querySelectorAll(".topic");
  if (!items.length || !("IntersectionObserver" in window)) return;

  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce) {
    items.forEach((el) => {
      el.style.opacity = "1";
      el.style.transform = "none";
      el.style.animation = "none";
    });
    return;
  }

  items.forEach((el) => {
    el.style.opacity = "0";
    el.style.animation = "none";
  });

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.style.animation = "rise 0.7s ease forwards";
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.12, rootMargin: "0px 0px -24px 0px" }
  );

  items.forEach((el) => observer.observe(el));
})();
