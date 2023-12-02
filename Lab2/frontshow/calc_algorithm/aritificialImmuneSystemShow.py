from tkinter import messagebox

from backend.algorithmArtificialImmuneSystem import algorithm_artificial_immune_system
from backend.helper import getMatrixFromList
from backend.helper_predicat import isNotEmptyFields, isNotOutGraphic, isNotOutGraphicDict

import global_variable as gv
import frontshow.animation as anim
import outer_imports.matplotlib  as omatpl
import frontshow.Color as colors

def call_AIimmuneSystem(arr_textField) -> None:
    try:
        if(len(gv.x_data) > 0 and len(gv.y_data) > 0 and isNotEmptyFields(arr_textField)):
            min_x = float(arr_textField[0].get())
            max_x = float(arr_textField[1].get())
            min_y = float(arr_textField[2].get())
            max_y = float(arr_textField[3].get())
            isNotOutBounds = False
            if (type(gv.START) == dict):
                isNotOutBounds = isNotOutGraphicDict(gv.START, gv.END, min_x, max_x, min_y, max_y)
            else:
                isNotOutBounds = isNotOutGraphic(gv.START, gv.END, min_x, max_x, min_y, max_y)

            if isNotOutBounds:
                sizePopulize = int(arr_textField[4].get())
                countGenerations = int(arr_textField[5].get())
                best_point, points = algorithm_artificial_immune_system(min_x, max_x, min_y, max_y, sizePopulize, gv.current_function, countGenerations)
                bestResult = [best_point[0], best_point[1], best_point[2], colors.Color.CYAN.value, "o", 50]
                points = getMatrixFromList(points)
                _ = omatpl.FuncAnimation(omatpl.fig_3d, anim.animate, frames=len(points), fargs=(points, bestResult, gv.textReachImmuneSystem, 'o',),interval=gv.SPEED, repeat=False)

                gv.canvas_3d.draw()
            else:
                messagebox.showerror("Error",f'Invalid data. Out of graphics: [{gv.START};{gv.END}]')
        else:
            print(f"size x = {len(gv.x_data)}")
            print(f"size y = {len(gv.y_data)}")
            messagebox.showerror("Error", "Invalid data. Fill defualt data and inputs: min_x,max_y,min_y,max_y,time,count bees")
    except ValueError:
        messagebox.showerror("Error", "Invalid fillMatrix. Check immune system algorithm")