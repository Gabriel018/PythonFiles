from tkinter import ttk
from tkinter import *
import sqlite3


class Produto:
    db_name = 'Banco.db'
    def __init__(self, janela):
        self.janela = None
        self.root = janela
        self.root.title('Estoque de Produtos')

        frame = LabelFrame(self.janela, text="Produtos em estoque")
        frame.grid(row=0, column=0, columnspan=2, pady=30)

        Label(frame, text='Nome: ').grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1)

        Label(frame,text='Preço: ').grid(row=2, column=0)
        self.preco = Entry(frame)
        self.preco.grid(row=2,column=1)
        #Messagem
        self.mensagem = Label(text="",fg='blue',font=12)
        self.mensagem.grid(row=3,columnspan=2,sticky = W + E)

        ttk.Button(frame,text="Salvar",command=self.Add).grid(row=3,columnspan=2,sticky=W+E)
        #Table
        self.view = ttk.Treeview(height = 12, column=2)
        self.view.grid(row=4,columnspan=2)
        self.view.heading('#0',text="Nome",anchor=CENTER)
        self.view.heading('#1',text="Preço",anchor=CENTER)

        self.get_info()
    # Connexao
    def connec(self,query,parametro=()):
     with sqlite3.connect(self.db_name) as conn:
      cursor = conn.cursor()
      result = cursor.execute(query,parametro)
      conn.commit()
      return  result
    def get_info(self):
       dados_info = self.view.get_children()
       for element in dados_info:
        self.view.delete(element)
       query = 'SELECT * FROM produtos'
       db_row = self.connec(query)
       for row in db_row:
        self.view.insert('',0,text=row[1],values=row[2])
    def valid(self):
        return len(self.name.get()) !=0 and len(self.preco.get()) !=0

    #Adiciona item
    def Add(self):
      if self.valid():
        query = 'INSERT INTO produtos VALUES(NULL,?,?)'
        parametro = self.name.get(),self.preco.get()
        self.connec(query,parametro)
        self.mensagem['text'] = 'Produto {} adicionado com sucesso'.format(self.name.get())
      else:
          print("Erro em algum campo")

if __name__ == '__main__':
    janela = Tk()
    App = Produto(janela)
    janela.mainloop()
