const target = "To be, or not to be.";
const populationSize = 200;
const mutationRate = 0.01;
const genes = [
  ..."abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789., !?"
];

// init variables
let population = new Population();

function setup() {
  createCanvas(800, 600);

  /* ------ Population initiation ------ */

  population.initPopulation();
  population.sortFitness();
}

function draw() {
  background(250, 250, 250);

  /* ------ Update population ------ */

  population.createPool();
  population.newPopulation();
  population.sortFitness();
  population.generation += 1;

  /* ------ Draw output ------ */

  // Constants
  textSize(25);
  textFont("Courier New");
  textAlign("right");
  text(
    `Population Size: ${populationSize}, Mutationrate: ${mutationRate}`,
    width - 20,
    50
  );
  strokeWeight(4);
  line(20, 70, width - 20, 70);
  textAlign("left");
  text(`Generation: ${population.generation}`, 20, 110);
  text(`Fitness: ${population.pop[0].fitness.toFixed(2)}`, 20, 150);
  line(20, 175, width - 20, 175);
  // Genomes
  textSize(25);
  for (let i = 0; i < 10; i += 1) {
    text(population.pop[i].genome, 20, 225 + i * 35);
  }
}
