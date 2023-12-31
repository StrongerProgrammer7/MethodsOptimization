import random

ROUND = 3
#Разделим пчёл на группы
def divide_bees_by_group(number_group_best, number_group_perspective, value):
    a = round((value / 100 * 70) / number_group_best, 0)
    b = round((value - a * number_group_best) / number_group_perspective, 0)
    return int(a),int(b)

#Гененрация новой точки в области старой с заданным диапазоном и границами
def create_new_point(min_x,max_x,now_x,spread_points):
    rand_x = round(random.uniform(now_x - spread_points, now_x + spread_points), ROUND)
    while(rand_x<min_x or rand_x>max_x):
        rand_x = round(random.uniform(now_x - spread_points, now_x + spread_points), ROUND)
    return rand_x

def algorithm_of_bees(min_x,max_x,min_y,max_y,number_of_bees,function,time):
    #Пчёлы-разведчики
    scout_bees =[]
    for i in range(number_of_bees):
        rand_x = round(random.uniform(min_x,max_x),ROUND)
        rand_y = round(random.uniform(min_y,max_y),ROUND)
        z = round(function(rand_x,rand_y),ROUND)
        scout_bees.append([[rand_x,rand_y],z])




    #Результат первой разведки
    sort_scout_bees = sorted(scout_bees, key = lambda x:x[1])

    #Количество лучших зон
    number_best_zone = 3
    #Количество перспективных зон
    number_perspective_zone = 5
    #Разброс точек
    spread_points = 5
    #Список лучших точек в каждом вылете
    history_best_point = []
    #запомним лучшую точку (минимальную)
    best_point = sort_scout_bees[0]
    for i in range(time):
        #Запоменим лучшую точку
        history_best_point.append(sort_scout_bees[0:5])
        # Запишем лучшие зоны
        best_zones = []
        # Проверяем
        if (best_point[1]>sort_scout_bees[0][1]):
            best_point = sort_scout_bees[0]

        #Запишем перспективные зоны
        perspective_zones = []
        #новая группа разведчиков
        new_scout_beens = []
        for i in range(number_best_zone):
            best_zones.append(sort_scout_bees[i][0])

        for i in range(number_perspective_zone):
            perspective_zones.append(sort_scout_bees[number_best_zone+i][0])

        val_best,val_persp = divide_bees_by_group(number_best_zone,number_perspective_zone,number_of_bees)

        for x,y in best_zones:
            for i in range(val_best):

                rand_x = round(create_new_point(min_x,max_x, x,spread_points),ROUND)
                rand_y = round(create_new_point(min_y, max_y, y, spread_points), ROUND)

                z = round(function(rand_x, rand_y), ROUND)
                new_scout_beens.append([[rand_x, rand_y], z])

        for x,y in perspective_zones:
            for i in range(val_persp):
                rand_x = round(create_new_point(min_x,max_x, x,spread_points),ROUND)
                rand_y = round(create_new_point(min_y, max_y, y, spread_points), ROUND)
                z = round(function(rand_x, rand_y), 3)
                new_scout_beens.append([[rand_x, rand_y], z])
         #Отсортируем еновые точки
        sort_scout_bees = sorted(new_scout_beens, key=lambda x: x[1])

    new_matrix = []
    for i in range(len(history_best_point)):
        for x_y, z in history_best_point[i]:
            new_matrix.append([x_y[0], x_y[1], z])

    return best_point,new_matrix


# rezusl,points = algorithm_of_bees(-10,10,-10,10,200,Rastrigin,1000)
# print(rezusl)
# for i in range(len(points)):
#     print("5 лучших точек на "+str(i+1)+"-ой итерации")
#     print(points[i])
#


