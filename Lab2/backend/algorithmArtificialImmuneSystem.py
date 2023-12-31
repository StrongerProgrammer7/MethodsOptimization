

from backend.body_AIImmuneSystem import *

# Определение функции аффинности (минимизация функции Розенброка)
def algorithm_artificial_immune_system(min_x,max_x,min_y,max_y,population_size,function,generations):
    # Задайте параметры алгоритма
    mutation_rate = 0.1
    # Список лучших точек в каждой популяции
    history_best_point = []

    # Инициализация популяции антител
    population = [(random.uniform(min_x, max_x), random.uniform(min_y, max_y)) for _ in range(population_size)]
    
    # Основной цикл оптимизации
    for generation in range(generations):
        # Оценка функции аффинности для каждого антитела
        fitness_values = [function(x, y) for x, y in population]
    
        # Отбор антител
        selected_population = antibody_selection(population,population_size,fitness_values)
    
        # Мутация
        selected_population = mutation(selected_population,population_size,mutation_rate)

        #Запишем лучшую точку в данной популяции и её решение
        best_solution = min(population, key=lambda ind: function(ind[0], ind[1]))
        history_best_point.append((best_solution[0],best_solution[1],(function(best_solution[0], best_solution[1]))))
        # Замена старой популяции новой
        population = selected_population
    
    # Вывод лучшего решения
    best_solution = min(population, key=lambda ind: function(ind[0], ind[1]))

    return (best_solution[0],best_solution[1],function(best_solution[0], best_solution[1])), history_best_point


# best_point,points = algorithm_artificial_immune_system(-10,10,-10,10,200,Rosenbrock,500)
# for i in range(len(points)):
#     print("Лучшая точка на "+str(i+1)+"-ой итерации")
#     print(points[i])
# print("Лучшее решение (x, y):", best_point)