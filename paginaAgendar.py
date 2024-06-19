from tkinter import *
from Styles import *
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'Bancos'))
from Bancos.BancoAnimais import BancoAnimais
from Atendente import Atendente
from Bancos.BancoClientes import BancoClientes

class PaginaAgendar(Frame):
    def __init__(self, master):
        super().__init__(master, bg="lightblue", width=600, height=400, padx=200, pady=50)
        self.title = Label(self, text="Agendar", bg="lightblue", fg="#054b9c")
        self.title["font"] = ("Verdana", "30", "italic", "bold")
        self.title.grid(row=0, column=0, columnspan=2, pady=20)

        self.div = Frame(self, bg="lightblue")
        self.div.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        
        self.pet_var = StringVar(self.div)
        self.pet_var.set("Selecione o PET")
        
        self.menu_pet = OptionMenu(self.div, self.pet_var, "")
        estilo_menu(self.menu_pet)
        self.menu_pet.grid(row=1, column=0, pady=5, padx=50)
        
        self.carregar_dados_pets()

        self.servico_banho = BooleanVar()
        self.servico_tosa = BooleanVar()
        self.servico_veterinario = BooleanVar()

        # Checkbuttons para selecionar serviços
        self.checkbox_banho = Checkbutton(self.div, text="Banho", variable=self.servico_banho, bg="#2E8B57", fg="#FFFAFA")
        self.checkbox_banho.grid(row=2, column=0, pady=5, sticky=W)
        estilo_checkbox(self.checkbox_banho)
        
        self.checkbox_tosa = Checkbutton(self.div, text="Tosa", variable=self.servico_tosa, bg="#2E8B57", fg="#FFFAFA")
        self.checkbox_tosa.grid(row=3, column=0, pady=5, sticky=W)
        estilo_checkbox(self.checkbox_tosa)

        self.checkbox_veterinario = Checkbutton(self.div, text="Consulta Veterinária", variable=self.servico_veterinario, bg="#2E8B57", fg="#FFFAFA")
        self.checkbox_veterinario.grid(row=4, column=0, pady=5, sticky=W)
        estilo_checkbox(self.checkbox_veterinario)

        self.valor_vacinas_label = Label(self.div, text="Valor total das vacinas:", bg="lightblue", fg="#054b9c")
        self.valor_vacinas_label["font"] = ("Arial", 12, "bold")
        self.valor_vacinas_label.grid(row=5, column=0, sticky=W)
        self.valor_vacinas = Entry(self.div, width=20)
        estilo_entry(self.valor_vacinas)
        self.valor_vacinas.grid(row=5, column=0, pady=5, padx=183)
        
        self.total_label = Label(self.div, text= "Total a ser pago:", bg="lightblue", fg="#054b9c" )
        self.total_label["font"] = ("Arial", 12, "bold")
        self.total_label.grid(row=6, column=0, sticky=W,pady=5)
        
        self.botao_confirmar = Button(self, text="Confirmar", font=("Calibri", 12), width=10, command=self.mostrar_selecoes)
        estilo_botao(self.botao_confirmar)
        self.botao_confirmar.grid(row=7, column=1, padx=40, pady=20)
        
         
        self.voltar = Button(self, text="Voltar", font=("Calibri", 12), width=10, command=self.navegar_pagina_principal)
        estilo_botao(self.voltar)
        self.voltar.grid(row=7, column=1, padx=50, sticky=W, pady=20)

    def carregar_dados_pets(self):
        banco_clientes = BancoClientes()
        banco_animais = BancoAnimais()
        clientes_data = banco_clientes.banco.values.tolist()
        pets_data = banco_animais.banco.values.tolist()
        
        clientes_dict = {cliente[0]: cliente[1] for cliente in clientes_data}
        
        self.pets = []
        for pet in pets_data:
            if pet[7] in clientes_dict:
                self.pets.append(f"Tutor: {clientes_dict[pet[7]]} - Pet: {pet[1]}")
            else:
                self.pets.append(f"Pet: {pet[1]} (Sem tutor)")

        menu = self.menu_pet["menu"]
        menu.delete(0, "end")
        for pet in self.pets:
            menu.add_command(label=pet, command=lambda value=pet: self.pet_var.set(value))
        
    def navegar_pagina_principal(self):
        self.master.master.mostrar_pagina("PaginaPrincipal")

    def mostrar_selecoes(self):
        selecoes = []
        if self.servico_banho.get():
            selecoes.append("Banho")
        if self.servico_tosa.get():
            selecoes.append("Tosa")
        if self.servico_veterinario.get():
            selecoes.append("Consulta Veterinária")
        
        resultado = "Serviços selecionados: " + ", ".join(selecoes)
        messagebox.showinfo("Seleções", resultado)

# Janela para fazer teste
if __name__ == "__main__":
    root = Tk()
    root.title("Sistema PetCare")
    pagina = PaginaAgendar(root)
    pagina.pack(expand=True, fill=BOTH)
    root.mainloop()
