"""main.py
Run the genetic algorithm.
"""

import sys

from population import Population

__author__ = "Tim de Klijn"

GENES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,.!? "
GENE_LENGTH = len(GENES)

TARGET = "To be, or not to be."
TARGET_LENGTH = len(TARGET)

POPULATION_SIZE = 300
MUTATION_RATE = 0.01

def main():
    """docstring"""

    print(f"""
Target: {TARGET}
Population Size: {POPULATION_SIZE}
Mutation_rate: {MUTATION_RATE}
""")

    population = Population(GENES,
                            GENE_LENGTH,
                            POPULATION_SIZE,
                            TARGET,
                            TARGET_LENGTH,
                            MUTATION_RATE)
    population.init_population()
    population.calc_fitness()
    max_fitness = population.max_fitness

    breed = True
    iteration = 0

    while breed:
        iteration += 1
        max_fitness = population.max_fitness

        sys.stdout.flush()
        sys.stdout.write("\r")
        sys.stdout.flush()
        sys.stdout.write(
            f"{iteration:>5} : {max_fitness:.2f} : {population.population[0].dna}")

        population.create_offspring()
        population.calc_fitness()

        if max_fitness == 1.0:
            breed = False

    print("\n\nFinished\n")


if __name__ == "__main__":
    main()
