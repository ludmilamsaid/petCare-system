from tkinter import *


class PaginaCadastro(Frame):
    def __init__(self, master):
        super().__init__(master, bg="#2E8B57", width=100, height=800, padx =30, pady=200)
        
        #self.container = Frame(master)
        #self.container.pack()
        
        self.label_nome = Label(self, text = "Nome")
        self.label_nome.pack(pady = 10)
        self.entry_nome = Entry (self, width = 50)
        self.entry_nome.pack(pady = 10)
        
        self.label_endereco = Label(self, text = "Endereço")
        self.label_endereco.pack(pady = 10)
        self.entry_endereco = Entry (self, width = 50)                                                                                                                                                                                              
        self.entry_endereco.pack(pady = 10)
        
        self.label_especie = Label(self, text = "Especie")
        self.label_especie.pack(pady = 10)
        self.entry_especie = Entry (self, width = 50)
        self.entry_especie.pack(pady = 10)
        
        self.label_tutor = Label(self, text="Nome do Dono:")
        self.label_tutor.pack(pady=10)
        self.entry_tutor =Entry(self, width=50)  # Definindo a largura do Entry
        self.entry_tutor.pack(pady=5)  # Adicionando espaçamento abaixo do widget
        
        
        self.voltar = Button(self, text="Voltar", font="Calibri", width = 6, command = self.navegar_pagina_principal)
        self.voltar.pack(pady = 10)
        
    def navegar_pagina_principal(self):
        self.master.master.mostrar_pagina("PaginaPrincipal")


  