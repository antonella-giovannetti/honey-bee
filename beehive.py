import random
import numpy as np

class Bee:
    def __init__(self, name):
        self.name = name
        self.genes = []
        self.hive = (500, 500)
        self.fitness = 0

    def set_genes(self, flowers):
        self.genes = [self.hive] + random.sample(flowers, len(flowers))

    def set_fitness(self):
        current_flower = self.hive
        distance_list = []
        for gene in self.genes:
            distance_list.append(self.distance(current_flower, gene))
            current_flower = gene
        self.fitness = sum(distance_list)

    def distance(self, x, y):
        return (abs(x[1] - x[0]) + abs(y[1] - y[0]))
    
class Reproduction:
    def __init__(self):
        self.parents = []

    def set_parents(self, bees_50): 
        print(len(bees_50))
        random.shuffle(bees_50)
        for i in range(0, len(bees_50), 2):
            if i + 1 < len(bees_50):
                pair = [bees_50[i], bees_50[i + 1]]
                self.parents.append(pair)
        print(len(self.parents))

    def union(self, flowers):
        parents1 = []
        parents2 = []
        for pair in self.parents:
            parents1.append(pair[0])
            parents2.append(pair[1])

        x = len(parents1) // 2
        children1 = parents1[:x] + parents2[x:]
        children2 = parents2[:x] + parents1[x:]
        flowers_positions = set(flowers)

        for i in range(len(children1)):
            if not isinstance(children1[i], Bee):
                children1[i] = flowers_positions.pop()
        
        for i in range(len(children2)):
            if not isinstance(children2[i], Bee):
                children2[i] = flowers_positions.pop()

        return children1, children2
        
