from imports_tkinter import *

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits import mplot3d  # for 3D
from matplotlib.animation import FuncAnimation

import numpy as np
import random

from gradient_descent import gradient_descent
from Color import *
from setFunction import *
from frontshow.placement_elements import createLabel
from global_variable import *

fig_3d = plt.figure()
ax_3d = fig_3d.add_subplot(111, projection="3d")

def fillMatrix(resultGradient):
    temp = []
    print(resultGradient)
    for x, y, countIter, f in resultGradient:
        temp.append([x, y, f])
    return temp

def animate(frame, arr, arr2):
    if len(arr) > frame:
        scatter_points.append(ax_3d.scatter(arr[frame][0], arr[frame][1], arr[frame][2], c=Color.GREEN.value, marker='o', s=SIZE_POINT))
    if len(arr2) > frame:
        scatter_points.append(ax_3d.scatter(arr2[frame][0], arr2[frame][1], arr2[frame][2], c=Color.RED.value, marker='o', s=SIZE_POINT))

def callGradient_DrawPoint(textFieldCountIter) -> None:
    try:
        if(len(x_data) > 0 and len(y_data) > 0 and int(textFieldCountIter.get()) > 10):
            # Moment draw 2 min
            temp = fillMatrix(list(gradient_descent(current_function, random.choice(x_data), random.choice(y_data), 0.1, int(textFieldCountIter.get()))))
            temp2 = fillMatrix(list(gradient_descent(current_function, random.choice(x_data), random.choice(y_data), 0.1, int(textFieldCountIter.get()))))

            ani = FuncAnimation(fig_3d, animate, frames=max(len(temp), len(temp2)), fargs=(temp, temp2,), interval=SPEED,
                            repeat=False)
            canvas_3d.draw()
        else:
            print(len(x_data))
            print(len(y_data))
            print(int(textFieldCountIter.get()))
            messagebox.showerror("Error", "Invalid data. Fill defualt data and count iter.")
    except ValueError:
        messagebox.showerror("Error", "Invalid fillMatrix. Please check fill matrix and gradient_descent")


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

    ax_3d.plot_surface(X, Y, Z, cmap=ColorFigure.BONE.value)
    canvas_3d.draw()

def clearPoint():
    for i in scatter_points:
        i.remove()
    canvas_3d.draw()
    scatter_points.clear()

def selectFunc(event,combo,lab,textField):
    try:
        global STEP
        if len(textField.get()) > 0 and textField.get()!='' and float(textField.get())!=0:
            selection = combo.get()
            STEP = float(textField.get())
            #print(selection)
            global current_function
            global START
            global END
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



if __name__ == '__main__':
    root = tk.Tk()
    root.title("Matplotlib with Windows Form 3D")

    notebook = ttk.Notebook(root)

    canvas_3d = FigureCanvasTkAgg(fig_3d, master=root)
    canvas_3d_widget = canvas_3d.get_tk_widget()

    frame1 = ttk.Frame(notebook)
    frame2 = ttk.Frame(notebook)

    notebook.add(frame1, text="Tab1")
    notebook.add(frame2,text="Tab2")

    textFieldStep = ttk.Entry(frame1)
    textFieldStep.insert(0, "0.1")

    lab_func = createLabel.placement_label(frame1, "Choose function", 0, 1, 5, 1, 3, 5)

    comboBoxFunc = ttk.Combobox(frame1, values=["function_1", "function_2", "Bila", "Buta", "Bukina", "Eggholder"],
                                state="readonly")
    comboBoxFunc.bind("<<ComboboxSelected>>", lambda event, cb=comboBoxFunc,lab = lab_func,field=textFieldStep: selectFunc(event, cb,lab,field))

    createLabel.placement_label(frame1, "Choose Step", 2, 1, 5, 1, 3, 5)

    createLabel.placement_label(frame1, "Choose count iteration for gradient", 4, 1, 5, 1, 3, 5)
    textFieldCountIter = ttk.Entry(frame1)
    textFieldCountIter.insert(0, "500")

    findMinGradientDescent_button = ttk.Button(frame1, text="Call gradient Descent", command=lambda: callGradient_DrawPoint(textFieldCountIter))


    canvas_3d_widget.grid(row=0, column=0, rowspan=20, padx=5, pady=5) #matplotlib
    notebook.grid(row=0,column=1,padx=5,pady=5,rowspan=1,columnspan=3,sticky="nsew")

    comboBoxFunc.grid(row=1,column=1,padx=5,pady=5,rowspan=1,columnspan=3,sticky="nsew")
    textFieldStep.grid(row=3, column=1,padx=5, pady=5,rowspan=1,columnspan=3,sticky="nsew")
    textFieldCountIter.grid(row=5, column=1, padx=5, pady=5, rowspan=1, columnspan=3, sticky="nsew")
    findMinGradientDescent_button.grid(row=6, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

    clear_btn = ttk.Button(frame1, text="Clear points", command=clearPoint)
    save_button = ttk.Button(root, text="Save Schedule", command=save_plot)

    clear_btn.grid(row=7,column=1,columnspan=3, padx=5, pady=5, sticky="nsew")
    save_button.grid(row=8, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")
    close_button = ttk.Button(root, text="Close Application", command=close_application)
    close_button.grid(row=9, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

    # Configure row and column weights for resizing
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(10, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(3, weight=1)

    root.mainloop()