// Container for individuals
class Individual {
  constructor(genome) {
    this.genome = genome;
  }

  // Create random genome of length of target
  initGenome() {
    this.genome = [...Array(target.length)].map(
      _ => genes[Math.floor(Math.random() * genes.length)]
    ).join``;
  }

  // Calucate fitness of individual
  calcFitness() {
    let f = 0;
    for (let i = 0; i < this.genome.length; i++) {
      if (this.genome[i] == target[i]) {
        f += 1;
      }
    }
    this.fitness = f / this.genome.length;
  }
}
