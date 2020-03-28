from tkinter import *
from PIL import ImageTk,Image
from tkinter import  filedialog
sys = Tk()
sys.title("Abrindo arquivos")
sys.iconbitmap("c:/PythonFiles/image/python.ico")
sys.filename = filedialog.askopenfilename(initialdir="c:/PythonFiles/image", title="Selecione a imagem",filetypes=(("jpg files", "*.jpg"),("all files","*.*")))


sys.mainloop()