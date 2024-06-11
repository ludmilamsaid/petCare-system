from tkinter import *
from Styles import *
from tkinter import messagebox

class PaginaAgendar(Frame):
    def __init__(self, master):
        super().__init__(master, bg="#2E8B57", width=600, height=400, padx=50, pady=50)
        self.title = Label(self, text="Agendar", bg="#2E8B57", fg="#FFFAFA")
        self.title["font"] = ("Verdana", "30", "italic", "bold")
        self.title.grid(row=0, column=0, columnspan=2, pady=20)

        self.pet_var = StringVar(self)
        self.pet_var.set("Selecione o PET")
        self.menu_pet = OptionMenu(self, self.pet_var, "Nome do cachorrinho")
        estilo_menu(self.menu_pet)
        self.menu_pet.grid(row=1, column=0, pady=5, padx=50)

        # Variáveis para armazenar o estado dos checkboxes
        self.servico_banho = BooleanVar()
        self.servico_tosa = BooleanVar()
        self.servico_veterinario = BooleanVar()

        # Checkbuttons para selecionar serviços
        self.checkbox_banho = Checkbutton(self, text="Banho", variable=self.servico_banho, bg="#2E8B57", fg="#FFFAFA")
        self.checkbox_banho.grid(row=2, column=0, pady=5, sticky=W)
        estilo_checkbox(self.checkbox_banho)
        
        self.checkbox_tosa = Checkbutton(self, text="Tosa", variable=self.servico_tosa, bg="#2E8B57", fg="#FFFAFA")
        self.checkbox_tosa.grid(row=3, column=0, pady=5, sticky=W)
        estilo_checkbox(self.checkbox_tosa)

        self.checkbox_veterinario = Checkbutton(self, text="Consulta Veterinária", variable=self.servico_veterinario, bg="#2E8B57", fg="#FFFAFA")
        self.checkbox_veterinario.grid(row=4, column=0, pady=5, sticky=W)
        estilo_checkbox(self.checkbox_veterinario)


        self.valor_vacinas_label = Label(self, text="Valor total das vacinas", bg="#2E8B57", fg="#FFFAFA")
        self.valor_vacinas_label["font"] = ( "10")
        self.valor_vacinas_label.grid(row = 5, column= 0,sticky=W)
        self.valor_vacinas = Entry(self, width=20)
        estilo_entry(self.valor_vacinas)
        self.valor_vacinas.grid(row=5, column=0, pady=5, padx = 170)
        
        
        self.botao_confirmar = Button(self, text="Confirmar", font=("Calibri", 12), width=10, command=self.mostrar_selecoes)
        estilo_botao(self.botao_confirmar)
        self.botao_confirmar.grid(row=6, column=0, padx=10, pady=20)

        self.voltar = Button(self, text="Voltar", font=("Calibri", 12), width=10, command=self.navegar_pagina_principal)
        estilo_botao(self.voltar)
        self.voltar.grid(row=7, column=1, padx=10, pady=20)

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
