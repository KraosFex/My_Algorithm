from tkinter import *
from tkinter import ttk as tk
import re

root = Tk()
errmsg = StringVar()
formatmsg = "Zip should be ##### or #####-####"

def check_zip(newval, op):
    errmsg.set('')
    valid = re.match('^[0-9]{5}(\-[0-9]{4})?$', newval) is not None
    btn.state(['!disabled'] if valid else ['disabled'])
    if op=='key':
        ok_so_far = re.match('^[0-9\-]*$', newval) is not None and len(newval) <= 10
        if not ok_so_far:
            errmsg.set(formatmsg)
        return ok_so_far
    elif op=='focusout':
        if not valid:
            errmsg.set(formatmsg)
    return valid

check_zip_wrapper = (root.register(check_zip), '%P', '%V')

zip = StringVar()
f = tk.Frame(root)
f.grid(column=0, row=0)
tk.Label(f, text='Name:').grid(column=0, row=0, padx=5, pady=5)
tk.Entry(f).grid(column=1, row=0, padx=5, pady=5)
tk.Label(f, text='Zip:').grid(column=0, row=1, padx=5, pady=5)
e = tk.Entry(f, textvariable=zip, validate='all', validatecommand=check_zip_wrapper)
e.grid(column=1, row=1, padx=5, pady=5)
btn = tk.Button(f, text="Process")
btn.grid(column=2, row=1, padx=5, pady=5)
btn.state(['disabled'])
msg = tk.Label(f, font='TkSmallCaptionFont', foreground='red', textvariable=errmsg)
msg.grid(column=1, row=2, padx=5, pady=5, sticky='w')

root.mainloop()
