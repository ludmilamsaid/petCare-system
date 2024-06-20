from tkinter import *

class PaginaPrincipal(Frame):
    def __init__(self, master):
       
        # Inicialização do frame principal com configurações de cor e tamanho
        super().__init__(master, bg="lightblue", width=100, height=800, padx=300, pady=150)  

        self.title = Label(self, text="PetCare", bg="lightblue", fg = "#054b9c")
        self.title["font"] = ("Verdana", "50", "italic", "bold")
        self.title.pack(pady=30)
         # Carregando a imagem
        self.logo_image = PhotoImage(file="logo_petcare.png") 
        self.logo_image = self.logo_image.subsample(4)
        # Criando um rótulo para exibir a imagem
        self.logo_label = Label(self, image=self.logo_image)
        self.logo_label.pack(side = LEFT, padx=10)
        
        self.botao_cadastrar = Button(self, text="Cadastrar", width= 15, command = self.navegar_pagina_cadastro)
        self.botao_cadastrar.pack(pady=10)

        self.botao_agendar = Button(self, text="Agendar",width= 15, command = self.navegar_pagina_agendar)
        self.botao_agendar.pack(pady=10)
        
        self.botao_agendamentos = Button(self, text="Agendamentos", width= 15,command = self.navegar_pagina_agendamentos)
        self.botao_agendamentos.pack(pady=10)
        
        self.botao_funcionarios = Button(self, text="Funcionarios", width= 15,command = self.navegar_pagina_funcionarios)
        self.botao_funcionarios.pack(pady=10)

        self.sair = Button(self, text="Sair", font="Calibri", width = 6, command = self.quit)
        self.sair.pack(pady=10)

    # Métodos de navegação para diferentes páginas
    def navegar_pagina_cadastro(self):
        self.master.master.mostrar_pagina("PaginaCadastro")

    def navegar_pagina_agendar(self):
        self.master.master.mostrar_pagina("PaginaAgendar")

    def navegar_pagina_agendamentos(self):
        self.master.master.mostrar_pagina("PaginaAgendamentos")
    def navegar_pagina_funcionarios(self):
        self.master.master.mostrar_pagina("PaginaFuncionarios")