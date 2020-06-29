from tkinter import *

sys = Tk()
sys.title("DropMenu")
sys.iconbitmap("c:/PythonFiles/image/python.ico")
sys.geometry("500x500")

def mostrar():
    M_Label = Label(sys, text=seleciona.get()).pack()

Cidades = [
        "Acrelândia",
        "Assis Brasil",
        "Brasiléia",
        "Bujari",
        "Capixaba",
        "Cruzeiro do Sul",
        "Epitaciolândia",
        "Feijó"
]
seleciona = StringVar()
seleciona.set(Cidades[0])
Estados = OptionMenu(sys, seleciona,*Cidades)
Estados.pack()

btn = Button(sys, text="Mostrar", command=mostrar)
btn.pack()

sys.mainloop()