from tkinter import messagebox
from backend.algorithmBacterial import algorithm_is_bacterial
from Lab2.backend.helper import getMatrixFromMatrixList
from Lab2.backend.helper_predicat import isNotEmptyFields,isNotOutGraphic

import global_variable as gv
import frontshow.animation as anim
import outer_imports.matplotlib  as omatpl
import Lab2.frontshow.Color as colors

def call_Bacterial(arr_textField) -> None:
    try:
        if (len(gv.x_data) > 0 and len(gv.y_data) > 0 and isNotEmptyFields(arr_textField)):
            min_x = float(arr_textField[0].get())
            max_x = float(arr_textField[1].get())
            min_y = float(arr_textField[2].get())
            max_y = float(arr_textField[3].get())
            if isNotOutGraphic(gv.START,gv.END,min_x, max_x, min_y, max_y):
                count_bacterials = int(arr_textField[4].get())
                time = int(arr_textField[5].get())
                points,bestPoint  = algorithm_is_bacterial(min_x, max_x, min_y, max_y, count_bacterials, gv.current_function, time,gv.STEP)
                bestResult = [bestPoint[0], bestPoint[1], bestPoint[2], colors.Color.CYAN.value, "o", 70]
                points = getMatrixFromMatrixList(points)

                _ = omatpl.FuncAnimation(omatpl.fig_3d, anim.animate, frames=len(points), fargs=(points, bestResult, gv.textReachBacterial, 'o',),interval=gv.SPEED, repeat=False)

                gv.canvas_3d.draw()
            else:
                messagebox.showerror("Error", f"Invalid data. Out of graphics: [{gv.START};{gv.END}]")
        else:
            print(f"size x = {len(gv.x_data)}")
            print(f"size y = {len(gv.y_data)}")
            messagebox.showerror("Error",
                                 "Invalid data. Fill defualt data and inputs: min_x,max_y,min_y,max_y,time,count bees")
    except ValueError:
        messagebox.showerror("Error", "Invalid fillMatrix. Check bacterial algorithm")