# Zack Ramirez Ramirez

from tkinter import *

ventana = Tk()
ventana.geometry("400x400")

canvas = Canvas(ventana, width=400, height=400)
canvas.pack()

cuadro = canvas.create_rectangle(50, 50, 100, 100, fill="green")

def mover():
    canvas.move(cuadro, 0, 5)
    ventana.after(100, mover)

mover()

ventana.mainloop()