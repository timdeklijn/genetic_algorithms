"""population
population class for genetic algorithm. Contains initiation functions,
calls for fitness fvalues, creates genepool and regulates reproduction.
"""

from typing import List
import numpy as np

from individual import Individual


class Population():
    """
    Control population during running the genetic algorithm. Has 
    functions for creating a population, producing offspring and
    scoring the population.

    Parameters:
        genes (str): options to create dna from
        population_size (int): amount of individuals per generation
        target (str): target of evolution
        target_length (int): length of target
        mutation_rate (float): determines mutation during reproduction
    """

    def __init__(self,
                 genes: str,
                 population_size: int,
                 target: str,
                 target_length: int,
                 mutation_rate: float) -> None:

        self.genes = genes

        self.population: List[Individual] = []
        self.population_size: int = population_size

        self.target: str = target
        self.target_length: int = target_length

        self.mutation_rate: float = mutation_rate

        self.max_fitness: float = 0.0

    def init_population(self) -> None:
        """
        Create n individuals where n is the population
        size. Save these in self.population.
        """

        for _ in range(self.population_size):
            self.population.append(Individual(
                self.genes,
                self.target,
                self.target_length))


    def _create_p_list(self) -> None:
        """
        Create a list of fitness scores and scale it to have a sum
        of 1.
        """

        p_list = np.array([ind.fitness for ind in self.population])
        return p_list / np.sum(p_list)


    def create_offspring(self) -> None:
        """
        For population size, pick two individuals from the populatoin
        based on the fitness score and create offspring, this will be
        the new population.
        """

        new_population = []
        p_list = self._create_p_list()
        for _ in range(self.population_size):
            # Select to individuals, chance is scaled to fitness score
            parents = np.random.choice(self.population, 2, p=p_list)
            # Create new dna form parents
            new_dna = parents[0].mix_dna(
                parents[1].dna, self.mutation_rate)
            new_population.append(Individual(
                self.genes,
                self.target,
                self.target_length,
                new_dna))
        self.population = new_population


    def calc_fitness(self) -> None:
        """
        Sort the population and extract the maximal fitness from
        the population
        """
        self.population = sorted(
            self.population,
            key=lambda x: x.fitness,
            reverse=True)
        self.max_fitness = self.population[0].fitness
