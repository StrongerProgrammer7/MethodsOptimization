import random

# Создание начальной популяции
def create_population(min_x, max_x, min_y, max_y, population_size):
    return [(random.uniform(min_x, max_x), random.uniform(min_y, max_y)) for _ in range(population_size)]

# Вычисление пригодности (fitness) для каждой особи в популяции
def compute_fitness(population,function):
    fitness_scores = []
    for ind in population:
        x, y = ind
        fitness_scores.append(function(x, y))
    return fitness_scores

# Селекция (выбор лучших особей)
def select_best_individuals(population, fitness_scores, num_parents):
    selected_indices = sorted(range(len(fitness_scores)), key=lambda i: fitness_scores[i])[:num_parents]
    return [population[i] for i in selected_indices]

# Скрещивание (кроссовер)
def crossover(parents, offspring_size):
    offspring = []
    while len(offspring) < offspring_size:
        parent1, parent2 = random.sample(parents, 2)
        crossover_point = random.randint(1, len(parent1) - 1)
        child = parent1[:crossover_point] + parent2[crossover_point:]
        offspring.append(child)
    return offspring

# Мутация
def mutate(offspring):
    mutated_offspring = []
    for child in offspring:
        x, y = child
        if random.random() < 0.1:  # Вероятность мутации
            x += random.uniform(-0.5, 0.5)
            y += random.uniform(-0.5, 0.5)
        mutated_offspring.append((x, y))
    return mutated_offspring
