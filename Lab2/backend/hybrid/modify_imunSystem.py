from Lab2.backend.body_AIImmuneSystem import *

# Определение функции аффинности (минимизация функции Розенброка)
def algorithm_artificial_immune_system(population,population_size, function, generations):
    # Задайте параметры алгоритма
    mutation_rate = 0.1

    # Список лучших точек в каждой популяции
    # history_best_point = []

    # Основной цикл оптимизации
    for generation in range(generations):
        # Оценка функции аффинности для каждого антитела
        fitness_values = [function(x, y) for x, y in population]

        # Отбор антител
        selected_population = antibody_selection(population, population_size, fitness_values)

        # Мутация
        selected_population = mutation(selected_population, population_size, mutation_rate)

        # Замена старой популяции новой
        population = selected_population
        return population




