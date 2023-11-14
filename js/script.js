let slideInterval;

function nextSlide() {
  let slide = document.getElementById("slide");
  let lists = document.querySelectorAll(".item");
  let firstItem = lists[0];
  slide.removeChild(firstItem);
  slide.appendChild(firstItem);
}

function startAutoSlide() {
  slideInterval = setInterval(nextSlide, 5000); // Slide every 2 seconds (2000 milliseconds)
}

function stopAutoSlide() {
  clearInterval(slideInterval);
}

document.getElementById("next").onclick = function () {
  nextSlide();
  stopAutoSlide(); // Stop auto slide when manually changing the slide
};

document.getElementById("prev").onclick = function () {
  let slide = document.getElementById("slide");
  let lists = document.querySelectorAll(".item");
  let lastItem = lists[lists.length - 1];
  slide.removeChild(lastItem);
  slide.insertBefore(lastItem, slide.firstChild);
  stopAutoSlide(); // Stop auto slide when manually changing the slide
};

startAutoSlide(); // Start auto slide when the page loads

// Pause auto slide when the user hovers over the slide container
document.getElementById("slide").addEventListener("mouseenter", stopAutoSlide);
// Resume auto slide when the user moves the mouse out of the slide container
document.getElementById("slide").addEventListener("mouseleave", startAutoSlide);

// change text function
function changeTextToReadmore() {
  const cards = document.querySelectorAll(".Event-main");

  cards.forEach((card) => {
    const anchor = card.querySelector(".Event-News-footer a");

    card.addEventListener("mouseover", () => {
      anchor.textContent = "Readmore";
    });

    card.addEventListener("mouseout", () => {
      anchor.textContent = "Detail";
    });
  });
}

changeTextToReadmore();

//responsive bar change

const menuIcon = document.querySelector("#menu-icon");
const navList = document.querySelector(".navlist");
let isMenuOpen = false;

// Define the default menu content
const defaultMenuContent = `
    <li><a href="#">PROGRAM</a></li>
    <li><a href="#">ADMISSION</a></li>
    <li><a href="#Event-News">EVENT&NEWS</a></li>
    <li><a href="#">ABOUT</a></li>
    <li><a href="/login"><i class="ri-user-line"></i></a></li>
`;

// Function to update the menu content
function updateMenuContent() {
  if (window.innerWidth <= 1195) {
    if (isMenuOpen) {
      navList.innerHTML = `
                <li><a href="#">PROGRAM</a></li>
                <li><a href="#">ADMISSION</a></li>
                <li><a href="#Event-News">EVENT&NEWS</a></li>
                <li><a href="#">ABOUT</a></li>
                <li><a href="/login"><i class="ri-user-line"></i></a></li>
            `;
    } else {
      navList.innerHTML = defaultMenuContent;
    }
  }
}

// Initial update
updateMenuContent();

// Event listener for menu icon click
menuIcon.addEventListener("click", () => {
  if (window.innerWidth <= 990) {
    if (isMenuOpen) {
      // Close the menu
      navList.classList.remove("open");
    } else {
      // Open the menu
      navList.classList.add("open");
    }
  }

  isMenuOpen = !isMenuOpen;
});

// Event listener for window resize
window.addEventListener("resize", updateMenuContent);

//navbar-menu
function toggleMenu() {
  const menuIcon = document.querySelector("#menu-icon");
  const navList = document.querySelector(".navlist");

  menuIcon.addEventListener("click", () => {
    // navList.classList.toggle("bx-x");
    navList.classList.toggle("open");
  });
}

toggleMenu();

//scroll smooth
function applyScrollReveal(selector, options) {
  const sr = ScrollReveal(options);
  sr.reveal(selector);
}

// Usage
applyScrollReveal(".main-text", {
  distance: "65px",
  duration: 2600,
  delay: 450,
  reset: true,
  origin: "top",
});

applyScrollReveal(".icons", {
  distance: "65px",
  duration: 2600,
  delay: 450,
  reset: true,
  origin: "left",
});

applyScrollReveal(".main-img", {
  distance: "65px",
  duration: 2600,
  delay: 450,
  reset: true,
  origin: "right",
});

applyScrollReveal(".border-bottom", {
  distance: "65px",
  duration: 2600,
  delay: 100,
  reset: true,
  origin: "right",
});
