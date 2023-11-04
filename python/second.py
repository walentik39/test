#!/usr/bin/env python3

import math as m
import os
import subprocess
import sys
import random
from tkinter import *
from tkinter import colorchooser
import turtle
w1=turtle.Turtle()
for c in ['green','red','yellow','blue','black']:
    w1.circle(12)
    w1.color(c)
    w1.forward(75)
    w1.left(90)
    w1.circle(12)
    w1.color(c)
    w1.forward(65)
    w1.left(80)
    w1.color(c)
    w1.forward(65)
    w1.circle(12)
    w1.color(c)
    w1.left(90)
    
w = Tk()
w.title("Надо попробовать!")
w.geometry("450x450")
w.config(bg='#725279')

w2 =Tk()
w2.title('Привет')
w2.geometry('220x220')
w2.config(bg='#269928')
w.mainloop()
w2.mainloop()


