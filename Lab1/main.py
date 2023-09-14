import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits import mplot3d #for 3D
from first_lab import gradient_descent
from first_lab import function
import random
from random import randint
from matplotlib.animation import FuncAnimation
#ax = plt.axes(projection="3d")
#ax.scatter(x_data,y_data,z_data,marker="v",alpha=0.1)

#
# X,Y = np.meshgrid(x_data,y_data)
# Z = np.sin(X) * np.cos(Y)
#
# ax.plot_surface(X,Y,Z,cmap="plasma")
# ax.view_init(azim=0,elev=90)

fig_3d = plt.figure()
ax_3d = fig_3d.add_subplot(111,projection="3d")
START = -5
END = 5
STEP = 0.6

x_data = []
y_data = []

data_points = {'x': [], 'y': [], 'z': []}
temp_input_x = ''
temp_input_y = ''

def clearDataPoint():
    data_points['x'].clear()
    data_points['y'].clear()
    data_points['z'].clear()
f2 = []
def animate(frame,arr,arr2):
    if(len(arr) > frame):
        ax_3d.scatter(arr[frame][0], arr[frame][1], arr[frame][2], c='green', marker='o',s=50)
    if (len(arr2) > frame):
        ax_3d.scatter(arr2[frame][0], arr2[frame][1], arr2[frame][2], c='r', marker='o', s=60)

def tempBtn(x_data,y_data) -> None:
    f2 = list(gradient_descent(function, random.choice(x_data), random.choice(y_data), 0.1, 500))
    temp = []
    temp2 = []
    for x, y, k, f in f2:
        temp.append([x,y,f-5])
    print(len(temp))
    f2 = list(gradient_descent(function, random.choice(x_data), random.choice(y_data), 0.1, 500))
    for x, y, k, f in f2:
        temp2.append([x, y, f - 5])
    print(len(temp2))
    ani = FuncAnimation(fig_3d, animate, frames=max(len(temp),len(temp2))//2,fargs=(temp,temp2,), interval=300, repeat=False)
   # for x, y, k, f in f2:
    #    ax_3d.scatter(x, y, f, c='r', marker='o')
    #    canvas_3d.draw()

        #data_points['x'].append(x)
        #data_points['y'].append(y)
        #data_points['z'].append(f)
    #ax_3d.clear()

    #ax_3d.scatter(data_points['x'], data_points['y'], data_points['z'], c='r', marker='o')

    canvas_3d.draw()
   # clearDataPoint()

def update_plot() -> None:
    try:
        global temp_input_x
        global temp_input_y
        #x = float(entry_x.get())
        #y = float(entry_y.get())
        input_x = entry_x.get()
        input_y = entry_y.get()
        points = [float(point) for point in input_x.split()]
        if True==True:#checkPointSimple(input_x,input_y)== True:
            temp_input_x = input_x
            temp_input_y = input_y
            #entry_x.delete(0,'end')
            #entry_y.delete(0, 'end')

            point_x = [float(point) for point in input_x.split()]
            point_y = [float(point) for point in input_y.split()]
            '''
            if (len(point_x) <2 or len(point_y) < 2) and len(point_x) != len(point_y):
                messagebox.showerror("Error","Please enter at least two numberic")
                return
    
            for i in point_x:
                data_points['x'].append(i)
            for i in point_y:
                data_points['y'].append(i)
            for i in range(len(data_points['x'])):
                data_points['z'].append(data_points['x'][i] + data_points['y'][i])
    '''
            for i in range(0, len(points), 2):
                x, y = points[i:i + 2]
                data_points['x'].append(x)
                data_points['y'].append(y)
                data_points['z'].append(x + y)
            # Clear the previous 3D plot
            ax_3d.clear()

            ax_3d.scatter(data_points['x'], data_points['y'], data_points['z'], c='r', marker='o')

            # Example 3D plot (replace with your own data)
            #ax_3d.scatter(x, y, x + y, c='r', marker='o')

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

def buildBaseFunction(ax_3d,x_data,y_data):
    ax_3d.clear()

    ax_3d.set_title("3D Matplotlib Plot")
    ax_3d.set_xlabel("X-axis")
    ax_3d.set_ylabel("Y-axis")
    ax_3d.set_zlabel("Z-axis")

    X, Y = np.meshgrid(x_data, y_data)
    Z = X ** 2.0 + Y ** 2.0

    ax_3d.plot_surface(X, Y, Z, cmap="plasma")
    canvas_3d.draw()

if __name__ == '__main__':
    x_data = np.arange(START, END, STEP)
    y_data = np.arange(START, END, STEP)

    root = tk.Tk()
    root.title("Matplotlib with Windows Form 3D")

    canvas_3d = FigureCanvasTkAgg(fig_3d, master=root)
    canvas_3d_widget = canvas_3d.get_tk_widget()

    label_x = ttk.Label(root,text="X:")
    label_y = ttk.Label(root, text="Y:")
    label_z = ttk.Label(root, text="Z:")
    entry_x = ttk.Entry(root)
    entry_y = ttk.Entry(root)
    entry_z = ttk.Entry(root)

    update_button = ttk.Button(root,text="Update Plot",command=lambda:tempBtn(x_data,y_data))
    baseFunc_btn = ttk.Button(root, text="Build base Plot", command=lambda: buildBaseFunction(ax_3d,x_data,y_data))
    #add_point_button = ttk.Button(root, text="Add Point", command=add_point)
    save_button = ttk.Button(root, text="Save Schedule", command=save_plot)
    close_button = ttk.Button(root, text="Close Application", command=close_application)


    canvas_3d_widget.grid(row=0, column=0, rowspan=6,padx=5, pady=5, sticky="nsew")
    label_x.grid(row=0,column=1)
    label_y.grid(row=1, column=1)
    label_z.grid(row=2, column=1)
    entry_x.grid(row=0, column=2)
    entry_y.grid(row=1, column=2)
    entry_z.grid(row=2, column=2)

    update_button.grid(row=3,column=1,columnspan=2,padx=5, pady=5, sticky="nsew")
    save_button.grid(row=4, column=1, columnspan=2,padx=5, pady=5, sticky="nsew")
    #add_point_button.grid(row=5, column=1, columnspan=2)
    baseFunc_btn.grid(row=5, column=1, columnspan=2,padx=5, pady=5, sticky="nsew")
    close_button.grid(row=6, column=1, columnspan=2,padx=5, pady=5, sticky="nsew")

    # Configure row and column weights for resizing
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(5, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(3, weight=1)

    root.mainloop()

    #plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
