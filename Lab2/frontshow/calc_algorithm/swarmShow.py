from tkinter import messagebox

from backend.Swarm_X2 import Swarm
from backend.helper import deleteDuplicateValue
from backend.helper_predicat import isNotEmptyFields

import global_variable as gv
import frontshow.animation as anim
import outer_imports.matplotlib  as omatpl
import frontshow.Color as colors

def call_Swarm(arr_textField) -> None:
    try:
        if(len(gv.x_data) > 0 and len(gv.y_data) > 0 and isNotEmptyFields(arr_textField)):
            sizeSwarm = int(arr_textField[0].get())
            curLocalVelociryRatio = float(arr_textField[1].get())
            locLocalVelociryRatio = float(arr_textField[2].get())
            globLocalVelociryRatio = float(arr_textField[3].get())
            #(globLocalVelociryRatio)
            numOfLife = int(arr_textField[4].get())

            a = Swarm(sizeSwarm, curLocalVelociryRatio, locLocalVelociryRatio, globLocalVelociryRatio, numOfLife, gv.current_function, gv.START, gv.END)
            points = a.startSwarm()
            #print("РЕЗУЛЬТАТ:", a.globalBestScore, "В ТОЧКЕ:", a.globalBestPos)

           # bestPointSet.append(ax_3d.scatter(a.globalBestPos[0], a.globalBestPos[1], a.globalBestScore, c=Color.BLUE.value, marker="o", s=250))
            bestResult = [a.globalBestPos[0],a.globalBestPos[1],a.globalBestScore,colors.Color.BLUE.value, "o",50]
            points = deleteDuplicateValue(points)
            _ = omatpl.FuncAnimation(omatpl.fig_3d, anim.animate, frames=len(points), fargs=(points,bestResult, gv.textReachSwarm,'x',), interval=gv.SPEED, repeat=False)
            gv.canvas_3d.draw()
        else:
            print(f"size x = {len(gv.x_data)}")
            print(f"size y = {len(gv.y_data)}")
            messagebox.showerror("Error", "Invalid data. Fill defualt data and inputs: size,lifes,velocity")
    except ValueError:
        messagebox.showerror("Error", "Invalid fillMatrix. Check swarm algorithm")