from outer_imports.imports_tkinter import *
from outer_imports.matplotlib import *
import global_variable as gv

from frontshow.placement_elements import (createLabel,
                                          createTab_gradient, createTab_simpleMethod,
                                          createTab_Genetic, createTab_Swarm,
                                          createTab_Bees, createTab_Bacterial, createTab_ImmuneSystem, createTab_Hybrid)

from frontshow.methods import save_plot,close_application,selectFunc,clearPoints
from frontshow.calc_algorithm.gradientDescentShow import callGradient_DrawPoint
from frontshow.calc_algorithm.simpleMethodShow import call_simplex_method
from frontshow.calc_algorithm.geneticAlgorithmShow import call_geneticsAlgorithm
from frontshow.calc_algorithm.swarmShow import call_Swarm
from frontshow.calc_algorithm.beesShow import call_Bees
from frontshow.calc_algorithm.bacterialShow import call_Bacterial
from frontshow.calc_algorithm.aritificialImmuneSystemShow import call_AIimmuneSystem
from frontshow.calc_algorithm.hybridShow import call_hybridAlgorithm

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Matplotlib with Windows Form 3D")

    notebook = ttk.Notebook(root)

    gv.canvas_3d = FigureCanvasTkAgg(fig_3d, master=root)
    canvas_3d_widget = gv.canvas_3d.get_tk_widget()

    frame1 = ttk.Frame(notebook)
    frame2 = ttk.Frame(notebook)
    frame3 = ttk.Frame(notebook)
    frame4 = ttk.Frame(notebook)
    frame5 = ttk.Frame(notebook)
    frame6 = ttk.Frame(notebook)
    frame7 = ttk.Frame(notebook)
    frame8 = ttk.Frame(notebook)

    notebook.add(frame1, text="Градиент")
    notebook.add(frame2,text="Квадратичная ф-я")
    notebook.add(frame3, text="Генетический")
    notebook.add(frame4, text="Рой")
    notebook.add(frame5, text="Пчелки")
    notebook.add(frame6, text="Бактерии")
    notebook.add(frame7, text="Иммунная система")
    notebook.add(frame8, text="Гибрид")

    createTab_gradient(frame1,callGradient_DrawPoint)
    createTab_simpleMethod(frame2,call_simplex_method)
    createTab_Genetic(frame3,call_geneticsAlgorithm)
    createTab_Swarm(frame4,call_Swarm)
    createTab_Bees(frame5,call_Bees)
    createTab_Bacterial(frame6,call_Bacterial)
    createTab_ImmuneSystem(frame7, call_AIimmuneSystem)
    createTab_Hybrid(frame8, call_hybridAlgorithm)

    createLabel.placement_label(root, "Шаг(епсилон)", 1, 1, 5, 1, 3, 5)
    textFieldStep = ttk.Entry(root)
    textFieldStep.insert(0, str(gv.STEP))

    lab_func = createLabel.placement_label(root, "Выбор базовой функции", 3, 1, 5, 1, 3, 5)
    comboBoxFunc = ttk.Combobox(root, values=[
        "Квадратная",
        "Синусоида",
        "Билла",
        "Бута",
        "Букина",
        "Эгхолдера",
        "Квадратичная",
        "Розенброк",
        "Рома",
        "Растригина",
        "Химмельблау"],state="readonly")
    comboBoxFunc.bind("<<ComboboxSelected>>", lambda event, cb=comboBoxFunc,lab = lab_func,field=textFieldStep: selectFunc(event, ax_3d,cb,lab,field))

    canvas_3d_widget.grid(row=0, column=0, padx=5, pady=0) #matplotlib
    notebook.grid(row=0,column=1,padx=5,pady=0,columnspan=5,sticky="nsew")

    comboBoxFunc.grid(row=4,column=1,padx=5,pady=5,rowspan=1,columnspan=3,sticky="nsew")
    textFieldStep.grid(row=2, column=1,padx=5, pady=5,rowspan=1,columnspan=3,sticky="nsew")


    clear_btn = ttk.Button(root, text="Очистить точки с графика", command=clearPoints)
    clear_btn.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

    save_button = ttk.Button(root, text="Сохранить график", command=save_plot)
    save_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")
    close_button = ttk.Button(root, text="Закрыть приложение",  command=lambda: close_application(root))
    close_button.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")


    root.grid_rowconfigure(12, weight=1)
    root.grid_columnconfigure(3, weight=1)

    root.mainloop()