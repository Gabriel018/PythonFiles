from tkinter import *
from PIL import ImageTk,Image
from tkinter import  filedialog
sys = Tk()
sys.title("Abrindo arquivos")
#sys.iconbitmap("c:/PythonFiles/image/python.ico")

def Arquivo():
    
    sys.filename = filedialog.askopenfilename(initialdir="c:/PythonFiles/image", title="Selecione a imagem",filetypes=(("jpg files", "*.jpg"),("all files","*.*")))
    M_Label = Label(sys,image=sys.filename)
    M_Label.pack()

Btn = Button(sys,text="Imagem",command=Arquivo)
Btn.pack()

sys.mainloop()