from tkinter import *

root = Tk()

root.title("MoveCanvas")
root.geometry("800x600")

w = 600
h = 400

x = w//2
y = h//2

My_canvas = Canvas(root,width=w,height=h,bg="white")
My_canvas.pack()

Meu_object = My_canvas.create_oval(x,y,x+10,y+10)

def Esquerda(event):
 x = -10
 y = 0
 My_canvas.move(Meu_object,x,y)

def Direita(event):
 x = +10
 y = 0
 My_canvas.move(Meu_object,x,y)

def Cima(event):
 x = 0
 y = -10
 My_canvas.move(Meu_object,x,y)

def Baixo(event):
 x = 0
 y = +10
 My_canvas.move(Meu_object,x,y)   




root.bind("<Left>",Esquerda)
root.bind("<Right>",Direita)
root.bind("<Up>",Cima)
root.bind("<Down>",Baixo)

root.mainloop()





