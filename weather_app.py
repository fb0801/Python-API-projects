import tkinter as tk
import requests
import time


canvas.tk.Tk()
canvas.geomerty("600x500")
canvas.title('Weather app')

f=("poppins", 15, "bold")
t= ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady= 20)
textfield.focus()


label1 = tk.Label(canvas, font = t)
label1.pack()

label2= tk.Label(canvas, font= f)
label2.pack()


canvas.mainloop()
