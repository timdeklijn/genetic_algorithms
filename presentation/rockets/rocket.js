class Rocket {
  constructor() {
    this.dna = [];
    this.life = DNASize;
    this.alive = true;
    this.count = 0;
    this.finish = false;
    this.position = createVector(width / 2, height - 10);
    this.velocity = createVector(0, 0);
  }

  /*
   * Draw the rocket as a line.
   * TODO -> color
   */
  draw() {
    strokeWeight(10);
    stroke(255);
    if (this.alive) {
      stroke(10, 175, 10);
    } else {
      stroke(175, 10, 10);
    }
    let v = this.velocity.normalize().mult(10);
    line(
      this.position.x,
      this.position.y,
      this.position.x + v.x,
      this.position.y + v.y
    );
  }

  /*
   * Check if rocket is at the edge of the screen or at the finish
   */
  check() {
    if ((this.position.x > width - 10) | (this.position.x < 10)) {
      this.alive = false;
    }
    if ((this.position.y > height - 10) | (this.position.y < 10)) {
      this.alive = false;
    }
    if (this.life == 0) {
      this.alive = false;
    }
    if (
      (this.position.x > box.x) &
      (this.position.x < box.x + box.w) &
      (this.position.y > box.y) &
      (this.position.y < box.y + box.h)
    ) {
      this.alive = false;
    }
    if (dist(this.position.x, this.position.y, width / 2, 100) < 25) {
      this.finish = true;
      this.alive = false;
    }
  }
  /*
   * Create initial random DNA consisting of random vectors
   */
  initDNA() {
    for (let i = 0; i < DNASize; i += 1) {
      this.dna.push(p5.Vector.random2D());
    }
  }

  /*
   * Update the velocity, position, fitness and some counters
   */
  update() {
    if (this.alive) {
      this.acceleration = this.dna[this.count];
      this.velocity = this.velocity.add(this.acceleration);
      this.velocity.limit(8);
      this.position = this.position.add(this.velocity);
      if (this.finish === false) {
        this.fitness =
          1 -
          dist(this.position.x, this.position.y, width / 2, 100) /
            (height - 10);
      } else {
        this.fitness = 1;
      }
      this.count += 1;
      this.life -= 1;
    }
  }
}
