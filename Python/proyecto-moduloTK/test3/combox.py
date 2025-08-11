from tkinter import *
from tkinter import ttk as tk

root = Tk()

country = StringVar()
date = StringVar()

country = tk.Combobox(root, textvariable=country, values=("USA", "Venecolandia", "Panaputa")).grid()

dates = tk.Combobox(root, textvariable=date, )

root.mainloop()