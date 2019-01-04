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
                 genes: str,
                 target: str,
                 target_length: int,
                 dna: str = None):

        self.genes = genes

        self.target = target
        self.target_length = target_length

        if dna is None:
            self.dna = "".join(
                np.random.choice(list(self.genes), self.target_length))
        else:
            self.dna = dna

        self.fitness = self.calc_fitness()


    def calc_fitness(self) -> float:
        """
        Calculate fitness score based on difference between current
        DNA sequence and target sequence
        """

        fitness = 0
        for i in range(self.target_length):
            if self.target[i] == self.dna[i]:
                fitness += 1
        return fitness / self.target_length


    def mix_dna(self, dna_2: str, mutation_rate: float) -> str:
        """
        Given a second DNA sequence, mix two sequences and return
        offspring DNA. Based on mutation rate, mutate certain genes.
        """

        new_dna = ""
        for i in range(self.target_length):
            choice = np.random.uniform()
            if choice < mutation_rate:
                new_gene = np.random.choice(list(self.genes))[0]
            else:
                new_gene = np.random.choice([self.dna[i], dna_2[i]])[0]
            new_dna += new_gene
        return new_dna
