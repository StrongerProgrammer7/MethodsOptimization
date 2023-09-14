import tkinter as tk
from tkinter import ttk
ttk = tk
class createLabel:

    @staticmethod
    def placement_label(root,text,row,column,padx,rowspan,columnspan,pady):
        label = ttk.Label(root, text=text)
        label.grid(row=row, column=column, padx=padx, rowspan=rowspan, columnspan=columnspan, pady=pady)
