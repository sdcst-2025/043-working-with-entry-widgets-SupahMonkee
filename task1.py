"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""
import tkinter as tk
from tkinter import *


def run(e):
    print('event ran')
    print(f'details of event are {e}')
    namedata = name.get()
    studnumdata = studnum.get()
    gradedata = grade.get()
    gurt = (f'{namedata}, {studnumdata}, Grade {gradedata}')
    info.delete(0, tk.END)
    info.insert(0,gurt)

win = tk.Tk()
nametxt = tk.Label(win, text="Name:")
name = tk.Entry(win, width=30)
studnumtxt = tk.Label(win, text="Student Number:")
studnum = tk.Entry(win, width=30)
gradetxt = tk.Label(win, text="Grade:")
grade = tk.Entry(win, width=30)
enter = tk.Button(win, width=30, text= "Click to Enter")
info = tk.Entry(win, width=30)

enter.bind('<Button-1>', run)

nametxt.pack()
name.pack()
studnumtxt.pack()
studnum.pack()
gradetxt.pack()
grade.pack()
enter.pack()
info.pack()

win.mainloop()

#done