"""main.py
Run the genetic algorithm. Set global variables, then initiate the 
population. Run untill the proper fitness has been reached. Print
the fitnes and dna of the fittest individual of the generation.

Parameters:
    GENES (str): possibles genes in a string
    GENE_LENGTH (int): Lenght of GENES
    TARGET (str): target of evolution
    LEN_TARGET: length of the target
    POPULATION_SIZE: Number of individuals per population
    MUTATION_RATE: Chance of a gene mutating during creation of 
        offspring
"""

__author__ = "Tim de Klijn"

import sys
import gym

from population import Population

env = gym.make('FrozenLake-v0')
env.is_slippery = False

POPULATION_SIZE = 300
MUTATION_RATE = 0.01
DNA_LENGTH = 50


def main():
    """
    Control the genetic algorithm:
    
    First create a population. The population is passed all global 
    variables. Then initiate the population and calculate the fitness.
    Start the loop, print the current fitness and best dna sequence, 
    when max fitness is reached, break out of loop and quit.
    """

    print(f"""
Population Size: {POPULATION_SIZE}
Mutation_rate: {MUTATION_RATE}
DNA_length: {DNA_LENGTH}
""")

    population = Population(env,
                            POPULATION_SIZE,
                            MUTATION_RATE,
                            DNA_LENGTH)
    population.init_population()
    population.calc_fitness()
    max_fitness = population.max_fitness

    breed = True
    iteration = 0

    while breed:
        iteration += 1
        max_fitness = population.max_fitness

        # Print on a line in terminal, then print over it
        sys.stdout.flush()
        sys.stdout.write("\r")
        sys.stdout.flush()
        sys.stdout.write(
            f"{iteration:>5} : {max_fitness:.2f} : {population.population[0].dna}")

        population.create_offspring()
        population.calc_fitness()

        # Escape loop
        if max_fitness == 1.0:
            breed = False

    print("\n\nFinished\n")


if __name__ == "__main__":
    main()
