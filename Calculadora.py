from tkinter import *


sys = Tk()
sys.title("Calculdora")
sys.iconbitmap("c:/PythonFiles/image/python.ico")
sys.geometry("500x500")
sys.grid()






Titulo = Label(sys,text="Calculadora Simples",justify="center", font=("Arial",16)).grid(row=0,column=1,columnspan=3,)
Titulo02 = Label(sys,text="Digite o numero",font=("Italico",14)).grid(row=2,column=1)

Entrada = Entry(sys,width=40,borderwidth=6)
Entrada.grid(row=3,column=1)

def Click(number):
    current = Entrada.get()
    Entrada.delete(0,END)
    Entrada.insert(0,str(current) + str(number))

def add():
   Number_one = Entrada.get()
   global N1
   global math
   math = "addition"
   N1  = int(Number_one)
   Entrada.delete(0,END)
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
    Entrada.delete(0,END)

    if math == "addition":
     Entrada.insert(0,N1 + int(segundo_number))


    if math == "Multiplicacion":
     Entrada.insert(0,N1 * int(segundo_number))

    if math == "Subtrair":
     Entrada.insert(0,N1 - int(segundo_number))

    if math == "Divisao":
     Entrada.insert(0,N1 / int(segundo_number))



#Botoes
Btn1 = Button(sys,text="1",padx=40,pady=20,borderwidth=4,command=lambda : Click(1))
Btn2 = Button(sys,text="2",padx=40,pady=20,borderwidth=4,command=lambda : Click(2))
Btn3 = Button(sys,text="3",padx=40,pady=20,borderwidth=4,command=lambda : Click(3))
Btn4 = Button(sys,text="4",padx=40,pady=20,borderwidth=4,command=lambda : Click(4))
Btn5 = Button(sys,text="5",padx=40,pady=20,borderwidth=4,command=lambda : Click(5))
Btn6 = Button(sys,text="6",padx=40,pady=20,borderwidth=4,command=lambda : Click(6))
Btn7 = Button(sys,text="7",padx=40,pady=20,borderwidth=4,command=lambda : Click(7))
Btn8 = Button(sys,text="8",padx=40,pady=20,borderwidth=4,command=lambda : Click(8))
Btn9 = Button(sys,text="9",padx=40,pady=20,borderwidth=4,command=lambda : Click(9))
Btn0 = Button(sys,text="0",padx=40,pady=20,borderwidth=4,command=lambda : Click(0))

BtnSoma = Button(sys,text="+",padx=40,pady=20,borderwidth=6,font=("Arial",12),command=add)
BtnMult = Button(sys,text="*",padx=40,pady=20,borderwidth=6,font=("Arial",12),command=mult)
BtnMenos = Button(sys,text="-",padx=40,pady=20,borderwidth=6,font=("Arial",12),command=sub)
BtnDiv = Button(sys,text="/",padx=40,pady=20,borderwidth=6,font=("Arial",12),command=div)
BtnIgual = Button(sys,text="=",padx=60,pady=20,borderwidth=6,font=("Arial",12),command=igual)

#Grid Buttoes
Btn1.grid(row=4,column=0)
Btn2.grid(row=4,column=1)
Btn3.grid(row=4,column=2)

Btn4.grid(row=5,column=0,)
Btn5.grid(row=5,column=1)
Btn6.grid(row=5,column=2)

Btn7.grid(row=6,column=0)
Btn8.grid(row=6,column=1)
Btn9.grid(row=6,column=2)
Btn0.grid(row=7,column=0)

BtnSoma.grid(row=4,column=4,columnspan=1)
BtnMult.grid(row=5,column=4,)
BtnMenos.grid(row=6,column=4,)
BtnDiv.grid(row=7,column=4)
BtnIgual.grid(row=7,column=0,columnspan=3)


sys.mainloop()