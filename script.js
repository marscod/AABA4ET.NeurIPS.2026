/* Reveal topic rows when they enter the viewport (respects reduced motion via CSS). */
(function () {
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
    { threshold: 0.15, rootMargin: "0px 0px -40px 0px" }
  );

  items.forEach((el) => observer.observe(el));
})();
