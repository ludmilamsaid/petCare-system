from tkinter import *
from Styles import *

class PaginaAgendar(Frame):
    def __init__(self, master):
        super().__init__(master, bg="#2E8B57", width=600, height=400, padx=50, pady=50)
        self.title = Label(self, text="Agendar", bg="#2E8B57", fg = "#FFFAFA")
        self.title["font"] = ("Verdana", "30", "italic", "bold")
        self.title.grid(padx=200)
        
        voltar = self.voltar = Button(self, text="Voltar", font=("Calibri", 12), width=10, command=self.navegar_pagina_principal)
        estilo_botao(voltar)
        self.voltar.grid(row=13, column=0, padx=10, pady=20)
        
    def navegar_pagina_principal(self):
        self.master.master.mostrar_pagina("PaginaPrincipal")