from tkinter import *
import sqlite3
from tkinter import ttk


class Loja:

  def __init__(self,janela):
      self.root = janela
      self.root.title("Lojas Raizer")
      self.root.geometry("500x500")

      Label(janela,text="Loja Raizer",font="arial",pady=10).grid(row=1,column=2,sticky="E")
      ttk.Button (text="Cadastro de Clientes", command=self.formClient).grid(row=2,column=1,padx=30,pady=30)
      ttk.Button(text="Cadastro de Produtos",command="").grid(row=2,column=3,padx=30,pady=30)

  def formClient(self):
      self.janelaform = Toplevel()
      self.janelaform.title("Formulario Cliente")
      self.janelaform.geometry("400x400")

      Label(self.janelaform,text="Nome ").grid(row=1,column=0)
      Entry(self.janelaform).grid(row=1,column=1)

      Label(self.janelaform, text="Idade ").grid(row=2, column=0)
      Entry(self.janelaform).grid(row=2, column=1)

      Label(self.janelaform, text="Telefone ").grid(row=3, column=0)
      Entry(self.janelaform).grid(row=3, column=1)

      Label(self.janelaform, text="Endereço").grid(row=4, column=0)
      Entry(self.janelaform).grid(row=4, column=1)

      ttk.Button(self.janelaform,text="Salvar").grid(row=5,column=0,pady=20,padx=40)
      ttk.Button(self.janelaform,text="Alterar").grid(row=5,column=1,pady=20,padx=40)
      ttk.Button(self.janelaform,text="Excluir").grid(row=5,columns=2,pady=20,padx=40)

      self.tabela = ttk.Treeview(self.janelaform,height=12,column=2 )
      self.tabela.grid(row=6,columnspan=2)
      self.tabela.heading("#0", text="ID", anchor=CENTER)
      self.tabela.heading("#1", text="Nome", anchor=CENTER)
      self.tabela.heading("#2",text="Telefone",anchor=CENTER)


      self.janelaform.mainloop()

if __name__ == '__main__':
     janela = Tk()
     app = Loja(janela)
     janela.mainloop()
