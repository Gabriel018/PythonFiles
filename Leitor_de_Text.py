from tkinter import *
import pyttsx3

#pip install pyttx3
#pipi install pywin32

root = Tk()
root.title()
root.geometry("300x300")

def Falar():
  engine = pyttsx3.init()
  volume = engine.getProperty('volume')
  #altera a voz para feminina ou masculina
  voices =  engine.getProperty('voices')
  engine.setProperty('voices', voices [1].id)

  engine.say(Texto.get('1.0',END))
  engine.setProperty('volume', 0.6)

  engine.runAndWait()

Texto = Text(root,font=12,height=10,width=25,border=2)
Texto.pack()

btn = Button(root,text="Falar", command=Falar).pack()

root.mainloop()