from  tkinter import  *
from PIL import ImageTk,Image

sys = Tk()
sys.title="Slider"
sys.iconbitmap("c:/PythonFiles/image/python.ico")
sys.geometry("500x500")

vertical = Scale(sys,from_=0, to=200)
vertical.pack()

def slide():
  M_label = Label(sys, text=horizontal.get()).pack()
  sys.geometry(str(horizontal.get()) +  "x" + str(vertical.get()))
horizontal = Scale(sys, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()
btn = Button(sys, text="click", command=slide).pack()






# def Largura():
#     global M_label
#     M_label = Label(sys, text=Eixo01.get()).pack()
#     sys.geometry(str(Eixo01.get()) + "x500")


#btn = Button(sys,text="Alterar", command=Largura()).pack()





sys.mainloop()