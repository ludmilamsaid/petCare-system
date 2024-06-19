import sys
import os
from tkinter import *
from Styles import *
sys.path.append(os.path.join(os.path.dirname(__file__), 'Bancos'))
from Atendente import Atendente
from Bancos.BancoAnimais import BancoAnimais

class PaginaAgendamentos(Frame):
    def __init__(self, master):
        super().__init__(master, bg="lightblue", width=800, height=600, padx=20, pady=20)
        self.grid(row=0, column=0, sticky="nsew")
        
        
        self.title = Label(self, text="Prontuário Veterinário", bg="lightblue", fg="#054b9c")
        self.title["font"] = ("Verdana", 30, "italic", "bold")
        self.title.grid(row=0, column=0, columnspan=2, pady=20)

        # Frame mais externo para exibir os dados dos pets
        self.div = Frame(self, bg="lightblue")
        self.div.grid(row=1, column=1, pady=10, sticky="nsew")
        
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
        
        voltar = self.voltar = Button(self, text="Voltar", font=("Calibri", 12), width=10, command=self.navegar_pagina_principal)
        estilo_botao(voltar)
        self.voltar.grid(row=2, column=2, padx=10, pady=20, sticky="w")
        self.carregar_dados_pets()

    def carregar_dados_pets(self):
        banco_animais = BancoAnimais()
        pets_data = banco_animais.banco.values.tolist()

        labels = ["ID", "Nome", "Idade", "Espécie", "Raça", "Cor", "Tamanho", "Tutor", "Horário Chegada", "Horário Saída", "Endereço Histórico", "Conta"]

        # Adicionando dados dos pets na página
        for pet in pets_data:
            pet_frame = Frame(self.scrollable_frame, bg="#FFFAFA", bd=2, relief="groove", padx=20, pady=20 )
            pet_frame.pack(fill="x", pady=10, padx=30)

            for i, detail in enumerate(pet):
                label = Label(pet_frame, text=f"{labels[i]}: {detail}", bg="#FFFAFA", anchor="w")
                label.pack(fill="x", pady=2)
                
            label_status = Label(pet_frame, text="Status do Pet:", bg="#FFFAFA")
            label_status.pack(fill="x", pady=2)
        
            #deletar = Button(pet_frame, text="Deletar")
            deletar = Button(pet_frame, text="Deletar", command=lambda pet_id=pet[0]: self.deletar_dados(pet_id))

            #estilo_botao(deletar)
            deletar.pack()
        
    def deletar_dados(self, pet_id):
        atendente = Atendente("Padrão", 101, True)
        atendente.excluirAnimal(pet_id)
           
    def navegar_pagina_principal(self):
        self.master.master.mostrar_pagina("PaginaPrincipal")

if __name__ == "__main__":
    root = Tk()
    root.title("Agendamentos")
    root.geometry("800x600")
    app = PaginaAgendamentos(root)
    root.mainloop()
