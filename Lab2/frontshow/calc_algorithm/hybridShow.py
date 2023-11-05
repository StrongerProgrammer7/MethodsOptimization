from tkinter import messagebox

from backend.hybrid.hybrid import hybrid
from backend.helper_predicat import isNotEmptyFields
import global_variable as gv
import frontshow.animation as anim
import outer_imports.matplotlib  as omatpl
import frontshow.Color as colors

from Lab2.backend.helper import getMatrixFromMatrixList


def call_hybridAlgorithm(tf_populationSize,tf_numGeneratics,lab_optimalFunc,lab_optimalValuePoints) -> None:
    try:
        if(len(gv.x_data) > 0 and len(gv.y_data) > 0 and isNotEmptyFields([tf_populationSize,tf_numGeneratics])):
            population_size,num_generations = int(tf_populationSize.get()),int(tf_numGeneratics.get())
            if (type(gv.START) == dict):
                min_x, max_x, min_y, max_y = gv.START[1], gv.START[2], gv.END[1], gv.END[2]
                best_solution, points = hybrid(min_x, max_x, min_y, max_y, population_size,
                                                                        num_generations, gv.current_function)
            else:
                best_solution, points = hybrid(gv.START, gv.END, gv.START, gv.END,
                                                                        population_size,
                                                                        num_generations, gv.current_function)
            lab_optimalValuePoints.configure(text="Оптимальное значение функции: " + str(round(best_solution[2],3)))
            lab_optimalFunc.configure(text="Оптимальное значение переменных: " + str(round(best_solution[0])) + " : " + str(round(best_solution[1])))

            bestResult = [best_solution[0], best_solution[1], best_solution[2],colors.Color.WHITE.value,"o",70]
            points = getMatrixFromMatrixList(points)
            _ = omatpl.FuncAnimation(omatpl.fig_3d, anim.animate, frames=len(points), fargs=(points, bestResult, gv.textReachHybrid, 'o',), interval=gv.SPEED, repeat=False)
            gv.canvas_3d.draw()
        else:
            print(len(gv.x_data))
            print(len(gv.y_data))
            messagebox.showerror("Error", "Invalid data. Fill defualt data and inputs: population size and count generatics")
    except ValueError:
        messagebox.showerror("Error", "Invalid fillMatrix. Please check fill matrix and hybrid algorithm")