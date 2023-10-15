import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits import mplot3d #for 3D

#ax = plt.axes(projection="3d")

#ax.scatter(x_data,y_data,z_data,marker="v",alpha=0.1)

# x_data = np.arange(-5,5,0.1)
# y_data = np.arange(-5,5,0.1)
#
# X,Y = np.meshgrid(x_data,y_data)
# Z = np.sin(X) * np.cos(Y)
#
# ax.plot_surface(X,Y,Z,cmap="plasma")
# ax.view_init(azim=0,elev=90)

points =[]
def update_plot():
    try:
       # x = float(entry_x.get())
        #y = float(entry_y.get())

        # Clear the previous 3D plot
        ax_3d.clear()

        if points:
            points_array = np.array(points)
            ax_3d.scatter(points_array[:, 0], points_array[:, 1], points_array[:, 2], c='r', marker='o')


        # Example 3D plot (replace with your own data)
        #ax_3d.scatter(x, y, x + y, c='r', marker='o')

        # Customize the 3D plot
        ax_3d.set_title("3D Matplotlib Plot")
        ax_3d.set_xlabel("X-axis")
        ax_3d.set_ylabel("Y-axis")
        ax_3d.set_zlabel("Z-axis")

        # Draw the updated 3D plot on the canvas
        canvas_3d.draw()

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

# Create a function to add a new point to the list
def add_point():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        z = float(entry_z.get())

        points.append([x, y, z])

        # Clear the input fields
        entry_x.delete(0, tk.END)
        entry_y.delete(0, tk.END)
        entry_z.delete(0, tk.END)

        # Update the plot
        update_plot()

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")


def close_application():
    root.quit()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Matplotlib with Windows Form 3D")

    fig_3d = plt.figure()
    ax_3d = fig_3d.add_subplot(111,projection="3d")

    canvas_3d = FigureCanvasTkAgg(fig_3d, master=root)
    canvas_3d_widget = canvas_3d.get_tk_widget()

    label_x = ttk.Label(root,text="X:")
    label_y = ttk.Label(root, text="Y:")
    label_z = ttk.Label(root, text="Z:")
    entry_x = ttk.Entry(root)
    entry_y = ttk.Entry(root)
    entry_z = ttk.Entry(root)

    update_button = ttk.Button(root,text="Update Plot",command=update_plot)
    add_point_button = ttk.Button(root, text="Add Point", command=add_point)
    save_button = ttk.Button(root, text="Save Schedule", command=save_plot)
    close_button = ttk.Button(root, text="Close Application", command=close_application)


    canvas_3d_widget.grid(row=0, column=0, rowspan=6)
    label_x.grid(row=0,column=1)
    label_y.grid(row=1, column=1)
    label_z.grid(row=2, column=1)
    entry_x.grid(row=0, column=2)
    entry_y.grid(row=1, column=2)
    entry_z.grid(row=2, column=2)

    update_button.grid(row=3,column=1,columnspan=2)
    save_button.grid(row=4, column=1, columnspan=2)
    add_point_button.grid(row=5, column=1, columnspan=2)
    close_button.grid(row=6, column=1, columnspan=2)

    root.mainloop()

#Moment draw
# for x, y, k, f in f2:
# data_points['x'].append(x)
# data_points['y'].append(y)
# data_points['z'].append(f)

# ax_3d.clear()
# ax_3d.scatter(data_points['x'], data_points['y'], data_points['z'], c='r', marker='o')
# clearDataPoint()