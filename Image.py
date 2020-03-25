from _ast import Lambda
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image")
#root.iconbitmap('c:/Projeto_Teste/photo.ico')
minha_Imag  = ImageTk.PhotoImage(Image.open("image\Boku.jpg"))
minha_Imag2 = ImageTk.PhotoImage(Image.open("image\Boku03.jpg"))
minha_Imag3 = ImageTk.PhotoImage(Image.open("image\Boku02.png"))
minha_Imag4 = ImageTk.PhotoImage(Image.open("image\Kakashi01.jpeg"))
minha_Imag5 = ImageTk.PhotoImage(Image.open("image\Street.png"))

img_list = [minha_Imag, minha_Imag2, minha_Imag3, minha_Imag4,minha_Imag5]

status = Label(root, text="Imagem " + str(img_list) +  "de"  + str(len(img_list)))

M_Label = Label(image=minha_Imag)
M_Label.grid(row=0,column=0,columnspan=3)


def Avanca(image_number):
    global M_Label
    global ButtonVol
    global ButtonPro

    M_Label.grid_forget()
    M_Label = Label(image=img_list[image_number-1])
    ButtonPro = Button(root, text="Avançar",command=lambda : Avanca(image_number+1))
    ButtonVol = Button(root, text="Anterior", command=lambda: Voltar(image_number - 1))



    if  image_number == 5:
        ButtonPro = Button(root,text="Avancar", command=DISABLED)


    M_Label.grid(row=0, column=0, columnspan=3)

    status = Label(root, text="Imagem " +   str(image_number) +  "de"  + str(len(img_list)))
    status.grid(row=2, column=0, columnspan=2)
    ButtonVol.grid(row=1, column=0)
    ButtonPro.grid(row=1, column=1)
    ButtonSair.grid(row=1, column=2)


def Voltar(image_number):
    global M_Label
    global ButtonVol
    global ButtonPro
    M_Label.grid_forget()
    M_Label = Label(image=img_list[image_number - 1])

    ButtonPro = Button(root, text="Avançar", command=lambda: Avanca(image_number + 1))
    ButtonVol = Button(root, text="Anterior", command=lambda: Voltar(image_number - 1))

    if image_number == 1:
        ButtonVol = Button(root,text="Anterior",command=DISABLED)

    status = Label(root, text="Imagem " +   str(image_number) +  "de"  + str(len(img_list)))
    status.grid(row=2, column=0, columnspan=2)

    M_Label.grid(row=0, column=0, columnspan=3)

    ButtonVol.grid(row=1, column=0)
    ButtonPro.grid(row=1, column=1)
    ButtonSair.grid(row=1, column=2)



ButtonVol = Button(root,text="Anterior",command=DISABLED)
ButtonPro = Button(root,text="Avançar", command=lambda : Avanca(2))
ButtonSair = Button(root,text="Sair", command=root.quit)



ButtonVol.grid(row=1,column=0)
ButtonPro.grid(row=1,column=1)
ButtonSair.grid(row=1,column=2)


root.mainloop()
