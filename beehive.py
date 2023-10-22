import random
import numpy as np

class Bee:
    def __init__(self):
        self.genes = []
        self.performance_score = 0

    def set_genes(self, flowers):
        self.genes = random.sample(flowers, len(flowers))

    def calculate_performance(self):
        # conversion en tableau numpy
        genes_np = np.array(self.genes)
        # calcul de la distance entre chaque fleur
        distances = np.sum(np.abs(genes_np[:-1] - genes_np[1:]), axis=1)
        # somme des distances
        self.performance_score = np.sum(distances)
        
    def reproduce(self, parent1, parent2):
        child1 = Bee()
        child2 = Bee()
        crossover_point = random.randint(1, len(self.genes) - 1)
        child1_genes = parent1.genes[:crossover_point]
        child2_genes = parent2.genes[:crossover_point]
        missing_coords_child1 = [coord for coord in parent2.genes if coord not in child1_genes]
        missing_coords_child2 = [coord for coord in parent1.genes if coord not in child2_genes]
        child1_genes += missing_coords_child1
        child2_genes += missing_coords_child2
        child1.genes = child1_genes
        child2.genes = child2_genes
        return child1, child2

class Beehive:
    def __init__(self, num_bees, flowers):
        self.bees = [Bee() for _ in range(num_bees)]
        self.generation = 0
        self.average_scores = []
        self.flowers = flowers

    def initialize_bees(self):
        for bee in self.bees:
            bee.set_genes(self.flowers)
            bee.calculate_performance()
    
    def evolve_generation(self):
        self.bees.sort(key=lambda bee: bee.performance_score)
        best_bees = self.bees[:50]
        new_bees = []

        while len(new_bees) < len(self.bees):
            parent1, parent2 = random.sample(best_bees, 2)
            child1, child2 = parent1.reproduce(parent1, parent2)
            child1.calculate_performance()
            child2.calculate_performance()
            new_bees.extend([child1, child2])
        self.bees = new_bees