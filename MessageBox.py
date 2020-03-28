from tkinter import *
from tkinter import messagebox


sys = Tk()
sys.title("MessagemBox")
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def menssage():
 msg = messagebox.showinfo("Alerta","Sistema Atualizado")
 Label(sys,text=msg,comand=messagebox)

btn = Button(sys,text="Atualizar sistema",command=menssage).pack()

sys.mainloop()