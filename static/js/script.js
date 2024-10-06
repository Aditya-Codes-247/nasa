const planets = document.querySelectorAll(".planet");
let startTime = Date.now(); // Start time of the animation

function updatePositions() {
  const now = Date.now() - startTime; // Elapsed time since the start

  planets.forEach((planet, index) => {
    const orbitTime = (index + 1) * 5000; // Orbit time in milliseconds
    const distanceFromSun = (index + 1) * 50; // Distance from the sun in pixels
    const diameter = getPlanetDiameter(index + 1); // Diameter of the planet
    const angle = ((now % orbitTime) / orbitTime) * 360; // Current angle
    const x = distanceFromSun * Math.cos((angle * Math.PI) / 180); // X-position
    const y = distanceFromSun * Math.sin((angle * Math.PI) / 180); // Y-position

    planet.style.width = `${diameter}px`; // Set the width based on diameter
    planet.style.height = `${diameter}px`; // Set the height based on diameter
    planet.style.left = `calc(50% - ${diameter / 2}px + ${x}px)`; // Position based on distance and angle
    planet.style.top = `calc(50% - ${diameter / 2}px + ${y}px)`; // Position based on distance and angle
  });
}

function getPlanetDiameter(index) {
  const diameters = [12, 30, 32, 16, 200, 180, 120, 110, 8]; // Updated diameters in pixels for new sizes
  const scaleFactor = [1, 0.7, 0.6, 0.4, 0.2, 0.1, 0.08, 0.05, 0.02]; // Scaling factor for size relation
  return diameters[index - 1] * scaleFactor[index - 1]; // Return the diameter with scaling
}

function createStars() {
  const starField = document.querySelector(".star-field");
  const numStars = 100; // Number of stars

  for (let i = 0; i < numStars; i++) {
    const star = document.createElement("div");
    star.classList.add("star");
    star.style.left = `${Math.random() * 100}%`; // Random horizontal position
    star.style.top = `${Math.random() * 100}%`; // Random vertical position
    star.style.animationDelay = `${Math.random()}s`; // Random twinkle delay
    starField.appendChild(star);
  }
}

createStars();
setInterval(updatePositions, 1000 / 60); // Update every 16.67ms (~60 FPS)
