from tkinter import *
import pyttsx3

#pip install pyttx3
#pipi install pywin32

root = Tk()
root.title()
root.geometry("200x200")

def Falar():
  engine = pyttsx3.init()
  engine.say(Texto.get())

  engine.runAndWait()

Texto = Entry(root,font=12)
Texto.pack()

btn = Button(root,text="Falar", command=Falar).pack()

root.mainloop()