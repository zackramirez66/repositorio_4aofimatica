# zoe tanairy ramirez bernal 

from tkinter import *

ventana = Tk()
ventana.geometry("400x200")

canvas = Canvas(ventana, width=400, height=200)
canvas.pack()

circulo = canvas.create_oval(10, 80, 60, 130, fill="blue")

def mover():
    canvas.move(circulo, 5, 0)
    ventana.after(100, mover)

mover()

ventana.mainloop()
