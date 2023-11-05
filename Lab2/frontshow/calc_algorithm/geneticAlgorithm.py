from tkinter import messagebox

from backend.geneticsAlgorithm import genetic_algorithm
from backend.helper_predicat import isNotEmptyFields
import global_variable as gv
import frontshow.animation as anim
import outer_imports.matplotlib  as omatpl
import frontshow.Color as colors

def call_geneticsAlgorithm(tf_populationSize,tf_numGeneratics,lab_optimalFunc,lab_optimalValuePoints) -> None:
    try:
        if(len(gv.x_data) > 0 and len(gv.y_data) > 0 and isNotEmptyFields([tf_populationSize,tf_numGeneratics])):
            population_size,num_generations = int(tf_populationSize.get()),int(tf_numGeneratics.get())
            best_solution, best_fitness,points = genetic_algorithm(population_size, num_generations,gv.current_function)

            lab_optimalValuePoints.configure(text="Оптимальное значение функции: " + str(round(best_fitness,3)))
            lab_optimalFunc.configure(text="Оптимальное значение переменных: " + str(round(best_solution[0])) + " : " + str(round(best_solution[1])))

            bestResult = [best_solution[0], best_solution[1], best_fitness,colors.Color.YELLOW.value,"o",70]

            _ = omatpl.FuncAnimation(omatpl.fig_3d, anim.animate, frames=len(points), fargs=(points,bestResult, gv.textReachGeneraticPoints,'v',), interval=gv.SPEED, repeat=False)
            gv.canvas_3d.draw()
        else:
            print(len(gv.x_data))
            print(len(gv.y_data))
            messagebox.showerror("Error", "Invalid data. Fill defualt data and inputs: population size and count generatics")
    except ValueError:
        messagebox.showerror("Error", "Invalid fillMatrix. Please check fill matrix and genetric algorithm")