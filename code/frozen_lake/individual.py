"""individual

Individual class, contains functions and values for individuals in
the gene pool.
"""

import numpy as np

class Individual():
    """
    Class containing info and functions on individuals in the
    population. Depending on value of dna, will create new
    dna or accept input.

    Parameters:
        genes (str): str with options to generate dna.
        target (str): str with target of evolution
        target_length (int): length of target
        dna (str): dna sequence of individual
    """

    def __init__(self,
                 env,
                 dna_length: int,
                 dna: str = None):

        self.env = env

        self.dna_length = dna_length

        if dna is None:
            self.dna = []
            for _ in range(self.dna_length):
                self.dna.append(self.env.action_space.sample())
        else:
            self.dna = dna

        self.fitness = self.calc_fitness()


    def calc_fitness(self) -> float:
        """
        Run environment with the current dna sequence. Each step the
        player is not done adds to the fitness score.

        TODO:
            * Make the shortes path important as well
        """

        self.env.reset()
        counter = 0
        fitness = 0
        for i in range(self.dna_length):
            _, reward, done, _ = self.env.step(self.dna[i])
            counter += 1
            if done:
                if reward != 0.0:
                    fitness = reward - (counter * 0.001)
                else:
                    fitness = counter * 0.001
                break
        return fitness


    def mix_dna(self, dna_2: str, mutation_rate: float) -> str:
        """
        Given a second DNA sequence, mix two sequences and return
        offspring DNA. Based on mutation rate, mutate certain genes.
        """

        new_dna = []
        for i in range(self.dna_length):
            choice = np.random.uniform()
            if choice < mutation_rate:
                new_gene = self.env.action_space.sample()
            else:
                new_gene = np.random.choice([self.dna[i], dna_2[i]])
            new_dna.append(new_gene)
        return new_dna
