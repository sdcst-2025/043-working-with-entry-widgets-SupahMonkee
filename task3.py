#!python3

"""
Create the interface shown.  The program should be able to perform the math operation specified
by the buttons and display the entry in the 3rd entry widget;
"""

import tkinter as tk
from tkinter import *

def mult(event):
    print('event happened')
    print(f'details: {event}')
    num1 = e[0].get()
    num2 = e[1].get()
    num1 = float(num1)
    num2 = float(num2)
    result = (num1*num2)
    e[2].delete(0, tk.END)
    e[2].insert(0, result)

def add(event):
    print('event happened')
    print(f'details: {event}')
    num1 = e[0].get()
    num2 = e[1].get()
    num1 = float(num1)
    num2 = float(num2)
    result = (num1+num2)
    e[2].delete(0, tk.END)
    e[2].insert(0, result)

def sub(event):
    print('event happened')
    print(f'details: {event}')
    num1 = e[0].get()
    num2 = e[1].get()
    num1 = float(num1)
    num2 = float(num2)
    result = (num1-num2)
    e[2].delete(0, tk.END)
    e[2].insert(0, result)

def div(event):
    print('event happened')
    print(f'details: {event}')
    num1 = e[0].get()
    num2 = e[1].get()
    num1 = float(num1)
    num2 = float(num2)
    result = (num1/num2)
    e[2].delete(0, tk.END)
    e[2].insert(0, result)


w = tk.Tk()
w.attributes("-topmost",True)

l = []
l.append(tk.Label(w,text="Number 1"))
l.append(tk.Label(w,text="Number 2"))
l.append(tk.Label(w,text="Number Calculator"))


e = []
e.append(tk.Entry(w,text=""))
e.append(tk.Entry(w,text=""))
e.append(tk.Entry(w,text="answer"))
b=[]
b.append(tk.Button(w,text="x"))
b[0].bind('<Button-1>', mult)
b.append(tk.Button(w,text="+"))
b[1].bind('<Button-1>', add)
b.append(tk.Button(w,text="-"))
b[2].bind('<Button-1>', sub)
b.append(tk.Button(w,text="÷"))
b[3].bind('<Button-1>', div)

l[2].grid(row=1,column=1,columnspan=4)
l[0].grid(row=2,column=1,columnspan=2)
l[1].grid(row=2,column=3,columnspan=2)
e[0].grid(row=3,column=1, columnspan=2)
e[1].grid(row=3,column=3, columnspan=2)
b[0].grid(row=4,column=1)
b[1].grid(row=4,column=2)
b[2].grid(row=4,column=3)
b[3].grid(row=4,column=4)
e[2].grid(row=5,column=1,columnspan=4)

w.mainloop()
