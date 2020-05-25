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

        Label(frame, text='Preço: ').grid(row=2, column=0)
        self.preco = Entry(frame)
        self.preco.grid(row=2, column=1)
        # Messagem
        self.mensagem = Label(text="", fg='blue', font=12)
        self.mensagem.grid(row=3, columnspan=2, sticky=W + E)
        # Buttons
        ttk.Button(text="DELETE", command=self.delete).grid(row=5, column=0, sticky=W + E)
        ttk.Button(text="Editar", command=self.edit).grid(row=5, column=1, sticky=W + E)
        ttk.Button(frame, text="Salvar", command=self.Add).grid(row=3, columnspan=2, sticky=W + E)
        # Table
        self.view = ttk.Treeview(height=12, column=2)
        self.view.grid(row=4, columnspan=2)
        self.view.heading('#0', text="Nome", anchor=CENTER)
        self.view.heading('#1', text="Preço", anchor=CENTER)

        self.get_info()

    # Connexao
    def connec(self, query, parametro= ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parametro)
            conn.commit()
            return result
            # retorna informaçao

    def get_info(self):
        dados_info = self.view.get_children()
        for element in dados_info:
            self.view.delete(element)
        query = 'SELECT * FROM produtos'
        db_row = self.connec(query)
        for row in db_row:
            self.view.insert('', 0, text=row[1], values=row[2])

    def valid(self):
        return len(self.name.get()) != 0 and len(self.preco.get()) != 0

    # Adiciona item
    def Add(self):
        if self.valid():
            query = 'INSERT INTO produtos VALUES(NULL,?,?)'
            parametro = self.name.get(), self.preco.get()
            self.connec(query, parametro)
            self.mensagem['text'] = 'Produto {} adicionado com sucesso'.format(self.name.get())
        else:
            print("Erro em algum campo")
        self.get_info()

    def delete(self):
        self.view.item(self.view.selection()), ['text']
        Nome = self.view.item(self.view.selection())['text']
        query = "DELETE FROM produtos WHERE Nome = ?"
        self.connec(query, (Nome,))
        self.mensagem['text'] = "Produto{} deletado".format(Nome)
        self.get_info()

    def edit(self):
        name = self.view.item(self.view.selection())['text']
        old_price = self.view.item(self.view.selection())['values'][0]
        self.edit_janela = Toplevel()
        self.edit_title = "Editar Produto"
        # Nome atual
        Label(self.edit_janela, text="Nome atual").grid(row=1, column=0)
        Entry(self.edit_janela, textvariable=StringVar(self.edit_janela, value= name), state="readonly").grid(row=1,
                                                                                                             column=1)
        # Valor atual
        Label(self.edit_janela, text="Valor atual").grid(row=2, column=0)
        Entry(self.edit_janela, textvariable=StringVar(self.edit_janela, value= old_price), state="readonly").grid(row=2,
                                                                                                                  column=1)
        # novo nome
        Label(self.edit_janela, text="Novo nome").grid(row=3, column=0)
        novo_nome = Entry(self.edit_janela)
        novo_nome.grid(row = 3, column = 1)
        # novo valor
        Label(self.edit_janela, text="Novo valor").grid(row=4, column=0)
        novo_valor = Entry(self.edit_janela)
        novo_valor.grid(row=4, column=1)

        Button(self.edit_janela, text='Alterar',command = lambda: self.edit_grava(novo_nome.get(), name, novo_valor.get(), old_price)).grid(row=4, column=2, sticky=W)

        self.edit_janela.mainloop()

    def edit_grava(self, novo_nome, name, novo_valor, old_price):
        query = 'UPDATE produtos SET Nome = ?, Preco = ? WHERE Nome = ? AND Preco = ? '
        parametro = (novo_nome, name, novo_valor, old_price)
        self.connec(query, parametro)
        self.edit_janela.destroy()
        self.mensagem['text'] = 'Record {} updated successfylly'.format(novo_nome)

        self.get_info()


if __name__ == '__main__':
    janela = Tk()
    App = Produto(janela)
    janela.mainloop()
