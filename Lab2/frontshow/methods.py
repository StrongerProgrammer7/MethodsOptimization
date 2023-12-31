import outer_imports.imports_tkinter as otk
import numpy as np
from outer_imports.matplotlib import fig_3d
from frontshow.Color import ColorFigure, colors_3DGraphic, colors_points
import global_variable as gv
from setFunction import chooseFunc

def buildBaseFunction(ax_3d,colorGraphic=ColorFigure.WINTER.value):
    if(len(gv.scatter_points) >0 or len(gv.bestPointSet)> 0 or len(gv.extraScatter) > 0):
        otk.messagebox.showinfo("Warning", "Clear points!")
        return
    ax_3d.clear()

    ax_3d.set_title("3D Matplotlib Plot")
    ax_3d.set_xlabel("X-axis")
    ax_3d.set_ylabel("Y-axis")
    ax_3d.set_zlabel("Z-axis")

    if type(gv.START) == dict:
        gv.x_data = np.arange(gv.START[1], gv.START[2], gv.STEP)
        gv.y_data = np.arange(gv.END[1], gv.END[2], gv.STEP)
    else:
        gv.x_data = np.arange(gv.START, gv.END, gv.STEP)
        gv.y_data = np.arange(gv.START, gv.END, gv.STEP)

    X, Y = np.meshgrid(gv.x_data, gv.y_data)
    Z = gv.current_function(X, Y)
    #plot_wireframe
    ax_3d.plot_surface(X, Y, Z, cmap=colorGraphic,alpha=0.8,rstride=1, cstride=1,zorder=0)
    gv.canvas_3d.draw()

def selectFunc(event,ax_3d,combo,lab,textField):
    try:
        if len(textField.get()) > 0 and textField.get()!='' and float(textField.get())!=0:
            #if(gv.COLOR_3DGRAPHIC == None):
                #otk.messagebox.showerror("Error", "Choose color")
                #return
            selection = combo.get()
            gv.STEP = float(textField.get())
            if selection in chooseFunc:
                gv.current_function = chooseFunc[selection]['f']
            if selection == "Букина" or selection == "Розенброк":
                gv.START = chooseFunc[selection]['x']
                gv.END = chooseFunc[selection]['y']
            else:
                gv.START = chooseFunc[selection]['from']
                gv.END = chooseFunc[selection]['to']

            buildBaseFunction(ax_3d,gv.COLOR_3DGRAPHIC)
            lab.config(text="Функция:" + selection)
        else:
            otk.messagebox.showerror("Error", "Invalid input. Please enter numeric values step.")
    except ValueError:
        otk.messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

def selectColor(event,combo,ax_3d):
    try:
        selection = combo.get()
        if gv.COLOR_3DGRAPHIC == None:
            gv.COLOR_3DGRAPHIC = colors_3DGraphic[selection]
        else:
            gv.COLOR_3DGRAPHIC = colors_3DGraphic[selection]
            buildBaseFunction(ax_3d,gv.COLOR_3DGRAPHIC)
    except ValueError:
        otk.messagebox.showerror("Error", "Problem with color graphic. Send message admin")

def selectColorPoints(event,combo):
    try:
        selection = combo.get()
        gv.COLOR_POINT = colors_points[selection]
        # If you, don't want to delete point and different color for every run, comment this code
        if(len(gv.scatter_points) >0):
            for point in gv.scatter_points:
                point.set_facecolors(gv.COLOR_POINT)
            gv.canvas_3d.draw()

    except ValueError:
        otk.messagebox.showerror("Error", "Problem with color point. Send message admin")

def save_plot():
    try:
        file_path = otk.filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            fig_3d.savefig(file_path)
            otk.messagebox.showinfo("Успех", "График сохранен.")

    except Exception as e:
        otk.messagebox.showerror("Error", f"An error occurred while saving the plot: {str(e)}")

def close_application(root):
    root.quit()

def clearPoints():
    for i in gv.scatter_points:
        i.remove()
    if(len(gv.bestPointSet) > 0):
        for i in gv.bestPointSet:
            i.remove()
    if(len(gv.extraScatter) > 0):
        for i in gv.extraScatter:
            i.remove()
    gv.textReachGradientPoint.delete(1.0,otk.tk.END)
    gv.textReachQuadPoint.delete(1.0, otk.tk.END)
    gv.textReachGenetic.delete(1.0, otk.tk.END)
    gv.textReachSwarm.delete(1.0,otk.tk.END)
    gv.textReachBees.delete(1.0,otk.tk.END)
    gv.textReachBacterial.delete(1.0,otk.tk.END)
    gv.textReachImmuneSystem.delete(1.0,otk.tk.END)
    gv.textReachHybrid.delete(1.0,otk.tk.END)
    gv.canvas_3d.draw()
    gv.scatter_points.clear()
    gv.bestPointSet.clear()
    gv.extraScatter.clear()