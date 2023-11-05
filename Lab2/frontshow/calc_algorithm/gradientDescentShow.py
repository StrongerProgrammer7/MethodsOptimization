import random
from tkinter import messagebox

from backend.gradient_descent import gradient_descent
from backend.helper import getMatrixFromList
import global_variable as gv
import frontshow.animation as anim
import outer_imports.matplotlib  as omatpl

def callGradient_DrawPoint(textFieldCountIter) -> None:
    try:
        if(len(gv.x_data) > 0 and len(gv.y_data) > 0 and int(textFieldCountIter.get()) > 10):
            points = gradient_descent(gv.current_function, random.choice(gv.x_data), random.choice(gv.y_data), gv.STEP/10, int(textFieldCountIter.get()))
            points = getMatrixFromList(list(points))
            ani = omatpl.FuncAnimation(omatpl.fig_3d, anim.animate, frames=len(points), fargs=(points, None,gv.textReachGradientPoint,'o',), interval=gv.SPEED,
                                repeat=False)
            gv.canvas_3d.draw()
        else:
            print(len(gv.x_data))
            print(len(gv.y_data))
            print(int(textFieldCountIter.get()))
            messagebox.showerror("Error", "Invalid data. Fill defualt data and count iter.")
    except ValueError:
        messagebox.showerror("Error", "Invalid fillMatrix. Please check fill matrix and gradient_descent")