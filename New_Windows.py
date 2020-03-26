from tkinter import *
from PIL import ImageTk,Image

sys = Tk()
sys.title("Nova Janela")
sys.iconbitmap("c:/PythonFiles/image/python.ico")

def abrir():
    global M_Label
    global Image00
    top = Toplevel()
    top.title("Nova Janela")
    top.iconbitmap("c:/PythonFiles/image/python.ico")
    Image00 = ImageTk.PhotoImage(Image.open("image\Boku02.png"))
    M_Label = Label(top, image=Image00, ).pack()

Botao = Button(sys,text="Abrir",command=abrir).pack()

sys.mainloop()