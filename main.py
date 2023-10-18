import random
import csv
from beehive import Bee, Reproduction

def load_flowers(file_path):
    flowers = []
    with open(file_path, newline='') as file:
        content = csv.reader(file, delimiter=",")
        for line in content:
            line = tuple(map(int, line))
            flower_tuple = tuple(line)
            flowers.append(flower_tuple)
    return flowers

flowers = load_flowers('flowers.csv')

# Première génération d'abeilles
bees = [Bee(f'bee_{i + 1}') for i in range(1, 101)]
for bee in bees:
    bee.set_genes(flowers)
    bee.set_fitness()

