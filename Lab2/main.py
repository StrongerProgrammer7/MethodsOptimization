import numpy as np

from backend.Swarm_X2 import Swarm
from backend.algorithm_of_bees import algorithm_of_bees
from outer_imports.imports_tkinter import *
from outer_imports.matplotlib import *

import random

from global_variable import *
from frontshow.Color import *
from frontshow.placement_elements import createLabel

from backend.gradient_descent import gradient_descent
from backend.simplexMethod import get_points
from backend.geneticsAlgorithm import genetic_algorithm
from setFunction import *

def fillMatrix(resultFunction):
    temp = []
    tx,ty,tz = None,None,None
    for x, y, countIter, f in resultFunction:
        if tx != None and ty != None and tz != None and tx == x and ty == y and tz == f:
            continue
        temp.append([x, y, f])
        tx,ty,tz = x,y,f
    return temp

def getMatrixFromGenetics(result):
    temp = []
    tx, ty = None, None
    for x,y in result:
        if tx != None and ty != None and tx == x and ty == y:
            continue
        z = current_function(x,y)
        temp.append([x,y,z])
        tx, ty = x, y
    return temp


def isNotZeroPoints(arr,frame):
    return abs(round(arr[frame][0])) != 0 and abs(round(arr[frame][1])) != 0 and abs(round(arr[frame][2])) !=0

def animate(frame, arr,best_result=None, textReach=None, marker=None):
    if len(arr) > frame:
        size_point = SIZE_POINT
        color = Color.GREEN.value
        if (len(arr) - 1 == frame):
            color = Color.RED.value
            size_point = 100
            if(best_result!=None):
                bestPointSet.append(ax_3d.scatter(best_result[0], best_result[1], best_result[2], c=best_result[3], marker=best_result[4], s=best_result[5]))
        if (textReach != None):
            point_z = None
            if(len(arr[frame]) == 2):
                point_z = current_function(arr[frame][0],arr[frame][1])
            else:
                point_z = arr[frame][2]
            str_temp = "# " + str(frame) + " X=" + str(round(arr[frame][0], 4)) + " Y=" + str(round(arr[frame][1],4 )) + " Z=" + str(round(point_z, 4)) + "\n"
            textReach.insert(1.0, str_temp)
            if(len(arr) - 1 == frame):
                extraScatter.append(ax_3d.scatter(arr[frame][0], arr[frame][1], point_z, c=color, marker=marker, s=size_point, zorder=4))
            else:
                scatter_points.append(ax_3d.scatter(arr[frame][0], arr[frame][1], point_z, c=color, marker=marker, s=size_point,zorder=2))

            if(len(scatter_points)>15 and  len(arr)-2 > frame):
                random_countForDel = random.randint(2, 5)
                for i in range(0,random_countForDel):
                    randomPos = random.randint(0,len(scatter_points)-2)
                    scatter_points[randomPos].remove()
                    scatter_points.remove(scatter_points[randomPos])

def changeMatrixBeesPoint(points):
    new_matrix = []
    for i in range(len(points)):
        for j in range(len(points[i])):
            x_y = points[i][j][0]
            z = points[i][j][1]
            new_matrix.append([x_y[0],x_y[1],z])
    return new_matrix

def isNotEmptyFields(arrFields):
    for i in arrFields:
        if i.get() == "" and int(i.get()) == 0:
            print(int(i.get()))
            return False
    return True

def deleteDuplicateValue(matrix):
    newMatrix = []
    tx,ty = None , None
    lastPoint = matrix[len(matrix)-1]
    for arr in matrix:
        if tx != None and ty != None and tx == round(arr[0],5) and ty == round(arr[1],5) and arr[0] != lastPoint[0] and arr[1] != lastPoint[1]:
            continue
        newMatrix.append(arr)
        tx = round(arr[0],5)
        ty = round(arr[1],5)
    return newMatrix

def callGradient_DrawPoint(textFieldCountIter) -> None:
    try:
        if(len(x_data) > 0 and len(y_data) > 0 and int(textFieldCountIter.get()) > 10):
            temp = fillMatrix(list(gradient_descent(current_function, random.choice(x_data), random.choice(y_data), 0.1, int(textFieldCountIter.get()))))
            ani = FuncAnimation(fig_3d, animate, frames=len(temp), fargs=(temp, None,textReachGradientPoint,'o',), interval=SPEED,
                                repeat=False)
            canvas_3d.draw()
        else:
            print(len(x_data))
            print(len(y_data))
            print(int(textFieldCountIter.get()))
            messagebox.showerror("Error", "Invalid data. Fill defualt data and count iter.")
    except ValueError:
        messagebox.showerror("Error", "Invalid fillMatrix. Please check fill matrix and gradient_descent")

def call_simplex_method() -> None:
    try:
        if(len(x_data) > 0 and len(y_data) > 0 and current_function.__name__ == "quadratic"):
            temp = get_points(max(x_data),max(y_data),current_function)
            ani = FuncAnimation(fig_3d, animate, frames=len(temp), fargs=(temp, None,textReachQuadPoint,'x',), interval=SPEED, repeat=False)
            canvas_3d.draw()
        else:
            print(len(x_data))
            print(len(y_data))
            messagebox.showerror("Error", "Invalid data. Fill defualt data or choose other function. Simplex work only quadratic")
    except ValueError:
        messagebox.showerror("Error", "Invalid fillMatrix. Please check fill matrix and simplex_method")

def call_geneticsAlgorithm(tf_populationSize,tf_numGeneratics,lab_optimalFunc,lab_optimalValuePoints) -> None:
    try:
        if(len(x_data) > 0 and len(y_data) > 0 and isNotEmptyFields([tf_populationSize,tf_numGeneratics])):
            population_size,num_generations = int(tf_populationSize.get()),int(tf_numGeneratics.get())
            best_solution, best_fitness,arr_points = genetic_algorithm(population_size, num_generations,current_function)

            lab_optimalValuePoints.configure(text="Оптимальное значение функции: " + str(round(best_fitness,3)))
            lab_optimalFunc.configure(text="Оптимальное значение переменных: " + str(round(best_solution[0])) + " : " + str(round(best_solution[1])))
           # bestPointSet.append(ax_3d.scatter(best_solution[0], best_solution[1], best_fitness, c=Color.YELLOW.value, marker="o", s=250))
            bestResult = [best_solution[0], best_solution[1], best_fitness,Color.YELLOW.value,"o",250]

            points = getMatrixFromGenetics(arr_points)
            _ = FuncAnimation(fig_3d, animate, frames=len(points), fargs=(points,bestResult, textReachGeneraticPoints,'v',), interval=SPEED, repeat=False)
            canvas_3d.draw()
        else:
            print(len(x_data))
            print(len(y_data))
            messagebox.showerror("Error", "Invalid data. Fill defualt data and inputs: population size and count generatics")
    except ValueError:
        messagebox.showerror("Error", "Invalid fillMatrix. Please check fill matrix and genetric algorithm")

def call_Swarm(arr_textField) -> None:
    try:
        if(len(x_data) > 0 and len(y_data) > 0 and isNotEmptyFields(arr_textField)):
            sizeSwarm = int(arr_textField[0].get())
            curLocalVelociryRatio = float(arr_textField[1].get())
            locLocalVelociryRatio = float(arr_textField[2].get())
            globLocalVelociryRatio = float(arr_textField[3].get())
            print(globLocalVelociryRatio)
            numOfLife = int(arr_textField[4].get())

            a = Swarm(sizeSwarm, curLocalVelociryRatio, locLocalVelociryRatio, globLocalVelociryRatio, numOfLife, current_function, START, END)
            points = a.startSwarm()
            #print("РЕЗУЛЬТАТ:", a.globalBestScore, "В ТОЧКЕ:", a.globalBestPos)

           # bestPointSet.append(ax_3d.scatter(a.globalBestPos[0], a.globalBestPos[1], a.globalBestScore, c=Color.BLUE.value, marker="o", s=250))
            bestResult = [a.globalBestPos[0],a.globalBestPos[1],a.globalBestScore,Color.BLUE.value, "o",250]
            points = deleteDuplicateValue(points)
            _ = FuncAnimation(fig_3d, animate, frames=len(points), fargs=(points,bestResult, textReachSwarm,'x',), interval=SPEED, repeat=False)
            canvas_3d.draw()
        else:
            print(f"size x = {len(x_data)}")
            print(f"size y = {len(y_data)}")
            messagebox.showerror("Error", "Invalid data. Fill defualt data and inputs: size,lifes,velocity")
    except ValueError:
        messagebox.showerror("Error", "Invalid fillMatrix. Check swarm algorithm")

def call_Bees(arr_textField) -> None:
    try:
        if(len(x_data) > 0 and len(y_data) > 0 and isNotEmptyFields(arr_textField)):
            min_x = int(arr_textField[0].get())
            max_x = int(arr_textField[1].get())
            min_y = int(arr_textField[2].get())
            max_y = int(arr_textField[3].get())
            numBees = int(arr_textField[4].get())
            time = int(arr_textField[5].get())
            rezusl, points = algorithm_of_bees(min_x, max_x, min_y, max_y, numBees, current_function, time)
            bestResult = [rezusl[0][0], rezusl[0][1], rezusl[1], Color.CYAN.value, "o", 250]
            points = changeMatrixBeesPoint(points)

            _ = FuncAnimation(fig_3d, animate, frames=len(points), fargs=(points, bestResult, textReachBees, 'o',),
                              interval=SPEED, repeat=False)

            canvas_3d.draw()

            #messagebox.showerror("Error",      "Invalid data. min_y | min_x | max_x | max_y out of bounds BOUND: " + str(START) + ": " + str(END))
        else:
            print(f"size x = {len(x_data)}")
            print(f"size y = {len(y_data)}")
            messagebox.showerror("Error", "Invalid data. Fill defualt data and inputs: min_x,max_y,min_y,max_y,time,count bees")
    except ValueError:
        messagebox.showerror("Error", "Invalid fillMatrix. Check bees algorithm")


def save_plot():
    try:
        # Save the 3D plot to a file
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            fig_3d.savefig(file_path)
            messagebox.showinfo("Успех", "График сохранен.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the plot: {str(e)}")

def close_application():
    root.quit()

def buildBaseFunction():
    ax_3d.clear()

    ax_3d.set_title("3D Matplotlib Plot")
    ax_3d.set_xlabel("X-axis")
    ax_3d.set_ylabel("Y-axis")
    ax_3d.set_zlabel("Z-axis")
    global x_data
    global y_data
    if type(START) == dict:
        x_data = np.arange(START[1], START[2], STEP)
        y_data = np.arange(END[1], END[2], STEP)
    else:
        if(current_function.__name__ == "rosenbrock"):
            x_data = np.arange(-2, 2, STEP)
            y_data = np.arange(-1, 3, STEP)
        else:
            x_data = np.arange(START, END, STEP)
            y_data = np.arange(START, END, STEP)


    X, Y = np.meshgrid(x_data, y_data)
    Z = current_function(X, Y)

    ax_3d.plot_surface(X, Y, Z, cmap=ColorFigure.VIRIDIS.value,alpha=0.7, antialiased=True,rstride=1, cstride=1)
    canvas_3d.draw()

def clearPoints():
    for i in scatter_points:
        i.remove()
    if(len(bestPointSet) > 0):
        for i in bestPointSet:
            i.remove()
    if(len(extraScatter) > 0):
        for i in extraScatter:
            i.remove()
    textReachGradientPoint.delete(1.0,tk.END)
    textReachQuadPoint.delete(1.0, tk.END)
    textReachGeneraticPoints.delete(1.0,tk.END)
    textReachSwarm.delete(1.0,tk.END)
    canvas_3d.draw()
    scatter_points.clear()
    bestPointSet.clear()
    extraScatter.clear()

def selectFunc(event,combo,lab,textField):
    try:
        global STEP,START,END,current_function
        if len(textField.get()) > 0 and textField.get()!='' and float(textField.get())!=0:
            selection = combo.get()
            STEP = float(textField.get())
            if selection in chooseFunc:
                current_function = chooseFunc[selection]['f']
            if selection == "Букина":
                START = chooseFunc[selection]['x']
                END = chooseFunc[selection]['y']
            else:
                START = chooseFunc[selection]['from']
                END = chooseFunc[selection]['to']
            buildBaseFunction()
            lab.config(text="Функция:" + selection)
        else:
            messagebox.showerror("Error", "Invalid input. Please enter numeric values step.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

def createTab_gradient(tab):
    createLabel.placement_label(tab, "Количество итераций", 0, 1, 5, 1, 3, 5)
    textFieldCountIter = ttk.Entry(tab)
    textFieldCountIter.insert(0, "500")

    findMinGradientDescent_button = ttk.Button(tab, text="Выполнить градиентный спуск",
                                               command=lambda: callGradient_DrawPoint(textFieldCountIter))
    textFieldCountIter.grid(row=1, column=1, padx=5, pady=5, rowspan=1, columnspan=3, sticky="nsew")
    findMinGradientDescent_button.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

    global textReachGradientPoint
    textReachGradientPoint = ScrolledText(tab, height=10, width=30)
    textReachGradientPoint.grid(row=3,column=1, columnspan=3, padx=5, pady=5, sticky="nsew")


def createTab_simpleMethod(tab):
    findQud_btn = ttk.Button(tab, text='Вызов симплекс метода', command=lambda: call_simplex_method())
    findQud_btn.grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")
    global textReachQuadPoint
    textReachQuadPoint = ScrolledText(tab, height=10, width=30)
    textReachQuadPoint.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

def createTab_Genetic(tab):
    createLabel.placement_label(tab, "Размер популяции", 0, 1, 5, 1, 3, 5)
    textField_populationSize = ttk.Entry(tab)
    textField_populationSize.insert(0, "50")

    createLabel.placement_label(tab, "Количество генераций", 2, 1, 5, 1, 3, 5)
    textField_numGeneratics= ttk.Entry(tab)
    textField_numGeneratics.insert(0, "100")

    textField_populationSize.grid(row=1, column=1, padx=5, pady=5, rowspan=1, columnspan=3, sticky="nsew")
    textField_numGeneratics.grid(row=3, column=1, padx=5, pady=5, rowspan=1, columnspan=3, sticky="nsew")

    lab_optimalFunc = createLabel.placement_label(tab, "Оптимальное значение функции: ", 4, 1, 5, 1, 3, 5)
    lab_optimalValuePoints = createLabel.placement_label(tab, "Оптимальное значение переменных", 5, 1, 5, 1, 3, 5)

    generatics_btn = ttk.Button(tab, text='Вызвать генетический', command=lambda: call_geneticsAlgorithm(textField_populationSize,textField_numGeneratics,lab_optimalFunc,lab_optimalValuePoints))
    generatics_btn.grid(row=6, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

    global textReachGeneraticPoints
    textReachGeneraticPoints = ScrolledText(tab, height=10, width=30)
    textReachGeneraticPoints.grid(row=7, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

def createTab_Swarm(tab):
    tf_swarm = []

    createLabel.placement_label(tab, "Размер Роя", 0, 0, 5, 1, 1, 5)
    tF = ttk.Entry(tab)
    tF.insert(0, "50")
    tF.grid(row=0, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf_swarm.append(tF)

    createLabel.placement_label(tab, "Общий масштабирующий\n коэффициент для скорости", 1, 0, 5, 1, 1, 5)
    tF = ttk.Entry(tab)
    tF.insert(0, "0.1")
    tF.grid(row=1, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf_swarm.append(tF)

    createLabel.placement_label(tab, "Коэффициент, задающий влияние лучшей точки,\n найденной каждой частицей,\n на будущую скорость", 2, 0, 5, 1, 1, 5)
    tF = ttk.Entry(tab)
    tF.insert(0, "1")
    tF.grid(row=2, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf_swarm.append(tF)

    createLabel.placement_label(tab, "Коэффициент, задающий влияние лучшей точки,\n найденной всеми частицами,\n на будущую скорость", 3, 0, 5, 1, 1, 5)
    tF = ttk.Entry(tab)
    tF.insert(0, "5")
    tF.grid(row=3, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf_swarm.append(tF)

    createLabel.placement_label(tab, "Количество жизней", 4, 0, 5, 1, 1, 5)
    tF = ttk.Entry(tab)
    tF.insert(0, "100")
    tF.grid(row=4, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf_swarm.append(tF)

    #createLabel.placement_label(tab, "Start", 5, 0, 5, 1, 1, 5)
   # createLabel.placement_label(tab, "End", 5, 1, 5, 1, 1, 5)
   # tF = ttk.Entry(tab)
   # tF.insert(0, "-5")
   # tF.grid(row=6, column=0, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
   # tf_swarm.append(tF)

   # tF = ttk.Entry(tab)
   # tF.insert(0, "5")
   # tF.grid(row=6, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
  #  tf_swarm.append(tF)

    btn = ttk.Button(tab, text='Вызвать рой',command=lambda: call_Swarm(tf_swarm))
    btn.grid(row=5, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

    global textReachSwarm
    textReachSwarm = ScrolledText(tab, height=10, width=30)
    textReachSwarm.grid(row=6, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

def createTab_Bees(tab):
    tf_bees = []

    createLabel.placement_label(tab, "Мин х", 0, 0, 5, 1, 1, 5)
    tF = ttk.Entry(tab)
    tF.insert(0, "-10")
    tF.grid(row=0, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf_bees.append(tF)

    createLabel.placement_label(tab, "Макс х", 1, 0, 5, 1, 1, 5)
    tF = ttk.Entry(tab)
    tF.insert(0, "10")
    tF.grid(row=1, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf_bees.append(tF)

    createLabel.placement_label(tab, "Мин у", 2, 0, 5, 1, 1, 5)
    tF = ttk.Entry(tab)
    tF.insert(0, "-10")
    tF.grid(row=2, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf_bees.append(tF)

    createLabel.placement_label(tab, "Макс у", 3, 0, 5, 1, 1, 5)
    tF = ttk.Entry(tab)
    tF.insert(0, "10")
    tF.grid(row=3, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf_bees.append(tF)

    createLabel.placement_label(tab, "Количество пчелок", 4, 0, 5, 1, 1, 5)
    tF = ttk.Entry(tab)
    tF.insert(0, "200")
    tF.grid(row=4, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf_bees.append(tF)

    createLabel.placement_label(tab, "Время(мс)", 5, 0, 5, 1, 1, 5)
    tF = ttk.Entry(tab)
    tF.insert(0, "100")
    tF.grid(row=5, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf_bees.append(tF)


    btn = ttk.Button(tab, text='Вызвать пчелок',command=lambda: call_Bees(tf_bees))
    btn.grid(row=6, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

    global textReachBees
    textReachBees = ScrolledText(tab, height=10, width=30)
    textReachBees.grid(row=7, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

if __name__ == '__main__':
    global STEP
    root = tk.Tk()
    root.title("Matplotlib with Windows Form 3D")

    notebook = ttk.Notebook(root)

    canvas_3d = FigureCanvasTkAgg(fig_3d, master=root)
    canvas_3d_widget = canvas_3d.get_tk_widget()

    frame1 = ttk.Frame(notebook)
    frame2 = ttk.Frame(notebook)
    frame3 = ttk.Frame(notebook)
    frame4 = ttk.Frame(notebook)
    frame5 = ttk.Frame(notebook)

    notebook.add(frame1, text="Градиент")
    notebook.add(frame2,text="Квадратичная ф-я")
    notebook.add(frame3, text="Генетический")
    notebook.add(frame4, text="Рой")
    notebook.add(frame5, text="Пчелки")

    createTab_gradient(frame1)
    createTab_simpleMethod(frame2)
    createTab_Genetic(frame3)
    createTab_Swarm(frame4)
    createTab_Bees(frame5)

    createLabel.placement_label(root, "Шаг(епсилон)", 1, 1, 5, 1, 3, 5)
    textFieldStep = ttk.Entry(root)
    textFieldStep.insert(0, str(STEP))

    lab_func = createLabel.placement_label(root, "Выбор базовой функции", 3, 1, 5, 1, 3, 5)
    comboBoxFunc = ttk.Combobox(root, values=[
        "Квадратная",
        "Синусоида",
        "Билла",
        "Бута",
        "Букина",
        "Эгхолдера",
        "Квадратичная",
        "Розенброк",
        "Рома",
        "Растригина",
        "Химмельблау"],
                                state="readonly")
    comboBoxFunc.bind("<<ComboboxSelected>>", lambda event, cb=comboBoxFunc,lab = lab_func,field=textFieldStep: selectFunc(event, cb,lab,field))

    canvas_3d_widget.grid(row=0, column=0, rowspan=20, padx=5, pady=5) #matplotlib
    notebook.grid(row=0,column=1,padx=5,pady=5,rowspan=1,columnspan=3,sticky="nsew")

    comboBoxFunc.grid(row=4,column=1,padx=5,pady=5,rowspan=1,columnspan=3,sticky="nsew")
    textFieldStep.grid(row=2, column=1,padx=5, pady=5,rowspan=1,columnspan=3,sticky="nsew")


    clear_btn = ttk.Button(root, text="Очистить точки с графика", command=clearPoints)
    clear_btn.grid(row=8, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")
    save_button = ttk.Button(root, text="Сохранить график", command=save_plot)

    save_button.grid(row=9, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")
    close_button = ttk.Button(root, text="Закрыть приложение", command=close_application)
    close_button.grid(row=10, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")


    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(12, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(3, weight=1)

    root.mainloop()