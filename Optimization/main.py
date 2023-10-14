
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
    for x, y, countIter, f in resultFunction:
        temp.append([x, y, f])
    return temp

def getMatrixFromGenetics(result):
    temp = []
    for x,y in result:
        z = current_function(x,y)
        temp.append([x,y,z])
    return temp


def isNotZeroPoints(arr,frame):
    return abs(round(arr[frame][0])) != 0 and abs(round(arr[frame][1])) != 0 and abs(round(arr[frame][2])) !=0

def animate(frame, arr, textReach=None, marker=None):
    if len(arr) > frame:
        size_point = SIZE_POINT
        color = Color.GREEN.value
        if (len(arr) - 1 == frame):
            color = Color.RED.value
            size_point = 100
        if (textReach != None):
            str_temp = "# " + str(frame) + " X=" + str(round(arr[frame][0], 4)) + " Y=" + str(round(arr[frame][1],4 )) + " Z=" + str(round(arr[frame][2], 4)) + "\n"
            textReach.insert(1.0, str_temp)
            scatter_points.append(ax_3d.scatter(arr[frame][0], arr[frame][1], arr[frame][2], c=color, marker=marker, s=size_point))


def callGradient_DrawPoint(textFieldCountIter) -> None:
    try:
        if(len(x_data) > 0 and len(y_data) > 0 and int(textFieldCountIter.get()) > 10):
            temp = fillMatrix(list(gradient_descent(current_function, random.choice(x_data), random.choice(y_data), 0.1, int(textFieldCountIter.get()))))
            ani = FuncAnimation(fig_3d, animate, frames=len(temp), fargs=(temp, textReachGradientPoint,'o',), interval=SPEED,
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
        if(len(x_data) > 0 and len(y_data) > 0):
            temp = get_points(max(x_data),max(y_data),current_function)
            ani = FuncAnimation(fig_3d, animate, frames=len(temp), fargs=(temp, textReachQuadPoint,'x',), interval=SPEED, repeat=False)
            canvas_3d.draw()
        else:
            print(len(x_data))
            print(len(y_data))
            messagebox.showerror("Error", "Invalid data. Fill defualt data")
    except ValueError:
        messagebox.showerror("Error", "Invalid fillMatrix. Please check fill matrix and simplex_method")

def isNotEmptyFields(arrFields):
    for i in arrFields:
        if int(i.get()) < 10:
            return False
    return True

def call_geneticsAlgorithm(tf_populationSize,tf_numGeneratics,lab_optimalFunc,lab_optimalValuePoints) -> None:
    try:
        if(len(x_data) > 0 and len(y_data) > 0 and isNotEmptyFields([tf_populationSize,tf_numGeneratics])):
            population_size,num_generations = int(tf_populationSize.get()),int(tf_numGeneratics.get())
            best_solution, best_fitness,arr_points = genetic_algorithm(population_size, num_generations,current_function)
            lab_optimalValuePoints.configure(text="Оптимальное значение функции: " + str(round(best_fitness,3)))
            lab_optimalFunc.configure(text="Оптимальное значение переменных: " + str(round(best_solution[0])) + " : " + str(round(best_solution[1])))

            points = getMatrixFromGenetics(arr_points)
            ani = FuncAnimation(fig_3d, animate, frames=len(points), fargs=(points, textReachGeneraticPoints,'v',), interval=SPEED, repeat=False)
            canvas_3d.draw()
        else:
            print(len(x_data))
            print(len(y_data))
            messagebox.showerror("Error", "Invalid data. Fill defualt data and inputs: population size and count generatics")
    except ValueError:
        messagebox.showerror("Error", "Invalid fillMatrix. Please check fill matrix and genetric algorithm")


def save_plot():
    try:
        # Save the 3D plot to a file
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            fig_3d.savefig(file_path)
            messagebox.showinfo("Success", "Plot saved successfully.")

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
        x_data = np.arange(START, END, STEP)
        y_data = np.arange(START, END, STEP)

    X, Y = np.meshgrid(x_data, y_data)
    Z = current_function(X, Y)

    ax_3d.plot_surface(X, Y, Z, cmap=ColorFigure.VIRIDIS.value,alpha=0.7, antialiased=True,rstride=1, cstride=1)
    canvas_3d.draw()

def clearPoints():
    for i in scatter_points:
        i.remove()
    textReachGradientPoint.delete(1.0,tk.END)
    textReachQuadPoint.delete(1.0, tk.END)
    textReachGeneraticPoints.delete(1.0,tk.END)
    canvas_3d.draw()
    scatter_points.clear()

def selectFunc(event,combo,lab,textField):
    try:
        global STEP,START,END,current_function
        if len(textField.get()) > 0 and textField.get()!='' and float(textField.get())!=0:
            selection = combo.get()
            STEP = float(textField.get())
            if selection in chooseFunc:
                current_function = chooseFunc[selection]['f']
            if selection == "Bukina":
                START = chooseFunc[selection]['x']
                END = chooseFunc[selection]['y']
            else:
                START = chooseFunc[selection]['from']
                END = chooseFunc[selection]['to']
            buildBaseFunction()
            lab.config(text="Function:" + selection)
        else:
            messagebox.showerror("Error", "Invalid input. Please enter numeric values step.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

def createTab_gradient(tab):
    createLabel.placement_label(tab, "Choose count iteration for gradient", 0, 1, 5, 1, 3, 5)
    textFieldCountIter = ttk.Entry(tab)
    textFieldCountIter.insert(0, "500")

    findMinGradientDescent_button = ttk.Button(tab, text="Call gradient Descent",
                                               command=lambda: callGradient_DrawPoint(textFieldCountIter))
    textFieldCountIter.grid(row=1, column=1, padx=5, pady=5, rowspan=1, columnspan=3, sticky="nsew")
    findMinGradientDescent_button.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

    global textReachGradientPoint
    textReachGradientPoint = ScrolledText(tab, height=10, width=30)
    textReachGradientPoint.grid(row=3,column=1, columnspan=3, padx=5, pady=5, sticky="nsew")


def createTab_simpleMethod(tab):
    findQud_btn = ttk.Button(tab, text='Call simplex method', command=lambda: call_simplex_method())
    findQud_btn.grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")
    global textReachQuadPoint
    textReachQuadPoint = ScrolledText(tab, height=10, width=30)
    textReachQuadPoint.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

def createTab_Genetic(tab):
    createLabel.placement_label(tab, "Population size", 0, 1, 5, 1, 3, 5)
    textField_populationSize = ttk.Entry(tab)
    textField_populationSize.insert(0, "50")

    createLabel.placement_label(tab, "Count generatic", 2, 1, 5, 1, 3, 5)
    textField_numGeneratics= ttk.Entry(tab)
    textField_numGeneratics.insert(0, "100")

    textField_populationSize.grid(row=1, column=1, padx=5, pady=5, rowspan=1, columnspan=3, sticky="nsew")
    textField_numGeneratics.grid(row=3, column=1, padx=5, pady=5, rowspan=1, columnspan=3, sticky="nsew")

    lab_optimalFunc = createLabel.placement_label(tab, "Оптимальное значение функции: ", 4, 1, 5, 1, 3, 5)
    lab_optimalValuePoints = createLabel.placement_label(tab, "Оптимальное значение переменных", 5, 1, 5, 1, 3, 5)

    generatics_btn = ttk.Button(tab, text='Call genetics', command=lambda: call_geneticsAlgorithm(textField_populationSize,textField_numGeneratics,lab_optimalFunc,lab_optimalValuePoints))
    generatics_btn.grid(row=6, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

    global textReachGeneraticPoints
    textReachGeneraticPoints = ScrolledText(tab, height=10, width=30)
    textReachGeneraticPoints.grid(row=7, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")




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

    notebook.add(frame1, text="Gradient")
    notebook.add(frame2,text="Simplex method")
    notebook.add(frame3, text="Genetic")

    createTab_gradient(frame1)
    createTab_simpleMethod(frame2)
    createTab_Genetic(frame3)
    createLabel.placement_label(root, "Choose Step", 1, 1, 5, 1, 3, 5)
    textFieldStep = ttk.Entry(root)
    textFieldStep.insert(0, str(STEP))

    lab_func = createLabel.placement_label(root, "Choose function", 3, 1, 5, 1, 3, 5)
    comboBoxFunc = ttk.Combobox(root, values=["function_1", "function_2", "Bila", "Buta", "Bukina", "Eggholder","quadratic","rosenbrock"],
                                state="readonly")
    comboBoxFunc.bind("<<ComboboxSelected>>", lambda event, cb=comboBoxFunc,lab = lab_func,field=textFieldStep: selectFunc(event, cb,lab,field))

    canvas_3d_widget.grid(row=0, column=0, rowspan=20, padx=5, pady=5) #matplotlib
    notebook.grid(row=0,column=1,padx=5,pady=5,rowspan=1,columnspan=3,sticky="nsew")

    comboBoxFunc.grid(row=4,column=1,padx=5,pady=5,rowspan=1,columnspan=3,sticky="nsew")
    textFieldStep.grid(row=2, column=1,padx=5, pady=5,rowspan=1,columnspan=3,sticky="nsew")


    clear_btn = ttk.Button(root, text="Clear points", command=clearPoints)
    clear_btn.grid(row=8, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")
    save_button = ttk.Button(root, text="Save Schedule", command=save_plot)

    save_button.grid(row=9, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")
    close_button = ttk.Button(root, text="Close Application", command=close_application)
    close_button.grid(row=10, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")


    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(12, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(3, weight=1)

    root.mainloop()