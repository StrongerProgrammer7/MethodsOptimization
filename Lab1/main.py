import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits import mplot3d  # for 3D
from matplotlib.animation import FuncAnimation

import numpy as np
from enum import Enum
import random
from gradient_descent import gradient_descent
from setFunction import *
from frontshow.placement_elements import createLabel
# ax.scatter(x_data,y_data,z_data,marker="v",alpha=0.1)

#
# X,Y = np.meshgrid(x_data,y_data)
# Z = np.sin(X) * np.cos(Y)
#
# ax.plot_surface(X,Y,Z,cmap="plasma")
# ax.view_init(azim=0,elev=90)

fig_3d = plt.figure()
ax_3d = fig_3d.add_subplot(111, projection="3d")
START = -5
END = 5
STEP = 0.6
SPEED = 100
SIZE_POINT = 50


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    CYAN = "cyan"
    YELLOW = "yellow"
    PINK = "pink"
    BLACK = "black"
    WHITE = "white"
    GRAY = "gray"
class ColorFigure(Enum):
    PLASMA = "plasma"
    VIRIDIS = "viridis"
    INFERNO = "inferno"
    MAGMA = "magma"
    CIVIDIS = "cividis"
    BINARY = "binary"
    SPRINT = "sprint"
    SUMMER = "summer"
    WINTER = "winter"
    AUTUMN = "autumn"
    BONE = "bone"


x_data = []
y_data = []

scatter_points = []

def fillMatrix(resultGradient):
    temp = []
    for x, y, countIter, f in resultGradient:
        if(countIter % 2 == 0):
            temp.append([x, y, f - 5]) # -5 for better show
    return temp

def animate(frame, arr, arr2):
    if len(arr) > frame:
        scatter_points.append(ax_3d.scatter(arr[frame][0], arr[frame][1], arr[frame][2], c=Color.GREEN.value, marker='o', s=SIZE_POINT))
    if len(arr2) > frame:
        scatter_points.append(ax_3d.scatter(arr2[frame][0], arr2[frame][1], arr2[frame][2], c=Color.RED.value, marker='o', s=SIZE_POINT))

def callGradient_DrawPoint() -> None:
    try:
        if(len(x_data) > 0 and len(y_data) > 0):
            # Moment draw 2 min
            temp = fillMatrix(list(gradient_descent(function_1, random.choice(x_data), random.choice(y_data), 0.1, 500)))
            temp2 = fillMatrix(list(gradient_descent(function_1, random.choice(x_data), random.choice(y_data), 0.1, 500)))

            ani = FuncAnimation(fig_3d, animate, frames=max(len(temp), len(temp2)), fargs=(temp, temp2,), interval=SPEED,
                            repeat=False)
            canvas_3d.draw()
        else:
            messagebox.showerror("Error", "Invalid data. Fill defualt data.")
    except ValueError:
        messagebox.showerror("Error", "Invalid fillMatrix. Please check fill matrix and gradient_descent")

def setBaseData():
    try:
        global START
        global END
        global STEP
        global x_data
        global y_data
        if len(entry_end.get()) > 0 and len(entry_start.get()) and len(entry_step.get()):
            START = float(entry_start.get())
            END = float(entry_end.get())
            STEP = float(entry_step.get())
            x_data = np.arange(START, END, STEP)
            y_data = np.arange(START, END, STEP)
        else:
            messagebox.showerror("Error", "Invalid input. Not enought values")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

'''
def update_plot() -> None:
    try:
        global temp_input_x
        global temp_input_y
        # x = float(entry_x.get())
        # y = float(entry_y.get())
        input_x = entry_x.get()
        input_y = entry_y.get()
        points = [float(point) for point in input_x.split()]
        if True == True:  # checkPointSimple(input_x,input_y)== True:
            temp_input_x = input_x
            temp_input_y = input_y
            # entry_x.delete(0,'end')
            # entry_y.delete(0, 'end')

            point_x = [float(point) for point in input_x.split()]
            point_y = [float(point) for point in input_y.split()]
          
            if (len(point_x) <2 or len(point_y) < 2) and len(point_x) != len(point_y):
                messagebox.showerror("Error","Please enter at least two numberic")
                return
    
            for i in point_x:
                data_points['x'].append(i)
            for i in point_y:
                data_points['y'].append(i)
            for i in range(len(data_points['x'])):
                data_points['z'].append(data_points['x'][i] + data_points['y'][i])
  
            for i in range(0, len(points), 2):
                x, y = points[i:i + 2]
                data_points['x'].append(x)
                data_points['y'].append(y)
                data_points['z'].append(x + y)
            # Clear the previous 3D plot
            ax_3d.clear()

            ax_3d.scatter(data_points['x'], data_points['y'], data_points['z'], c='r', marker='o')

            # Example 3D plot (replace with your own data)
            # ax_3d.scatter(x, y, x + y, c='r', marker='o')

            # Customize the 3D plot
            ax_3d.set_title("3D Matplotlib Plot")
            ax_3d.set_xlabel("X-axis")
            ax_3d.set_ylabel("Y-axis")
            ax_3d.set_zlabel("Z-axis")

            # Draw the updated 3D plot on the canvas
            canvas_3d.draw()
        else:
            messagebox.showerror("Error", "This point already added")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

'''
# Create a function to add a new point to the list
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

def buildBaseFunction(ax_3d,function):
    ax_3d.clear()

    ax_3d.set_title("3D Matplotlib Plot")
    ax_3d.set_xlabel("X-axis")
    ax_3d.set_ylabel("Y-axis")
    ax_3d.set_zlabel("Z-axis")

    X, Y = np.meshgrid(x_data, y_data)
    Z = function(X, Y)

    ax_3d.plot_surface(X, Y, Z, cmap=ColorFigure.BONE.value)
    canvas_3d.draw()

def fillEntryDefaultForTest(arr_entry):
    arr_entry[0].insert(0,"-5")
    arr_entry[1].insert(0, "5")
    arr_entry[2].insert(0, "0.8")

def clearPoint():
    for i in scatter_points:
        i.remove()
    canvas_3d.draw()
    scatter_points.clear()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Matplotlib with Windows Form 3D")

    canvas_3d = FigureCanvasTkAgg(fig_3d, master=root)
    canvas_3d_widget = canvas_3d.get_tk_widget()

    createLabel.placement_label(root,"Start",0,1,5,1,1,5)
    createLabel.placement_label(root, "END", 1, 1, 5, 1, 1, 5)
    createLabel.placement_label(root, "STEP", 2, 1, 5, 1, 1, 5)

    entry_start = ttk.Entry(root)
    entry_end = ttk.Entry(root)
    entry_step = ttk.Entry(root)

    fillEntryDefaultForTest([entry_start, entry_end, entry_step])

    findMinGradientDescent_button = ttk.Button(root, text="Call gradient Descent", command=lambda: callGradient_DrawPoint())
    buildBaseFunc_btn = ttk.Button(root, text="Build base Plot",
                                   command=lambda: buildBaseFunction(ax_3d, function_1))
    clear_btn = ttk.Button(root,text="Clear points",command=clearPoint)
    addDefaultValue_btn = ttk.Button(root, text="Set point", command=setBaseData)
    save_button = ttk.Button(root, text="Save Schedule", command=save_plot)
    close_button = ttk.Button(root, text="Close Application", command=close_application)

    canvas_3d_widget.grid(row=0, column=0, rowspan=20, padx=5, pady=5) #matplotlib

    entry_start.grid(row=0, column=2,padx=5, pady=5,rowspan=1,columnspan=1,sticky="nsew")
    entry_end.grid(row=1, column=2,padx=5, pady=5,rowspan=1,columnspan=1,sticky="nsew")
    entry_step.grid(row=2, column=2,padx=5, pady=5,rowspan=1,columnspan=1,sticky="nsew")


    addDefaultValue_btn.grid(row=3,column=1,columnspan=2, padx=5, pady=5, sticky="nsew")
    buildBaseFunc_btn.grid(row=4, column=1, columnspan=2, padx=5, pady=5, sticky="nsew")
    findMinGradientDescent_button.grid(row=5, column=1, columnspan=2, padx=5, pady=5, sticky="nsew")
    clear_btn.grid(row=6,column=1,columnspan=2, padx=5, pady=5, sticky="nsew")
    save_button.grid(row=7, column=1, columnspan=2, padx=5, pady=5, sticky="nsew")
    close_button.grid(row=8, column=1, columnspan=2, padx=5, pady=5, sticky="nsew")

    # Configure row and column weights for resizing
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(9, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(3, weight=1)

    root.mainloop()