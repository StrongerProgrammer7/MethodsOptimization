import random
import outer_imports.matplotlib  as omatpl
import global_variable as gv
import frontshow.Color as colors

def animate(frame, arr,best_result=None, textReach=None, marker=None):
    if len(arr) > frame:
        size_point = gv.SIZE_POINT
        color = gv.COLOR_POINT
        if (len(arr) - 1 == frame):
            color = colors.Color.RED.value
            size_point = 40
            if(best_result!=None):
                gv.bestPointSet.append(omatpl.ax_3d.scatter(best_result[0], best_result[1], best_result[2], c=best_result[3], marker=best_result[4], s=best_result[5]))
        if (textReach != None):
            point_z = None
            if(len(arr[frame]) == 2):
                point_z = gv.current_function(arr[frame][0],arr[frame][1])
            else:
                point_z = arr[frame][2]

            str_temp = "# " + str(frame) + " X=" + str(round(arr[frame][0], 4)) + " Y=" + str(round(arr[frame][1],4 )) + " Z=" + str(round(point_z, 4)) + "\n"
            textReach.insert(1.0, str_temp)
            if(len(arr) - 1 == frame):
                gv.extraScatter.append(omatpl.ax_3d.scatter(arr[frame][0], arr[frame][1], point_z, c=color, marker=marker, s=size_point, zorder=1))
            else:
                gv.scatter_points.append(omatpl.ax_3d.scatter(arr[frame][0], arr[frame][1], point_z, c=color, marker=marker, s=size_point,zorder=1))
            # If you, don't want to delete point , comment this code
            if len(gv.scatter_points)>15 and  len(arr)-2 > frame:
                random_countForDel = random.randint(2, 5)
                for i in range(0,random_countForDel):
                    randomPos = random.randint(0,len(gv.scatter_points)-2)
                    gv.scatter_points[randomPos].remove()
                    gv.scatter_points.remove(gv.scatter_points[randomPos])