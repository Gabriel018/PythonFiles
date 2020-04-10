from tkinter import *
from tkinter import scrolledtext

root = Tk()
root.title("Calculadora Tkinder")
root.geometry("400x400")
root.iconbitmap("c:/PythonFiles/image/calc.ico")


def abrir():
    global Entrada
    global janela
    global M_Label
    janela = Toplevel()
    janela.title("Segunda Janela")
    janela.geometry("400x400")

    Titulo = Label(janela, text="Calculadora Simples", justify="center", font=("Arial", 16)).grid(row=0, column=1,                                                                                             columnspan=3, )

    Entrada = Entry(janela, width=30, borderwidth=6)
    Entrada.grid(row=1, column=0,columnspan=4)

    Btn1 = Button(janela, text="1",padx=30,pady=20, borderwidth=4, command=lambda: Click(1))
    Btn2 = Button(janela, text="2", padx=30,pady=20, borderwidth=4, command=lambda: Click(2))
    Btn3 = Button(janela, text="3", padx=30,pady=20, borderwidth=4, command=lambda: Click(3))
    Btn4 = Button(janela, text="4", padx=30,pady=20, borderwidth=4, command=lambda: Click(4))
    Btn5 = Button(janela, text="5", padx=30,pady=20, borderwidth=4, command=lambda: Click(5))
    Btn6 = Button(janela, text="6", padx=30,pady=20, borderwidth=4, command=lambda: Click(6))
    Btn7 = Button(janela, text="7", padx=30,pady=20, borderwidth=4, command=lambda: Click(7))
    Btn8 = Button(janela, text="8", padx=30,pady=20, borderwidth=4, command=lambda: Click(8))
    Btn9 = Button(janela, text="9", padx=30,pady=20, borderwidth=4, command=lambda: Click(9))
    Btn0 = Button(janela, text="0", padx=30,pady=20, borderwidth=4, command=lambda: Click(0))
    Btn1.grid(row=4, column=0)
    Btn2.grid(row=4, column=1)
    Btn3.grid(row=4, column=2)
    Btn4.grid(row=5, column=0)
    Btn5.grid(row=5, column=1)
    Btn6.grid(row=5, column=2)
    Btn7.grid(row=6, column=0)
    Btn8.grid(row=6, column=1)
    Btn9.grid(row=6, column=2)
    Btn0.grid(row=7, column=0)

    BtnSoma = Button(janela, text="+", padx=30,pady=20, borderwidth=5, command=add)
    BtnMult = Button(janela, text="*", padx=30,pady=20, borderwidth=5, command=mult)
    BtnMenos = Button(janela, text="-", padx=30,pady=20, borderwidth=5, command=sub)
    BtnDiv = Button(janela, text="/", padx=30,pady=20, borderwidth=5,  command=div)
    BtnIgual = Button(janela, text="=", padx=70,pady=20, borderwidth=5,command=igual)

    BtnSoma.grid(row=4, column=3, columnspan=1)
    BtnMult.grid(row=5, column=3)
    BtnMenos.grid(row=6, column=3)
    BtnDiv.grid(row=7, column=3)
    BtnIgual.grid(row=7, column=0, columnspan=4)

Titulo = Label(root,text="Escolha a calculadora desejada", font=("arial", 12)).grid(row=0,column=0,columnspan=3,padx=8)
Bt1 = Button(root, text="Calculadora simples", command=abrir,font=("Arial",12))
Bt1.grid(row=1,column=0,sticky=N,padx=8,pady=8)

Bt2 = Button(root, text="Calculadora Rustica", command="",font=("Arial",12))
Bt2.grid(row=1,column=1,sticky=N,padx=8,pady=8)

def Click(number):
    current = Entrada.get()
    Entrada.delete(0, END)
    Entrada.insert(0, str(current) + str(number))

def add():
    Number_one = Entrada.get()
    global N1
    global math
    math = "addition"
    N1 = int(Number_one)
    Entrada.delete(0, END)


def mult():
    Number_one = Entrada.get()
    global N1
    global math
    math = "Multiplicacion"
    N1 = int(Number_one)
    Entrada.delete(0, END)


def sub():
    Number_one = Entrada.get()
    global N1
    global math
    math = "Subtrair"
    N1 = int(Number_one)
    Entrada.delete(0, END)


def div():
    Number_one = Entrada.get()
    global N1
    global math
    math = "Divisao"
    N1 = int(Number_one)
    Entrada.delete(0, END)


def igual():

    segundo_number = Entrada.get()
    Entrada.delete(0, END)

    if math == "addition":
        Entrada.insert(0, N1 + int(segundo_number))

    if math == "Multiplicacion":
        Entrada.insert(0, N1 * int(segundo_number))

    if math == "Subtrair":
        Entrada.insert(0, N1 - int(segundo_number))

    if math == "Divisao":
        Entrada.insert(0, N1 / int(segundo_number))

root.mainloop()
