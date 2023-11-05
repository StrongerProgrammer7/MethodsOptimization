import random
from Lab2.backend.body_AIImmuneSystem import *

def antibody_selection(population,population_size,fitness_values):
    selected_population = []
    for _ in range(population_size):
        selected_index = random.choices(range(population_size), weights=[1 / v for v in fitness_values], k=1)[0]
        selected_population.append(population[selected_index])
    return selected_population

def mutation(selected_population,population_size,mutation_rate):
    for i in range(population_size):
        if random.random() < mutation_rate:
            x, y = selected_population[i]
            x += random.uniform(-0.1, 0.1)
            y += random.uniform(-0.1, 0.1)
            selected_population[i] = (x, y)
    return selected_population