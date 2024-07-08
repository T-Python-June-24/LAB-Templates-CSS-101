document.addEventListener("DOMContentLoaded", (event) => {
  const fadeElements = document.querySelectorAll(".fade-in");
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
          }
        });
      },
      {
        threshold: 0.1,
      }
    );
    fadeElements.forEach((el) => observer.observe(el));

    // Add random stars
    const bgImage = document.querySelector(".bg-image");
    for (let i = 0; i < 100; i++) {
      const star = document.createElement("div");
      star.classList.add("star");
      star.style.left = `${Math.random() * 100}%`;
      star.style.top = `${Math.random() * 100}%`;
      star.style.animationDelay = `${Math.random() * 2}s`;
      bgImage.appendChild(star);
    }

    // Add multiple comets
    for (let i = 0; i < 3; i++) {
      const comet = document.createElement("div");
      comet.classList.add("comet");
      comet.style.top = `${Math.random() * 100}%`;
      comet.style.animationDelay = `${Math.random() * 10}s`;
      bgImage.appendChild(comet);
    }
});
