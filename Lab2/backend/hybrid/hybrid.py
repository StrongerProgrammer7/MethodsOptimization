from backend.hybrid.modify_genetic import *
from backend.hybrid.modify_imunSystem import *

def getHistoryBestPoint(population,func):

    history_best_points = []
    for i in range(len(population)):
        history_best_points.append((population[i][0],population[i][1],func(population[i][0],population[i][1])))
    return history_best_points


def hybrid(min_x,max_x,min_y,max_y,population_size,num_generations,func):
    #Создаём общую популяцию
    population = create_population(min_x,max_x,min_y,max_y,population_size)
    
    history_best_points = []
    best_point =(population[0][0],population[0][1], func(population[0][0],population[0][1]))
    
    for i in range(num_generations):
        gen_pop = genetic_algorithm(population,func)

        imun_pop = algorithm_artificial_immune_system(gen_pop,population_size,func,2)

        #Заменяем старую популяцию новой 
        population = imun_pop
        sort_pop = sorted(population,key=lambda x: func(x[0],x[1]))
        fitnessFunc = getHistoryBestPoint(sort_pop,func)
        history_best_points.append(fitnessFunc[0:5])

        if best_point[2]>func(sort_pop[0][0],sort_pop[0][1]):
            best_point = (sort_pop[0][0], sort_pop[0][1], func(sort_pop[0][0], sort_pop[0][1]))

    return best_point,history_best_points
        

# # Запуск генетического алгоритма
# population_size = 100
# num_generations = 100
# points,bestPoint = hybrid(population_size, num_generations,Rosenbrock)
#
# for i in points:
#     print(i)
#
# print("Лучшая точка: "+str(bestPoint))
