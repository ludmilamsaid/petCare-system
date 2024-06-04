from tkinter import *
from Styles import *

class PaginaAgendamentos(Frame):
    def __init__(self, master):
        super().__init__(master, bg="#2E8B57", width=800, height=600, padx=20, pady=20)
        self.grid(row=0, column=0, sticky="nsew")
        
        
        self.title = Label(self, text="Agendamentos", bg="#2E8B57", fg="#FFFAFA")
        self.title["font"] = ("Verdana", 30, "italic", "bold")
        self.title.grid(row=0, column=0, columnspan=2, pady=20)

        # Frame mais externo para exibir os dados dos pets
        self.div = Frame(self, bg="lightblue")
        self.div.grid(row=1, column=1,padx=10, pady=10, sticky="nsew")
        
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
        pets_data = [
            ["Rex", "3", "Labrador", "João", "Grande", "99999-9999", "Rua A, 123"],
            ["Mimi", "2", "Persa", "Maria", "Pequeno", "88888-8888", "Rua B, 456"],
            ["Bobby", "5", "Poodle", "Carlos", "Médio", "77777-7777", "Rua C, 789"],
            ["Luna", "1", "Golden Retriever", "Ana", "Grande", "66666-6666", "Rua D, 101"],
            ["Thor", "4", "Bulldog", "Pedro", "Médio", "55555-5555", "Rua E, 202"],
           
        ]

        # Adicionando dados dos pets na página
        for pet in pets_data:
            pet_frame = Frame(self.scrollable_frame, bg="#FFFAFA", bd=2, relief="groove", padx=20, pady=20 )
            pet_frame.pack(fill="x", pady=10, padx=30)

            labels = ["Nome do Pet:", "Idade:", "Raça:", "Tutor:", "Tamanho:", "Telefone:", "Endereço:"]
            for i, detail in enumerate(pet):
                label = Label(pet_frame, text=f"{labels[i]} {detail}", bg="#FFFAFA", anchor="w")
                label.pack(fill="x", pady=2)

        
        voltar = self.voltar = Button(self, text="Voltar", font=("Calibri", 12), width=10, command=self.navegar_pagina_principal)
        estilo_botao(voltar)
        self.voltar.grid(row=2, column=0, padx=10, pady=20, sticky="w")

    def navegar_pagina_principal(self):
        self.master.master.mostrar_pagina("PaginaPrincipal")

if __name__ == "__main__":
    root = Tk()
    root.title("Agendamentos")
    root.geometry("800x600")
    app = PaginaAgendamentos(root)
    root.mainloop()
