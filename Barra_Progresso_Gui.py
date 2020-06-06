from tkinter import *
from tkinter import  ttk
from tkinter import messagebox
import  time

root = Tk()
root.title("Barra de progresso")
root.geometry("500x500")

def Progresso():
 for x in range(5):
   lbl.config(text=progresso['value'])
   progresso['value'] +=20
   root.update_idletasks()
   time.sleep(1)

   if progresso['value'] == 100:
     messagebox.showinfo("Comcluido","Comcluido com sucesso!!")

   if progresso['value'] == 100:
     root.destroy()
 #Barra de progresso
progresso  = ttk.Progressbar(root,orient=HORIZONTAL,length=400,mode="determinate")
progresso.pack(pady=30)


bnt = Button(root,text="Tranferir", command=Progresso)
bnt.pack(pady=30)

lbl = Label(root,text="")
lbl.pack()

root.mainloop()
