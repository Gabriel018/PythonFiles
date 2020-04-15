from tkinter import *

sys = Tk()
sys.title("Calculadora rustica")
sys.geometry("500x500")



Titulo01 = Label(text="Calculadora Rustica", pady=30, font=("Arial", 14)).grid(row=0, column=1, columnspan=2,
                                                                               sticky=N)
labe01 = Label(text="Digite o primeiro numero", font="arial", padx=10).grid(row=1, column=0)
label02 = Label(text="Digite o segundo numero", font="arial").grid(row=2, column=0)

dados1 = Entry(sys, text="1", width=30)
dados1.grid(row=1, column=1)

dados2 = Entry(sys, text="2", width=30)
dados2.grid(row=2, column=1)

label03 = Label(sys, text="Escolhas a operaçao", font=14, pady=30).grid(row=3, column=0, columnspan=3)

opcao = IntVar()
# Radion
soma = Radiobutton(sys, text="+", variable=opcao, font=("arial", 14), value=1).grid(row=4, column=0)
menor = Radiobutton(sys, text="-", variable=opcao, font=("arial", 14), value=2).grid(row=4, column=1)
mult = Radiobutton(sys, text="*", variable=opcao, font=("arial", 14), value=3).grid(row=5, column=0)
divd = Radiobutton(sys, text="/", variable=opcao, font=("arial", 14), value=4).grid(row=5, column=1)

def cal():
 But_escolhido = opcao.get()
 valor1 = float(dados1.get())
 valor2 = float(dados2.get())

 if But_escolhido == 1:
            resultado = valor1 + valor2

 if But_escolhido == 2:
     resultado = valor1 - valor2

 if But_escolhido == 3:
     resultado = valor1 * valor2

 if But_escolhido == 4:
     resultado = valor1 / valor2

 resultadofinal = Entry(sys)
 resultadofinal.grid(row=7, column=1)


 resultadofinal.delete(0, END)
 resultadofinal.insert(0, resultado)

btncalc = Button(sys, text="Calcular", font=("arial", 12), command=cal).grid(row=6, column=0, columnspan=1)

labelResult = Label(sys, text="Resultado", font=("Arial", 13), pady=50).grid(row=7, column=0)

sys.mainloop()
