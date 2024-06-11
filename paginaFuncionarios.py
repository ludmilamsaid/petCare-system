from tkinter import *
from Styles import *

class PaginaFuncionarios(Frame):
    def __init__(self, master):
        super().__init__(master, bg="#2E8B57", width=800, height=600, padx=20, pady=20)
        self.grid(row=0, column=0, sticky="nsew")
        
        self.title = Label(self, text="Status dos Funcionarios", bg="#2E8B57", fg="#FFFAFA")
        self.title["font"] = ("Verdana", 30, "italic", "bold")
        self.title.grid(row=0, column=0, columnspan=2, pady=20)

        # Frame mais externo para exibir os dados dos funcionarios
        self.div = Frame(self, bg="lightblue")
        self.div.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        
        # Barra de rolagem
        self.canvas = Canvas(self.div, bg="lightblue", width=600, height=500)
        self.scrollbar = Scrollbar(self.div, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas, bg="lightblue")

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

        # Dados fictícios para teste
        self.funcionarios_data = [
            ["Lucas Maciel", "Disponível"],
            ["Barbara Reis", "Indisponível"],
            ["Claudia Assunção", "Disponível"],
            ["Thiago Galvão", "Indisponível"],
            ["Sabrina Lemos", "Disponível"],
        ]

        # Adicionando dados dos funcionarios na página
        self.funcionario_frames = []
        for funcionario in self.funcionarios_data:
            funcionario_frame = Frame(self.scrollable_frame, bg="#FFFAFA", bd=2, relief="groove", padx=20, pady=20)
            funcionario_frame.pack(fill="x", pady=10, padx=30)
            
            labels = ["Nome do Funcionario:"]
            for i, detail in enumerate(funcionario[:1]):
                label = Label(funcionario_frame, text=f"{labels[i]} {detail}", bg="#FFFAFA", anchor="w")
                label.pack(fill="x", pady=2)

            self.label_status = Label(funcionario_frame, text=f"Disponibilidade: {funcionario[1]}", bg="#FFFAFA", anchor="w")
            self.label_status.pack(fill="x", pady=2)
            self.atualizar_cor_disponibilidade(self.label_status, funcionario[1])

            button = Button(funcionario_frame, text="Alterar Disponibilidade", command=lambda f=funcionario, l=self.label_status: self.alterar_disponibilidade(f, l))
            button.pack(pady=5)

            self.funcionario_frames.append((funcionario_frame, self.label_status, button))

        voltar = self.voltar = Button(self, text="Voltar", font=("Calibri", 12), width=10, command=self.navegar_pagina_principal)
        estilo_botao(voltar)
        self.voltar.grid(row=2, column=0, padx=10, pady=20, sticky="w")

    def atualizar_cor_disponibilidade(self, label, status):
        if status == "Disponível":
            label.config(fg="green")
        else:
            label.config(fg="red")

    def alterar_disponibilidade(self, funcionario, label_status):
        if funcionario[1] == "Disponível":
            funcionario[1] = "Indisponível"
        else:
            funcionario[1] = "Disponível"
        label_status.config(text=f"Disponibilidade: {funcionario[1]}")
        self.atualizar_cor_disponibilidade(label_status, funcionario[1])

    def navegar_pagina_principal(self):
        self.master.master.mostrar_pagina("PaginaPrincipal")

if __name__ == "__main__":
    root = Tk()
    root.title("Agendamentos")
    root.geometry("800x600")
    app = PaginaFuncionarios(root)
    root.mainloop()
