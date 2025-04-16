#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""

import tkinter as tk
import math
from tkinter import *


def run(e):
    print('Event Happened')
    print(f'Details: {e}')
    s1data = s1.get()
    s2data = s2.get()
    s1data = float(s1data)
    s2data = float(s2data)
    ansdata = (math.sqrt(s1data**2 + s2data**2))
    ans.delete(0, tk.END)
    ans.insert(0, ansdata)


win = tk.Tk()
title = tk.Label(win, text="Hypotenuse Solver")
s1text = tk.Label(win, text="\nFirst side length:")
s1 = tk.Entry(win, width=30)
s2text = tk.Label(win, text="Second side length:")
s2 = tk.Entry(win, width=30)
button = tk.Button(win, text='Click to enter')
anstext = tk.Label(win, text='Hypotenuse length:')
ans = tk.Entry(win, width=30)

button.bind('<Button-1>', run)

title.pack()
s1text.pack()
s1.pack()
s2text.pack()
s2.pack()
button.pack()
anstext.pack()
ans.pack()

win.mainloop()

#done