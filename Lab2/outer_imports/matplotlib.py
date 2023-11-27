import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits import mplot3d  # for 3D
from matplotlib.animation import FuncAnimation

fig_3d = plt.figure()
ax_3d = fig_3d.add_subplot(111, projection="3d",computed_zorder=False)