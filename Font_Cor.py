import tkinter as tk
from tkinter import *
from tkinter import font
import tkinter.colorchooser
import tkinter.messagebox
import sys


Janela  = Tk()
Janela.title("Selecionador")
Janela.geometry("400x400")
txt  = Label(Janela,text="Selecione uma opçao",font=14).grid(row=0,columnspan=2)
def Cor():
    #Mosta as cores disponiveis no sistema
   cor =  tkinter.colorchooser.askcolor()
   selec_cor = Label(Janela,text=cor).grid(row=1,column=2)

def Font():
    Fonts = list(font.families())
    Fonts.sort()


    PagText = Text(Janela,height=50, width=50)
    PagText.grid(row=0,column=1)

    FontPosicao = 0

    for item  in Fonts:
        StrPos = str(FontPosicao)

        FontPosicao = FontPosicao + 1

        PagText.tag_configure(StrPos,font=(item,14))
        PagText.insert(tk.END, item, StrPos)
        PagText.insert(tk.END, "\n")

Button(Janela,text="Selecionar Fonte",command=Font).grid(row=2,column=1)
Button(Janela,text="Selecione a cor",command=Cor).grid(row=2,column=2)


Janela.mainloop()

