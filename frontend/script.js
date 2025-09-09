const elements = document.querySelectorAll('.fade-in');

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting)  {
      entry.target.classList.add('visible');
    }
  });
});

elements.forEach(el => observer.observe(el));

document.addEventListener("DOMContentLoaded", () => {
  const buyen = document.querySelector(".buypen")
  const options = document.querySelector(".options-wrapper");
  const onlineBtn = document.querySelector("#myButton");
  const penBtn = document.querySelector(".option2");
  const cards = document.querySelector("#cardsdiv");
  const startbutton = document.querySelector("#start");
  const backbutton = document.querySelector("#appearagag");
  const page = document.querySelector(".page");

  if (!options || !cards || !startbutton || !backbutton) return;

  cards.style.display = "none";
  backbutton.style.display = "none";

  function showCards(type) {
    localStorage.setItem("trainingType", type);
    options.style.display = "none";
    cards.style.display = "block";
    backbutton.style.display = "inline-block";
    page.style.filter = "blur(0)";
    cards.classList.add("visible");
  }

  onlineBtn.addEventListener("click", () => showCards("online"));
  penBtn.addEventListener("click", () => showCards("pen"));

  let hidden = false;

  startbutton.addEventListener("click", () => {
    cards.classList.add("hide");
    cards.style.display = "none";
    startbutton.style.display = "none";
    startbutton.textContent = "Continue";
    hidden = true;
  });

  backbutton.addEventListener("click", () => {
    cards.style.display = "block";
    cards.classList.remove("hide");
    cards.classList.add("visible");
    startbutton.textContent = "Continue";
    startbutton.style.display = "inline-block";
    hidden = false;
  });

  const saved = localStorage.getItem("trainingType");
  if (saved) {
    options.style.display = "none";
    cards.style.display = "block";
    backbutton.style.display = "inline-block";
    page.style.filter = "blur(0)";
    cards.classList.add("visible");
  }
});
