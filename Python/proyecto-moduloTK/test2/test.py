from tkinter import *
from tkinter import ttk as tk

def calcula():
    print(f"la sumana de 2 + 2 = {2 + 2}")

root = Tk()
content = tk.Frame(root, padding="3 3 12 12").grid(row=0, column=0)
tk.Label(content, text="Preciona el boton para conocer el resultado de sumar 2 + 2").grid(row=0, column=0)
tk.Button(content, text="Preciona", command=calcula).grid(row=0, column=1, columnspan=2)
root.mainloop()