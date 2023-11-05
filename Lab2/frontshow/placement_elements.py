import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
ttk = tk


class createLabel:
    @staticmethod
    def placement_label(root,text,row,column,padx,rowspan,columnspan,pady):
        label = ttk.Label(root, text=text)
        label.grid(row=row, column=column, padx=padx, rowspan=rowspan, columnspan=columnspan, pady=pady)
        return label


def createTab_gradient(tab,call_function,ttk):
    createLabel.placement_label(tab, "Количество итераций", 0, 1, 5, 1, 3, 5)
    textFieldCountIter = ttk.Entry(tab)
    textFieldCountIter.insert(0, "500")

    findMinGradientDescent_button = ttk.Button(tab, text="Выполнить градиентный спуск",
                                               command=lambda: call_function(textFieldCountIter))
    textFieldCountIter.grid(row=1, column=1, padx=5, pady=5, rowspan=1, columnspan=3, sticky="nsew")
    findMinGradientDescent_button.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")


    textReachGradientPoint = ScrolledText(tab, height=10, width=30)
    textReachGradientPoint.grid(row=3,column=1, columnspan=3, padx=5, pady=5, sticky="nsew")
    return textReachGradientPoint


def createTab_simpleMethod(tab,call_function,ttk):
    findQud_btn = ttk.Button(tab, text='Вызов симплекс метода', command=lambda: call_function())
    findQud_btn.grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

    textReachQuadPoint = ScrolledText(tab, height=10, width=30)
    textReachQuadPoint.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")
    return textReachQuadPoint

def createTab_Genetic(tab,call_function,ttk):
    createLabel.placement_label(tab, "Размер популяции", 0, 1, 5, 1, 3, 5)
    textField_populationSize = ttk.Entry(tab)
    textField_populationSize.insert(0, "50")

    createLabel.placement_label(tab, "Количество генераций", 2, 1, 5, 1, 3, 5)
    textField_numGeneratics= ttk.Entry(tab)
    textField_numGeneratics.insert(0, "100")

    textField_populationSize.grid(row=1, column=1, padx=5, pady=5, rowspan=1, columnspan=3, sticky="nsew")
    textField_numGeneratics.grid(row=3, column=1, padx=5, pady=5, rowspan=1, columnspan=3, sticky="nsew")

    lab_optimalFunc = createLabel.placement_label(tab, "Оптимальное значение функции: ", 4, 1, 5, 1, 3, 5)
    lab_optimalValuePoints = createLabel.placement_label(tab, "Оптимальное значение переменных", 5, 1, 5, 1, 3, 5)

    generatics_btn = ttk.Button(tab, text='Вызвать генетический', command=lambda: call_function(textField_populationSize,textField_numGeneratics,lab_optimalFunc,lab_optimalValuePoints))
    generatics_btn.grid(row=6, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

    textReachGeneraticPoints = ScrolledText(tab, height=10, width=30)
    textReachGeneraticPoints.grid(row=7, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")
    return textReachGeneraticPoints

def createTab_Swarm(tab,call_function,ttk):
    tf_swarm = []

    createLabel.placement_label(tab, "Размер Роя", 0, 0, 5, 1, 1, 5)
    tF = ttk.Entry(tab)
    tF.insert(0, "50")
    tF.grid(row=0, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf_swarm.append(tF)

    createLabel.placement_label(tab, "Общий масштабирующий\n коэффициент для скорости", 1, 0, 5, 1, 1, 5)
    tF = ttk.Entry(tab)
    tF.insert(0, "0.1")
    tF.grid(row=1, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf_swarm.append(tF)

    createLabel.placement_label(tab, "Коэффициент, задающий влияние лучшей точки,\n найденной каждой частицей,\n на будущую скорость", 2, 0, 5, 1, 1, 5)
    tF = ttk.Entry(tab)
    tF.insert(0, "1")
    tF.grid(row=2, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf_swarm.append(tF)

    createLabel.placement_label(tab, "Коэффициент, задающий влияние лучшей точки,\n найденной всеми частицами,\n на будущую скорость", 3, 0, 5, 1, 1, 5)
    tF = ttk.Entry(tab)
    tF.insert(0, "5")
    tF.grid(row=3, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf_swarm.append(tF)

    createLabel.placement_label(tab, "Количество жизней", 4, 0, 5, 1, 1, 5)
    tF = ttk.Entry(tab)
    tF.insert(0, "100")
    tF.grid(row=4, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf_swarm.append(tF)

    #createLabel.placement_label(tab, "Start", 5, 0, 5, 1, 1, 5)
   # createLabel.placement_label(tab, "End", 5, 1, 5, 1, 1, 5)
   # tF = ttk.Entry(tab)
   # tF.insert(0, "-5")
   # tF.grid(row=6, column=0, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
   # tf_swarm.append(tF)

   # tF = ttk.Entry(tab)
   # tF.insert(0, "5")
   # tF.grid(row=6, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
  #  tf_swarm.append(tF)

    btn = ttk.Button(tab, text='Вызвать рой',command=lambda: call_function(tf_swarm))
    btn.grid(row=5, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

    textReachSwarm = ScrolledText(tab, height=10, width=30)
    textReachSwarm.grid(row=6, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")
    return textReachSwarm


def createTab_insects(tab,text_count,count,time,text_call,call_function,ttk):
    tf = []

    createLabel.placement_label(tab, "Мин х", 0, 0, 5, 1, 1, 5)
    tF = ttk.Entry(tab)
    tF.insert(0, "-5.12")
    tF.grid(row=0, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf.append(tF)

    createLabel.placement_label(tab, "Макс х", 1, 0, 5, 1, 1, 5)
    tF = ttk.Entry(tab)
    tF.insert(0, "5.12")
    tF.grid(row=1, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf.append(tF)

    createLabel.placement_label(tab, "Мин у", 2, 0, 5, 1, 1, 5)
    tF = ttk.Entry(tab)
    tF.insert(0, "-5.12")
    tF.grid(row=2, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf.append(tF)

    createLabel.placement_label(tab, "Макс у", 3, 0, 5, 1, 1, 5)
    tF = ttk.Entry(tab)
    tF.insert(0, "5.12")
    tF.grid(row=3, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf.append(tF)

    createLabel.placement_label(tab, text_count, 4, 0, 5, 1, 1, 5)
    tF = ttk.Entry(tab)
    tF.insert(0, count)
    tF.grid(row=4, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf.append(tF)

    createLabel.placement_label(tab, "Время(мс)", 5, 0, 5, 1, 1, 5)
    tF = ttk.Entry(tab)
    tF.insert(0, time)
    tF.grid(row=5, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf.append(tF)

    btn = ttk.Button(tab, text=text_call, command=lambda: call_function(tf))
    btn.grid(row=6, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

def createTab_Bees(tab,call_function,ttk):
    createTab_insects(tab,"Количество пчелок",200,100,"Вызвать пчелок",call_function,ttk)


    textReachBees = ScrolledText(tab, height=10, width=30)
    textReachBees.grid(row=7, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")
    return textReachBees


def createTab_Bacterial(tab,call_function,ttk):
    createTab_insects(tab,"Количество бактерий",200,100,"Вызвать бактерии",call_function,ttk)

    textReachBacterial = ScrolledText(tab, height=10, width=30)
    textReachBacterial.grid(row=7, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")
    return textReachBacterial