from tkinter import *
from tkinter import ttk as tk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
mainframe = tk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = tk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
tk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

tk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

tk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
tk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
tk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()