from tkinter import *

from PIL import Image, ImageTk

sys = Tk()
sys.title("Check Box")
sys.iconbitmap("c:/PythonFiles/image/python.ico")
sys.geometry("500x500")




def checar():

 M_label = Label (sys, text=var.get()).pack()

var = StringVar()
c = Checkbutton(sys, text="Aceito vender minha alma", variable=var, onvalue="Aceito", offvalue="Recusado")
c.pack()



btn = Button(sys,text="Verificar", command=checar).pack()

sys.mainloop()