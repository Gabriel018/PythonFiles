from tkinter import *
from PIL import ImageTk,Image
from tkinter import  filedialog
sys = Tk()
sys.title("Abrindo arquivos")
sys.iconbitmap("c:/PythonFiles/image/python.ico")

def Arquivo():
    global  M_Label
    sys.filename = filedialog.askopenfilename(initialdir="c:/PythonFiles/image", title="Selecione a imagem",filetypes=(("jpg files", "*.jpg"),("all files","*.*")))
    M_Label = Label(sys,text=sys.filename).pack()

Btn = Button(sys,text="Arquivo",command=Arquivo).pack()

sys.mainloop()