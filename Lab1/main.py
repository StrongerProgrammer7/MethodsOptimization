import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d #for 3D

#Single Points
ax = plt.axes(projection="3d")
#ax.scatter(3,5,7)

#x_data = np.random.randint(0,100,(500,))
#y_data = np.random.randint(0,100,(500,))
#z_data = np.random.randint(0,100,(500,))
#ax.scatter(x_data,y_data,z_data,marker="v",alpha=0.1)

x_data = np.arange(-5,5,0.1)
y_data = np.arange(-5,5,0.1)

X,Y = np.meshgrid(x_data,y_data)
Z = np.sin(X) * np.cos(Y)

ax.plot_surface(X,Y,Z,cmap="plasma")
ax.view_init(azim=0,elev=90)
if __name__ == '__main__':
    plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
