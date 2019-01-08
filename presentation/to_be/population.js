// Container for population
class Population {
  constructor(pop) {
    this.pop = pop;
    this.generation = 0;
  }

  // Create initial population
  initPopulation() {
    let init = [];
    for (let i = 0; i < populationSize; i++) {
      let ind = new Individual();
      ind.initGenome();
      ind.calcFitness();
      init.push(ind);
    }
    this.pop = init;
  }

  // Create population
  createPool() {
    this.pool = [];
    for (let i = 0; i < this.pop.length; i++) {
      let n = Math.floor(this.pop[i].fitness * 100);
      for (let j = 0; j < n; j++) {
        this.pool.push(this.pop[i]);
      }
    }
  }

  // Create offsprint
  offspring(a, b) {
    let splitVal = Math.floor(Math.random() * a.genome.length);
    let newGenome =
      a.genome.slice(0, splitVal) + b.genome.slice(splitVal, a.genome.length);
    newGenome = newGenome.split("");
    for (let i = 0; i < newGenome.length; i++) {
      if (Math.random() < mutationRate) {
        newGenome[i] = genes[Math.floor(Math.random() * genes.length)];
      }
    }
    return newGenome.join``;
  }

  // Create new population
  newPopulation() {
    let p = [];
    for (let i = 0; i < populationSize; i++) {
      let a = this.pool[Math.floor(Math.random() * this.pool.length)];
      let b = this.pool[Math.floor(Math.random() * this.pool.length)];
      let ind = new Individual(this.offspring(a, b));
      ind.calcFitness();
      p.push(ind);
    }
    this.pop = p;
  }

  // Calculate max fitnes of population
  sortFitness() {
    this.pop.sort((a, b) => {
      return b.fitness - a.fitness;
    });
  }
}
