#!/usr/bin/env python3

import tkinter
import datetime
window = tkinter.Tk()
canvas = tkinter.Canvas(window)
time = canvas.create_text(140,100,text='' ,fill='red',font=('Arial', 30))

canvas.pack()
while True:
    day_x= datetime.datetime.now()
    day_str = day_x.strftime('%X')
    canvas.itemconfig(time, text=day_str)
    canvas.update()
window.mainloop()
