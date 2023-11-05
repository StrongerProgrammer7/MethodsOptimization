from Lab2.backend.body_genetic import *

def genetic_algorithm(population,function):
    population_size = len(population)

    fitness_scores = compute_fitness(population,function)
    parents = select_best_individuals(population, fitness_scores, population_size // 2)
    offspring = crossover(parents, population_size - len(parents))
    mutated_offspring = mutate(offspring)
    population = parents + mutated_offspring

    return population


