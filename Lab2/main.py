import random

from outer_imports.imports_tkinter import *
from outer_imports.matplotlib import *

from backend.gradient_descent import gradient_descent
from backend.simplexMethod import get_points
from backend.geneticsAlgorithm import genetic_algorithm
from backend.Swarm_X2 import Swarm
from backend.algorithm_of_bees import algorithm_of_bees
from backend.algorithmBacterial import algorithm_is_bacterial

from backend.helper_predicat import *
from backend.helper import *

from global_variable import *
from frontshow.Color import *
from frontshow.placement_elements import (createLabel,
                                          createTab_gradient,createTab_simpleMethod,
                                          createTab_Genetic,createTab_Swarm,
                                          createTab_Bees,createTab_Bacterial)
from frontshow.methods import save_plot,close_application


from setFunction import *


def animate(frame, arr,best_result=None, textReach=None, marker=None):
    if len(arr) > frame:
        size_point = SIZE_POINT
        color = Color.GREEN.value
        if (len(arr) - 1 == frame):
            color = Color.RED.value
            size_point = 50
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


def callGradient_DrawPoint(textFieldCountIter) -> None:
    try:
        if(len(x_data) > 0 and len(y_data) > 0 and int(textFieldCountIter.get()) > 10):
            points = gradient_descent(current_function, random.choice(x_data), random.choice(y_data), STEP/10, int(textFieldCountIter.get()))
            points = getMatrixFromList(list(points))
            ani = FuncAnimation(fig_3d, animate, frames=len(points), fargs=(points, None,textReachGradientPoint,'o',), interval=SPEED,
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
            points = get_points(max(x_data),max(y_data),current_function)
            ani = FuncAnimation(fig_3d, animate, frames=len(points), fargs=(points, None,textReachQuadPoint,'x',), interval=SPEED, repeat=False)
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
            best_solution, best_fitness,points = genetic_algorithm(population_size, num_generations,current_function)

            lab_optimalValuePoints.configure(text="Оптимальное значение функции: " + str(round(best_fitness,3)))
            lab_optimalFunc.configure(text="Оптимальное значение переменных: " + str(round(best_solution[0])) + " : " + str(round(best_solution[1])))

            bestResult = [best_solution[0], best_solution[1], best_fitness,Color.YELLOW.value,"o",70]

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
            #(globLocalVelociryRatio)
            numOfLife = int(arr_textField[4].get())

            a = Swarm(sizeSwarm, curLocalVelociryRatio, locLocalVelociryRatio, globLocalVelociryRatio, numOfLife, current_function, START, END)
            points = a.startSwarm()
            #print("РЕЗУЛЬТАТ:", a.globalBestScore, "В ТОЧКЕ:", a.globalBestPos)

           # bestPointSet.append(ax_3d.scatter(a.globalBestPos[0], a.globalBestPos[1], a.globalBestScore, c=Color.BLUE.value, marker="o", s=250))
            bestResult = [a.globalBestPos[0],a.globalBestPos[1],a.globalBestScore,Color.BLUE.value, "o",70]
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
            min_x = float(arr_textField[0].get())
            max_x = float(arr_textField[1].get())
            min_y = float(arr_textField[2].get())
            max_y = float(arr_textField[3].get())
            if isNotOutGraphic(START,END,min_x,max_x,min_y,max_y):
                numBees = int(arr_textField[4].get())
                time = int(arr_textField[5].get())
                rezusl, points = algorithm_of_bees(min_x, max_x, min_y, max_y, numBees, current_function, time)
                bestResult = [rezusl[0][0], rezusl[0][1], rezusl[1], Color.CYAN.value, "o", 70]

                _ = FuncAnimation(fig_3d, animate, frames=len(points), fargs=(points, bestResult, textReachBees, 'o',),interval=SPEED, repeat=False)

                canvas_3d.draw()
            else:
                messagebox.showerror("Error",f'Invalid data. Out of graphics: [{START};{END}]')
        else:
            print(f"size x = {len(x_data)}")
            print(f"size y = {len(y_data)}")
            messagebox.showerror("Error", "Invalid data. Fill defualt data and inputs: min_x,max_y,min_y,max_y,time,count bees")
    except ValueError:
        messagebox.showerror("Error", "Invalid fillMatrix. Check bees algorithm")

def call_Bacterial(arr_textField) -> None:
    try:
        if (len(x_data) > 0 and len(y_data) > 0 and isNotEmptyFields(arr_textField)):
            min_x = float(arr_textField[0].get())
            max_x = float(arr_textField[1].get())
            min_y = float(arr_textField[2].get())
            max_y = float(arr_textField[3].get())
            if isNotOutGraphic(START,END,min_x, max_x, min_y, max_y):
                count_bacterials = int(arr_textField[4].get())
                time = int(arr_textField[5].get())
                points,bestPoint  = algorithm_is_bacterial(min_x, max_x, min_y, max_y, count_bacterials, current_function, time,STEP)
                bestResult = [bestPoint[0], bestPoint[1], bestPoint[2], Color.CYAN.value, "o", 70]
                points = getMatrixFromMatrixList(points)

                _ = FuncAnimation(fig_3d, animate, frames=len(points), fargs=(points, bestResult, textReachBacterial, 'o',),interval=SPEED, repeat=False)

                canvas_3d.draw()
            else:
                messagebox.showerror("Error", f"Invalid data. Out of graphics: [{START};{END}]")
        else:
            print(f"size x = {len(x_data)}")
            print(f"size y = {len(y_data)}")
            messagebox.showerror("Error",
                                 "Invalid data. Fill defualt data and inputs: min_x,max_y,min_y,max_y,time,count bees")
    except ValueError:
        messagebox.showerror("Error", "Invalid fillMatrix. Check bacterial algorithm")


def buildBaseFunction():
    ax_3d.clear()

    ax_3d.set_title("3D Matplotlib Plot")
    ax_3d.set_xlabel("X-axis")
    ax_3d.set_ylabel("Y-axis")
    ax_3d.set_zlabel("Z-axis")
    global x_data
    global y_data
    global z_data
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

    ax_3d.plot_surface(X, Y, Z, cmap=ColorFigure.INFERNO.value,alpha=0.7, antialiased=True,rstride=1, cstride=1)
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
    textReachBees.delete(1.0,tk.END)
    textReachBacterial.delete(1.0,tk.END)
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
    frame6 = ttk.Frame(notebook)

    notebook.add(frame1, text="Градиент")
    notebook.add(frame2,text="Квадратичная ф-я")
    notebook.add(frame3, text="Генетический")
    notebook.add(frame4, text="Рой")
    notebook.add(frame5, text="Пчелки")
    notebook.add(frame6, text="Бактерии")

    global textReachGradientPoint,textReachQuadPoint,textReachSwarm,textReachBees,textReachGeneraticPoints,textReachBacterial
    textReachGradientPoint = createTab_gradient(frame1,callGradient_DrawPoint,ttk)
    textReachQuadPoint = createTab_simpleMethod(frame2,call_simplex_method,ttk)
    textReachGeneraticPoints = createTab_Genetic(frame3,call_geneticsAlgorithm,ttk)
    textReachSwarm = createTab_Swarm(frame4,call_Swarm,ttk)
    textReachBees = createTab_Bees(frame5,call_Bees,ttk)
    textReachBacterial = createTab_Bacterial(frame6,call_Bacterial,ttk)

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
        "Химмельблау"],state="readonly")
    comboBoxFunc.bind("<<ComboboxSelected>>", lambda event, cb=comboBoxFunc,lab = lab_func,field=textFieldStep: selectFunc(event, cb,lab,field))

    canvas_3d_widget.grid(row=0, column=0, rowspan=20, padx=5, pady=5) #matplotlib
    notebook.grid(row=0,column=1,padx=5,pady=5,rowspan=1,columnspan=3,sticky="nsew")

    comboBoxFunc.grid(row=4,column=1,padx=5,pady=5,rowspan=1,columnspan=3,sticky="nsew")
    textFieldStep.grid(row=2, column=1,padx=5, pady=5,rowspan=1,columnspan=3,sticky="nsew")


    clear_btn = ttk.Button(root, text="Очистить точки с графика", command=clearPoints)
    clear_btn.grid(row=8, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")
    save_button = ttk.Button(root, text="Сохранить график", command=save_plot)

    save_button.grid(row=9, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")
    close_button = ttk.Button(root, text="Закрыть приложение",  command=lambda: close_application(root))
    close_button.grid(row=10, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")


    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(12, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(3, weight=1)

    root.mainloop()