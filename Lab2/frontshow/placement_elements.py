import outer_imports.imports_tkinter as otk
import global_variable as gv


class createLabel:
    @staticmethod
    def placement_label(root, text, row, column, padx, rowspan, columnspan, pady):
        label = otk.ttk.Label(root, text=text)
        label.grid(row=row, column=column, padx=padx, rowspan=rowspan, columnspan=columnspan, pady=pady)
        return label


def createTab_gradient(tab, call_function):
    createLabel.placement_label(tab, "Количество итераций", 0, 1, 5, 1, 3, 5)
    textFieldCountIter = otk.ttk.Entry(tab)
    textFieldCountIter.insert(0, "500")

    findMinGradientDescent_button = otk.ttk.Button(tab, text="Выполнить градиентный спуск",
                                                   command=lambda: call_function(textFieldCountIter))
    textFieldCountIter.grid(row=1, column=1, padx=5, pady=5, rowspan=1, columnspan=3, sticky="nsew")
    findMinGradientDescent_button.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

    gv.textReachGradientPoint = otk.ScrolledText(tab, height=10, width=30)
    gv.textReachGradientPoint.grid(row=3, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")


def createTab_simpleMethod(tab, call_function):
    findQud_btn = otk.ttk.Button(tab, text='Вызов симплекс метода', command=lambda: call_function())
    findQud_btn.grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

    gv.textReachQuadPoint = otk.ScrolledText(tab, height=10, width=30)
    gv.textReachQuadPoint.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")


def createTab_genetic_hybrid(tab, call_function, text_btn):
    createLabel.placement_label(tab, "Размер популяции", 0, 1, 5, 1, 3, 5)
    textField_populationSize = otk.ttk.Entry(tab)
    textField_populationSize.insert(0, "50")

    createLabel.placement_label(tab, "Количество генераций", 2, 1, 5, 1, 3, 5)
    textField_numGeneratics = otk.ttk.Entry(tab)
    textField_numGeneratics.insert(0, "100")

    textField_populationSize.grid(row=1, column=1, padx=5, pady=5, rowspan=1, columnspan=3, sticky="nsew")
    textField_numGeneratics.grid(row=3, column=1, padx=5, pady=5, rowspan=1, columnspan=3, sticky="nsew")

    lab_optimalFunc = createLabel.placement_label(tab, "Оптимальное значение функции: ", 4, 1, 5, 1, 3, 5)
    lab_optimalValuePoints = createLabel.placement_label(tab, "Оптимальное значение переменных", 5, 1, 5, 1, 3, 5)

    generatics_btn = otk.ttk.Button(tab, text=text_btn,
                                    command=lambda: call_function(textField_populationSize, textField_numGeneratics,
                                                                  lab_optimalFunc, lab_optimalValuePoints))
    generatics_btn.grid(row=6, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")


def createTab_Genetic(tab, call_function):
    createTab_genetic_hybrid(tab, call_function, "Вызвать генетический")

    gv.textReachGenetic = otk.ScrolledText(tab, height=10, width=30)
    gv.textReachGenetic.grid(row=7, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")


def createTab_Hybrid(tab, call_function):
    createTab_genetic_hybrid(tab, call_function, "Вызвать гибрид")

    gv.textReachHybrid = otk.ScrolledText(tab, height=10, width=30)
    gv.textReachHybrid.grid(row=7, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")


def createTab_Swarm(tab, call_function):
    tf_swarm = []

    createLabel.placement_label(tab, "Размер Роя", 0, 0, 5, 1, 1, 5)
    tF = otk.ttk.Entry(tab)
    tF.insert(0, "50")
    tF.grid(row=0, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf_swarm.append(tF)

    createLabel.placement_label(tab, "Общий масштабирующий\n коэффициент для скорости", 1, 0, 5, 1, 1, 5)
    tF = otk.ttk.Entry(tab)
    tF.insert(0, "0.1")
    tF.grid(row=1, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf_swarm.append(tF)

    createLabel.placement_label(tab,
                                "Коэффициент, задающий влияние лучшей точки,\n найденной каждой частицей,\n на будущую скорость",
                                2, 0, 5, 1, 1, 5)
    tF = otk.ttk.Entry(tab)
    tF.insert(0, "1")
    tF.grid(row=2, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf_swarm.append(tF)

    createLabel.placement_label(tab,
                                "Коэффициент, задающий влияние лучшей точки,\n найденной всеми частицами,\n на будущую скорость",
                                3, 0, 5, 1, 1, 5)
    tF = otk.ttk.Entry(tab)
    tF.insert(0, "5")
    tF.grid(row=3, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf_swarm.append(tF)

    createLabel.placement_label(tab, "Количество жизней", 4, 0, 5, 1, 1, 5)
    tF = otk.ttk.Entry(tab)
    tF.insert(0, "100")
    tF.grid(row=4, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf_swarm.append(tF)

    # createLabel.placement_label(tab, "Start", 5, 0, 5, 1, 1, 5)
    # createLabel.placement_label(tab, "End", 5, 1, 5, 1, 1, 5)
    # tF = otk.ttk.Entry(tab)
    # tF.insert(0, "-5")
    # tF.grid(row=6, column=0, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    # tf_swarm.append(tF)

    # tF = otk.ttk.Entry(tab)
    # tF.insert(0, "5")
    # tF.grid(row=6, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    #  tf_swarm.append(tF)

    btn = otk.ttk.Button(tab, text='Вызвать рой', command=lambda: call_function(tf_swarm))
    btn.grid(row=5, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

    gv.textReachSwarm = otk.ScrolledText(tab, height=10, width=30)
    gv.textReachSwarm.grid(row=6, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")


def createTab_insects(tab, text_count, count, text_generation, count_generations, text_call, call_function):
    tf = []

    createLabel.placement_label(tab, "Мин х", 0, 0, 5, 1, 1, 5)
    tF = otk.ttk.Entry(tab)
    tF.insert(0, "-5.12")
    tF.grid(row=0, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf.append(tF)

    createLabel.placement_label(tab, "Макс х", 1, 0, 5, 1, 1, 5)
    tF = otk.ttk.Entry(tab)
    tF.insert(0, "5.12")
    tF.grid(row=1, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf.append(tF)

    createLabel.placement_label(tab, "Мин у", 2, 0, 5, 1, 1, 5)
    tF = otk.ttk.Entry(tab)
    tF.insert(0, "-5.12")
    tF.grid(row=2, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf.append(tF)

    createLabel.placement_label(tab, "Макс у", 3, 0, 5, 1, 1, 5)
    tF = otk.ttk.Entry(tab)
    tF.insert(0, "5.12")
    tF.grid(row=3, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf.append(tF)

    createLabel.placement_label(tab, text_count, 4, 0, 5, 1, 1, 5)
    tF = otk.ttk.Entry(tab)
    tF.insert(0, count)
    tF.grid(row=4, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf.append(tF)

    createLabel.placement_label(tab, text_generation, 5, 0, 5, 1, 1, 5)
    tF = otk.ttk.Entry(tab)
    tF.insert(0, count_generations)
    tF.grid(row=5, column=1, padx=5, pady=5, rowspan=1, columnspan=2, sticky="nsew")
    tf.append(tF)

    btn = otk.ttk.Button(tab, text=text_call, command=lambda: call_function(tf))
    btn.grid(row=6, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")


def createTab_Bees(tab, call_function):
    createTab_insects(tab, "Количество пчелок", 200, "Время(мс)", 100, "Вызвать пчелок", call_function)

    gv.textReachBees = otk.ScrolledText(tab, height=10, width=30)
    gv.textReachBees.grid(row=7, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")


def createTab_Bacterial(tab, call_function):
    createTab_insects(tab, "Количество бактерий", 200, "Время(мс)", 100, "Вызвать бактерии", call_function)

    gv.textReachBacterial = otk.ScrolledText(tab, height=10, width=30)
    gv.textReachBacterial.grid(row=7, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")


def createTab_ImmuneSystem(tab, call_function):
    createTab_insects(tab, "Размер популяции", 200, "Генераций", 500, "Вызвать имунную систему", call_function)

    gv.textReachImmuneSystem = otk.ScrolledText(tab, height=10, width=30)
    gv.textReachImmuneSystem.grid(row=7, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")
