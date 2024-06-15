from tkinter import Tk, Frame
from paginaPrincipal import PaginaPrincipal
from paginaCadastro import PaginaCadastro
from paginaAgendar import PaginaAgendar
from paginaAgendamentos import PaginaAgendamentos
from paginaFuncionarios import PaginaFuncionarios

class PetCare(Tk):
    def __init__(self):
        super().__init__()
        self.container = Frame(self, bg="#2E8B57", width=1000, height=800)
        self.container.pack(expand=True, fill="both")
        
        self.paginas = {}

        for Pagina in (PaginaPrincipal, PaginaCadastro, PaginaAgendar, PaginaAgendamentos, PaginaFuncionarios):
            pagina = Pagina(self.container)
            self.paginas[Pagina.__name__] = pagina
            pagina.grid(row=0, column=0, sticky="nsew")

        self.mostrar_pagina("PaginaPrincipal")

    def mostrar_pagina(self, pagina_nome):
        pagina = self.paginas[pagina_nome]
        pagina.tkraise()

if __name__ == "__main__":
    root = PetCare()
    root.mainloop()
