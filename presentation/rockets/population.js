class Population {
  constructor() {
    this.pop = [];
  }

  /*
   * Initialize population, create new rockets
   */
  init() {
    for (let i = 0; i < populationSize; i += 1) {
      let r = new Rocket();
      r.initDNA();
      this.pop.push(r);
    }
  }

  /*
   * updat the population, draw the rockets, check amount alive
   */
  update() {
    this.alive_count = 0;
    for (let i = 0; i < this.pop.length; i += 1) {
      this.pop[i].update();
      this.pop[i].check();
      this.pop[i].draw();
      if (this.pop[i].alive) {
        this.alive_count += 1;
      }
    }
  }

  /*
   * Splice DNA, per gene random from one of the parents
   * Then apply mutation based on mutation rate
   */
  offspring(a, b) {
    let newGenome = [];
    for (let i = 0; i < a.dna.length; i++) {
      let r = random();
      if (r <= 0.5) {
        newGenome.push(a.dna[i]);
      } else {
        newGenome.push(b.dna[i]);
      }
    }
    for (let i = 0; i < newGenome.length; i++) {
      if (random <= mutationRate) {
        newGenome[i] = p5.Vector.random2D();
      }
    }
    return newGenome;
  }

  /*
   * Create new dna from two parents
   */
  newPopulation() {
    this.createPool();
    let p = [];
    for (let i = 0; i < populationSize; i++) {
      let a = this.pool[floor(random(this.pool.length))];
      let b = this.pool[floor(random(this.pool.length))];
      let dna = this.offspring(a, b);
      let r = new Rocket();
      r.dna = dna;
      p.push(r);
    }
    this.pop = p;
  }

  /*
   * Create a pool based on fitness values
   */
  createPool() {
    this.pool = [];
    for (let i = 0; i < this.pop.length; i++) {
      let n = Math.floor(this.pop[i].fitness * 100);
      for (let j = 0; j < n; j++) {
        this.pool.push(this.pop[i]);
      }
    }
  }
}
