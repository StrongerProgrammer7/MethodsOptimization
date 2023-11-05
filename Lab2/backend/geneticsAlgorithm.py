from Lab2.backend.body_genetic import *
import global_variable as gv

def genetic_algorithm(min_x,max_x,min_y,max_y,population_size, num_generations, current_function):
    population = create_population(min_x,max_x,min_y,max_y,population_size)
    arr_points = []
    for generation in range(num_generations):
        fitness_scores = compute_fitness(population, current_function)
        parents = select_best_individuals(population, fitness_scores, population_size // 2)
        offspring = crossover(parents, population_size - len(parents))
        mutated_offspring = mutate(offspring)
        population = parents + mutated_offspring
        best_fitness = min(fitness_scores)
        #print(f"Поколение {generation + 1}: Лучшее значение функции Розенброка = {best_fitness}")
        arr_points.append(population[fitness_scores.index(min(fitness_scores))])


    best_solution = population[fitness_scores.index(min(fitness_scores))]

    points = []
    for x,y in arr_points:
        points.append([x,y,current_function(x,y)])

    return best_solution, min(fitness_scores),points

# Запуск генетического алгоритма
#population_size = 50
#num_generations = 100
#best_solution, best_fitness,arr_points = genetic_algorithm(population_size, num_generations,rosenbrock)
#print("Оптимальное значение функции Розенброка:", best_fitness)
#print("Оптимальные значения переменных:")
#print("x =", best_solution[0])
#print("y =", best_solution[1])
#print(arr_points)
