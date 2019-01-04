"""main.py
Run the genetic algorithm. Set global variables, then initiate the 
population. Run untill the proper fitness has been reached. Print
the fitnes and dna of the fittest individual of the generation.

Parameters:
    DNA_LENGTH: amount of 'actions' to optimize
    POPULATION_SIZE: Number of individuals per population
    MUTATION_RATE: Chance of a gene mutating during creation of 
        offspring
"""

__author__ = "Tim de Klijn"

import sys
import gym

from population import Population

from gym.envs.registration import register 

# Setup custom environment
register(
    id='FrozenLakeIsNotSlip-v0',
    entry_point='gym.envs.toy_text:FrozenLakeEnv', 
    kwargs={
        'map_name' : '8x8',
        'is_slippery': False}, 
    max_episode_steps=100, 
    reward_threshold=0.78)#, # optimum = .8196 )

env = gym.make('FrozenLakeIsNotSlip-v0')
env.is_slippery = False

# Global parameters
POPULATION_SIZE = 200
MUTATION_RATE = 0.02
DNA_LENGTH = 50

def run_dna(env, dna):
    """
    Given a environment and a dna sequence, run and show the sequence.
    """

    observation = env.reset()
    env.render()
    for i,s in enumerate(dna):
        observation, reward, done, info = env.step(s)
        env.render()
        if done:
            print(f"\n {i} steps needed")
            break
 

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

        population.create_offspring()
        population.calc_fitness()
        max_fitness = population.max_fitness

        dna_str = ''.join([str(i) for i in population.population[0].dna])

        # Print on a line in terminal, then print over it
        sys.stdout.flush()
        sys.stdout.write("\r")
        sys.stdout.flush()
        sys.stdout.write(f"{iteration:>5} : {max_fitness:.3f} : {dna_str}")

        if iteration == 100:
            breed = False

        iteration += 1

    print('\n\n')

    run_dna(env, population.population[0].dna)

    print("\n\nFinished\n")


if __name__ == "__main__":
    main()
