from tkinter import *
class PaginaPrincipal(Frame):
    def __init__(self, master):
        # Definindo a cor de fundo como amarela, dimensões maiores e espaçamento interno
        super().__init__(master,bg="yellow", width=600, height=400, padx=50, pady=50)  

        self.msg = Label(self, text = "PetCare", bg = "yellow")
        self.msg["font"] = ("Verdana", "20", "italic", "bold")
        self.msg.pack()
        self.botao_cadastrar = Button(self, text = "Cadastrar", command=self.navegar_pagina_cadastro)
        self.botao_cadastrar.pack(pady=10)
        self.botao_agendar = Button(self, text = "Cadastrar", command=self.navegar_pagina_cadastro)
        self.botao_agendar.pack(pady=10)
        self.sair = Button(self, text = "Sair", font = "Calibri", width = 6, command = self.quit)
        self.sair.pack()

    def navegar_pagina_cadastro(self):
        self.master.master.mostrar_pagina("PaginaCadastro")
    def navegar_pagina_agendar(self):
        self.master.master.mostrar_pagina("PaginaAgendar")
    def navegar_pagina_agendamentos(self):
        self.master.master.mostrar_pagina("PaginaAgendamentos")
    def navegar_pagina_principal(self):
        self.master.master.mostrar_pagina("PaginaPrincipal")
    

class PaginaCadastro(Frame):
    def __init__(self, master):
        super().__init__(master, bg="yellow", width=600, height=400, padx=50, pady=50)  
        self.label_nome = Label(self, text = "Nome", width = 20)
        self.label_nome.pack()

        self.label_endereco = Label(self, text = "Endereço", width = 20)
        self.label_endereco.pack()

        self.label_telefone = Label(self, text = "Telefone", width = 20)
        self.label_telefone.pack()
        self.label_pet = Label(self, text = "Pet", width = 20)
        self.label_pet.pack()
        self.botao_salvar = Button(self, text = "Salvar", command=self.navegar_pagina_cadastro)
        self.botao_salvar.pack()
        self.botao_cancelar = Button(self, text = "Cancelar", command=self.navegar_pagina_principal)
        self.botao_cancelar.pack()
        
        



        



class PaginaAgendar(Frame):
    def __init__(self, master):
        super().__init__(master, bg="yellow", width=600, height=400, padx=50, pady=50)  


class PaginaAgendamentos(Frame):
    def __init__(self, master):
        super().__init__(master, bg="yellow", width=600, height=400, padx=50, pady=50)  

# Classe para gerenciar a navegação entre as páginas     
class PetCare(Tk):
    def __init__(self):
        super().__init__()
        self.container = Frame(self, bg="yellow", width=800, height=600)
        self.container.pack(expand=True, fill="both")

        self.paginas = {}

        for Pagina in (PaginaPrincipal, PaginaCadastro):
            pagina = Pagina(self.container)
            self.paginas[Pagina.__name__] = pagina
            pagina.grid(row=0, column=0, sticky="nsew")

        self.mostrar_pagina("PaginaPrincipal")
    def mostrar_pagina(self, pagina_nome):
        pagina = self.paginas[pagina_nome]
        pagina.tkraise()

if __name__ == "__main__":

    root = PetCare()
    root.mainloop() #loop para exibir a tela

