"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""
import tkinter as tk
from tkinter import *
import math

def factor(e):
    print('event happened')
    print(f'details: {e}')

def swap1(e):
    print('event happened')
    print(f'details: {e}')

def swap2(e):
    print('event happened')
    print(f'details: {e}')

win = tk.Tk()
win.attributes("-topmost",True)

l = []
l.append(tk.Label(win, text='Trinomial Factorer')) #title
l.append(tk.Label(win, text='Input coefficients for b and c.')) #instructions
l.append(tk.Label(win, text='x^2')) #ax^2
l.append(tk.Label(win, text='x')) #bx
l.append(tk.Label(win, text='Factors of x are:')) #answer

e = []
e.append(tk.Entry(win, text='',width=2)) #bx
e.append(tk.Entry(win, text='',width=2)) #c
e.append(tk.Entry(win, text='')) #answer

b = []
b.append(tk.Button(win, text='+',height=0,width=0)) #ax^2 + bx
b.append(tk.Button(win, text='+')) #bx + c
b.append(tk.Button(win, text='FACTOR ME!')) #solve


l[0].place(x=50, y=0)
l[1].place(x=25, y=20)
l[2].place(x=45, y=43)
b[0].place(x=70, y=40)
e[0].place(x=90,y=43)
l[3].place(x=105,y=43)
b[1].place(x=115,y=40)
e[1].place(x=135,y=43)
b[2].place(x=60, y=75)

win.mainloop()