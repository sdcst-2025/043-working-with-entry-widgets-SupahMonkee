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


win = tk.Tk()
win.attributes("-topmost",True)
press1 = 0
press2 = 0
b_sign = 1
c_sign = 1


def factor(event):
    print('event happened')
    print(f'details: {event}')
    b = e[0].get()
    c = e[1].get()
    b = float(b)
    c = float(c)
    b = b*b_sign
    c = c*c_sign
    try:
        x1 = ((-1*b + math.sqrt(b**2 - 4*c))/(2))
        try:
            x2 = ((-1*b - math.sqrt(b**2 - 4*c))/(2))
            x1 = round(x1, 2)
            x1 = x1*-1
            x2 = round(x2, 2)
            x2 = x2*-1
            if x1 >= 0:
                x1 = str(f'(x+{x1})')
            else:
                x1 = str(f'(x{x1})')
            if x2 >= 0:
                x2 = str(f'(x+{x2})')
            else:
                x2 = str(f'(x{x2})')
            answer = (f'{x1}{x2}')
        except:
            x1 = round(x1, 2)
            if x1 >= 0:
                answer = str(f'(x+{x1})')
            else:
                answer = str(f'(x{x1})')
    except:
        x1 = ('dne')
        try:
            x2 = ((-1*b - math.sqrt(b**2 - 4*c))/(2))
            x2 = round(x2, 2)
            x2 = x2*-1
            if x2 >= 0:
                answer = str(f'(x+{x2})')
            else:
                answer = str(f'(x{x2})')
                
        except:
            answer = ('No Real Roots')
    e[2].delete(0, tk.END)
    e[2].insert(0, answer)

def swap1(event):
    print('event happened')
    print(f'details: {event}')
    global press1
    press1 += 1
    if press1 % 2 != 0:
        b[0].config(text='-')
    else:
        b[0].config(text='+')
    global b_sign
    b_sign = b_sign*-1

def swap2(event):
    print('event happened')
    print(f'details: {event}')
    global press2
    press2 += 1
    if press2 % 2 != 0:
        b[1].config(text='-')
    else:
        b[1].config(text='+')
    global c_sign
    c_sign = c_sign*-1


l = []
l.append(tk.Label(win, text='Trinomial Factorer')) #title
l.append(tk.Label(win, text='Input coefficients for b and c.')) #instructions
l.append(tk.Label(win, text='x^2')) #ax^2
l.append(tk.Label(win, text='x')) #bx
l.append(tk.Label(win, text='Factor(s) of x are:')) #answer

e = []
e.append(tk.Entry(win, text='',width=2)) #bx
e.append(tk.Entry(win, text='',width=2)) #c
e.append(tk.Entry(win, text='',width=15)) #answer

b = []
b.append(tk.Button(win, text='+',height=0,width=0)) #ax^2 + bx
b[0].bind('<Button-1>', swap1)
b.append(tk.Button(win, text='+')) #bx + c
b[1].bind('<Button-1>', swap2)
b.append(tk.Button(win, text='FACTOR ME!')) #solve
b[2].bind('<Button-1>', factor)


l[0].place(x=50, y=0)
l[1].place(x=25, y=20)
l[2].place(x=45, y=43)
b[0].place(x=70, y=40)
e[0].place(x=90,y=43)
l[3].place(x=105,y=43)
b[1].place(x=115,y=40)
e[1].place(x=135,y=43)
b[2].place(x=60, y=75)
l[4].place(x=53, y=100)
e[2].place(x=52, y=125)


win.mainloop()


#done