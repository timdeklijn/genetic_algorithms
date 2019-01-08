const populationSize = 200;
const DNASize = 1000;
const mutationRate = 0.01;
const box = { x: 300, y: 300, w: 500, h: 50 };

let population;
let genCount = 1;
population = new Population();

function setup() {
  createCanvas(800, 600);
  // initiate population
  population.init();
}

function draw() {
  background(250, 250, 250);
  // Generation counter
  textSize(25);
  noStroke();
  fill(30);
  textFont("Courier New");
  text(`Generation: ${genCount}`, 10, 30);
  // Draw goal
  fill(0, 150, 150);
  strokeWeight(2);
  stroke(0);
  ellipse(width / 2, 100, 50, 50);
  // Draw obstacles
  fill(30);
  rect(box.x, box.y, box.w, box.h);

  // Update population
  population.update();
  if (population.alive_count == 0) {
    population.newPopulation();
    genCount += 1;
  }
}
