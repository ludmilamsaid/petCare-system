import sys
import os
from tkinter import *
from Styles import *
sys.path.append(os.path.join(os.path.dirname(__file__), 'Bancos'))
from Bancos.BancoFuncionarios import BancoFuncionarios
from Atendente import Atendente
from Funcionario import Funcionario

class PaginaFuncionarios(Frame):
    def __init__(self, master):
        super().__init__(master, bg="lightblue", width=800, height=600, padx=20, pady=20)
        self.grid(row=0, column=0, sticky="nsew")
        
        self.title = Label(self, text="Status dos Funcionarios", bg="lightblue", fg="#054b9c")
        self.title["font"] = ("Verdana", 30, "italic", "bold")
        self.title.grid(row=0, column=0, columnspan=2, pady=20)
        
        self.label_nome = Label(self, text="Nome:", bg="lightblue", fg="#054b9c", font=("Verdana", 12))
        self.label_nome.grid(row=1, column=0, sticky=W, pady=5)
        self.entry_nome = Entry(self, width=90)
        estilo_entry(self.entry_nome)
        self.entry_nome.grid(row=1, column=1, columnspan=10, pady=5)
        #self.entry_nome.bind("<KeyPress>", self.validar_nome)

        
        self.label_cpf = Label(self, text="CPF:", bg="lightblue", fg="#054b9c", font=("Verdana", 12))
        self.label_cpf.grid(row=2, column=0, sticky=W, pady=5)
        self.entry_cpf = Entry(self, width=20)
        estilo_entry(self.entry_cpf)
        self.entry_cpf.grid(row=2, column=0, columnspan=10,sticky=W, pady=5, padx=60)
        
        self.cadastrar = Button(self, text="Salvar", font=("Calibri", 12), width=10, command = self.salvar_dados)
        estilo_botao(self.cadastrar)
        self.cadastrar.grid(row=2, column=1)
        
        # Banco de dados
        self.banco_funcionarios = BancoFuncionarios()

        # Frame mais externo para exibir os dados dos funcionarios
        self.div = Frame(self, bg="lightblue")
        self.div.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
        
        # Barra de rolagem
        self.canvas = Canvas(self.div, bg="#eff0ed", width=600, height=450)
        self.scrollbar = Scrollbar(self.div, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas, bg="#eff0ed")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Carregar dados dos funcionários
        self.carregar_dados_funcionarios()

        voltar = self.voltar = Button(self, text="Voltar", font=("Calibri", 12), width=10, command=self.navegar_pagina_principal)
        estilo_botao(voltar)
        self.voltar.grid(row=4, column=2, padx=10, pady=0, sticky="w")

        self.atualizar_dados()

    def carregar_dados_funcionarios(self):
        funcionarios_data = self.banco_funcionarios.banco.to_dict(orient="records")

        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
            
        self.funcionario_frames = []
        for funcionario in funcionarios_data:
            funcionario_frame = Frame(self.scrollable_frame, bg="#FFFAFA", bd=2, relief="groove", padx=20, pady=20)
            funcionario_frame.pack(fill="x", pady=10, padx=30)
            
            labels = ["Nome do Funcionario:"]
            for i, detail in enumerate([funcionario["Nome"]]):
                label = Label(funcionario_frame, text=f"{labels[i]} {detail}", bg="#FFFAFA", anchor="w")
                label.pack(fill="x", pady=2)

            status = "Disponível" if funcionario["Disponibilidade"] else "Indisponível"
            label_status = Label(funcionario_frame, text=f"Disponibilidade: {status}", bg="#FFFAFA", anchor="w")
            label_status.pack(fill="x", pady=2)
            self.atualizar_cor_disponibilidade(label_status, status)

            button = Button(funcionario_frame, text="Alterar Disponibilidade", command=lambda f=funcionario, l=label_status: self.alterar_disponibilidade(f, l))
            button.pack(pady=5)

            self.funcionario_frames.append((funcionario_frame, label_status, button))

    def atualizar_cor_disponibilidade(self, label, status):
        if status == "Disponível":
            label.config(fg="green")
        else:
            label.config(fg="red")

    def alterar_disponibilidade(self, funcionario, label_status):
        self.banco_funcionarios.alterar_disponibilidade(funcionario["Nome"])
        novo_status = "Disponível" if not funcionario["Disponibilidade"] else "Indisponível"
        label_status.config(text=f"Disponibilidade: {novo_status}")
        self.atualizar_cor_disponibilidade(label_status, novo_status)
        
    def salvar_dados(self):
        atendente = Atendente("Padrão", 101, True)
        nome_funcionario = self.entry_nome.get()
        cpf_funcionario = self.entry_cpf.get()
        novo_funcionario = Funcionario(cpf_funcionario, nome_funcionario, True)
        atendente.cadastrar_funcionario(novo_funcionario)
        
    #tentiva de atualizar a página a cada 5 segundos
    def atualizar_dados(self):
        self.carregar_dados_funcionarios()
        self.after(5000, self.atualizar_dados)  
        

    def navegar_pagina_principal(self):
        self.master.master.mostrar_pagina("PaginaPrincipal")

if __name__ == "__main__":
    root = Tk()
    root.title("Agendamentos")
    root.geometry("800x600")
    app = PaginaFuncionarios(root)
    root.mainloop()
