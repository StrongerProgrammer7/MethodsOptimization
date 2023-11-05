from tkinter import messagebox

from backend.simplexMethod import get_points
import global_variable as gv
import frontshow.animation as anim
import outer_imports.matplotlib  as omatpl

def call_simplex_method() -> None:
    try:
        if(len(gv.x_data) > 0 and len(gv.y_data) > 0 and gv.current_function.__name__ == "quadratic"):
            points = get_points(max(gv.x_data),max(gv.y_data),gv.current_function)
            ani = omatpl.FuncAnimation(omatpl.fig_3d, anim.animate, frames=len(points), fargs=(points, None,gv.textReachQuadPoint,'x',), interval=gv.SPEED, repeat=False)
            gv.canvas_3d.draw()
        else:
            print(len(gv.x_data))
            print(len(gv.y_data))
            messagebox.showerror("Error", "Invalid data. Fill defualt data or choose other function. Simplex work only quadratic")
    except ValueError:
        messagebox.showerror("Error", "Invalid fillMatrix. Please check fill matrix and simplex_method")