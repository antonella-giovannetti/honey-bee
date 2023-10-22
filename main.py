import csv
import matplotlib.pyplot as plt
import cProfile
import pstats
from beehive import Beehive
import numpy as np  

def load_flowers(file_path):
    flowers = []
    with open(file_path, newline='') as file:
        content = csv.reader(file, delimiter=",")
        for line in content:
            line = tuple(map(int, line))
            flower_tuple = tuple(line)
            flowers.append(flower_tuple)
    return flowers

def main():
    num_generations = 100
    num_bees = 100
    flowers = load_flowers('flowers.csv')
    beehive = Beehive(num_bees, flowers)
    beehive.initialize_bees() 
    best_bee = None
    best_score = float('inf')
    generation_scores = []
    all_bees_scores = []

    for i in range(num_generations):
        beehive.evolve_generation()
        current_best_bee = min(beehive.bees, key=lambda bee: bee.performance_score)
        if current_best_bee.performance_score < best_score:
            best_bee = current_best_bee
            best_score = current_best_bee.performance_score
        generation_scores.append(best_score)
        all_scores = [bee.performance_score for bee in beehive.bees]
        all_bees_scores.append(all_scores)

    average_scores = [np.mean(scores) for scores in all_bees_scores]

    plt.figure(figsize=(18, 4))

    # parcours de la meilleure abeille
    plt.subplot(131)
    best_path = best_bee.genes
    x, y = zip(*best_path)
    plt.plot(x, y, marker='o')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title("Best Bee's Path")

    # évolution du score de performance de la meilleure abeille
    plt.subplot(132)
    plt.plot(range(num_generations), generation_scores)
    plt.xlabel('Generation')
    plt.ylabel("Best Bee's Performance Score")
    plt.title("Evolution of Best Bee's Performance Score")

    # moyenne du score de performance global (toutes les abeilles)
    plt.subplot(133)
    plt.plot(range(num_generations), average_scores, color='green', label='Average Score')
    plt.xlabel('Generation')
    plt.ylabel('Average Performance Score')
    plt.title('Average Performance Score of All Bees')
    plt.legend()

    plt.tight_layout()
    plt.show()
    
if __name__ == '__main__':
    main()