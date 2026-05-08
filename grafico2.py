# Zack Ramirez Ramirez

from tkinter import *

ventana = Tk()
ventana.geometry("300x300")

canvas = Canvas(ventana, width=300, height=300)
canvas.pack()

canvas.create_rectangle(50, 50, 250, 250, fill="red")

ventana.mainloop()