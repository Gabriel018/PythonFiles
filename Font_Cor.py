from tkinter import *
from tkinter import font
from tkinter import colorchooser



root = Tk()
root.title("Selecionador de cor")
root.geometry("400x400")



class selecionar():
 def collor():
  cor = colorchooser.askcolor()
  cor_selec = Label(root,text=cor).grid(row=2,column=1)
 lbl = Label(root,text="Escolha um referencia",font=12).grid(row=0,column=1)


 def fontes():
  fonts = list(font.families())
  fonts.sort()

  pagTexto = Text(root, height=50, width=50)
  pagTexto.grid(row=3,column=1)

  posicaoFont = 0

  for item in fonts:
   strPos = str(posicaoFont)

   posicaoFont = posicaoFont + 1

   pagTexto.tag_config(strPos, font=(item, 14))
   pagTexto.insert(END, item, strPos)
   pagTexto.insert(END, "\n")

 btn = Button(root,text="Tipos de Cor", command=collor).grid(row=1,column=0,pady=20)
 btn1 = Button(root,text="Tipos de fonte",command=fontes).grid(row=1,column=2,pady=20)

root.mainloop()