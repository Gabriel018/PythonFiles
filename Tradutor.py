from tkinter import *
from translate import Translator


#pip install pyopenssl
#Resolve o erro HTTPConnectionPool

root = Tk()
root.title("Tradutor")
root.geometry("600x800")



translator = Translator(to_lang="Portuguese")
traducao = translator.translate("Hi")
dicionario = traducao
lbl = Entry(root,dicionario)
lbl.pack()
lbl2 = Label(root,text=lbl)
lbl2.pack()



root.mainloop()