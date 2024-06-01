from tkinter import *
from Cliente import Cliente
from Cachorro import Cachorro, raca_cachorro
from Gato import Gato, raca_gato
from Styles import *
from tkinter import messagebox

from datetime import date


class PaginaCadastro(Frame):
    def __init__(self, master):
        super().__init__(master, bg="#2E8B57", padx=30, pady=30)
        self.grid(row=0, column=0, sticky="nsew")

        self.title = Label(self, text="Cadastro Tutor", bg="#2E8B57", fg="#FFFAFA", font=("Verdana", 30, "italic", "bold"))
        self.title.grid(row=0, column=0, pady=20)
        
        # Form Frame
        self.label_nome = Label(self, text="Nome:", bg="#2E8B57", fg="#FFFAFA", font=("Verdana", 12))
        self.label_nome.grid(row=1, column=0, sticky=W, pady=5)
        self.entry_nome = Entry(self, width=100)
        estilo_entry(self.entry_nome)
        self.entry_nome.grid(row=1, column=0,columnspan=10, pady=5 )
        
        self.label_endereco = Label(self, text="Endereço:", bg="#2E8B57", fg="#FFFAFA", font=("Verdana", 12))
        self.label_endereco.grid(row=2, column=0, sticky=W, pady=5)
        self.entry_endereco = Entry(self, width=100)
        estilo_entry(self.entry_endereco)
        self.entry_endereco.grid(row=2, column=0,columnspan=10, pady=5, padx = 100)
        
        # Formulário PET
        self.title = Label(self, text="Cadastro PET", bg="#2E8B57", fg="#FFFAFA", font=("Verdana", 30, "italic", "bold"))
        self.title.grid(row=6, column=0,pady=20)
        
        self.label_nome_pet = Label(self, text="Nome:", bg="#2E8B57", fg="#FFFAFA", font=("Verdana", 12))
        self.label_nome_pet.grid(row=8, column=0, sticky=W, pady=5)
        self.entry_nome_pet = Entry(self, width=100)
        estilo_entry(self.entry_nome_pet)
        self.entry_nome_pet.grid(row=8, column=0,columnspan= 10, pady=5, padx = 60)
        
        self.label_idade_pet = Label(self, text="Idade:", bg="#2E8B57", fg="#FFFAFA", font=("Verdana", 12))
        self.label_idade_pet.grid(row=9,column= 0, sticky=W,  pady=5)
        self.entry_idade_pet = Entry(self, width=50)
        self.entry_idade_pet.grid(row=9, column=0, pady=5, padx=100)

        self.label_especie_pet = Label(self, text="Espécie:", bg="#2E8B57", fg="#FFFAFA", font=("Verdana", 12))
        self.label_especie_pet.grid(row=9, column=1, columnspan= 10, pady=5)
        
        self.especie_var = StringVar(self)
        self.especie_var.set("Selecione Espécie")  # valor padrão
        self.option_menu_especie_pet = OptionMenu(self, self.especie_var, "Cachorro", "Gato", command=self.atualizar_racas)
        estilo_menu(self.option_menu_especie_pet)
        self.option_menu_especie_pet.grid(row=9, column=1, pady=5, padx = 50)

        self.label_raca_pet = Label(self, text="Raça:", bg="#2E8B57", fg="#FFFAFA", font=("Verdana", 12))
        self.label_raca_pet.grid(row=10, column=0, sticky=W, pady=5)

        self.raca_var = StringVar(self)
        menu = self.option_menu_raca_pet = OptionMenu(self, self.raca_var, "Selecione uma Raça")
        estilo_menu(menu)
        menu.grid(row=10, column=0, pady=5)

        # Button Frame
        voltar = self.voltar = Button(self, text="Voltar", font=("Calibri", 12), width=10, command=self.navegar_pagina_principal)
        estilo_botao(voltar)
        self.voltar.grid(row=13, column=0, padx=10, pady=20)
        salvar = self.salvar = Button(self, text="Salvar", font=("Calibri", 12), width=10, command=self.salvar_dados)
        estilo_botao(salvar)
        self.salvar.grid(row=13, column=1, pady=20)
    
    def atualizar_racas(self, especie):
        if especie == "Cachorro":
            racas = raca_cachorro
        elif especie == "Gato":
            racas = raca_gato
        else:
            racas = []

        menu = self.option_menu_raca_pet["menu"]
        menu.delete(0, "end")

        for raca in racas:
            menu.add_command(label=raca, command=lambda r=raca: self.raca_var.set(r))

        self.raca_var.set("Selecione Raça")

    def navegar_pagina_principal(self):
        self.master.master.mostrar_pagina("PaginaPrincipal")

    def salvar_dados(self):
        cliente_nome = self.entry_nome.get()
        endereco = self.entry_endereco.get()

        pet_nome = self.entry_nome_pet.get()
        pet_idade = int(self.entry_idade_pet.get())
        pet_especie = self.especie_var.get()
        pet_raca = self.raca_var.get()
        
        if not cliente_nome or not endereco or not pet_nome or not pet_idade or not pet_especie or not pet_raca:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return
        
        cor = "Caramelo"  
        tamanho = "MEDIO"
        cliente_id = 1
        pet_id = 1
        conta = 0.0
        data_chegada = date.today()
        data_saida = date.today()
        addr_historico = ""
        
        if pet_especie == "Cachorro":
            pet = Cachorro(pet_nome, pet_idade, pet_raca, cor, tamanho, cliente_id, pet_id, data_chegada, data_saida, addr_historico, conta)
        elif pet_especie == "Gato":
            pet = Gato(pet_nome, pet_idade, pet_raca, cor, tamanho, cliente_id, pet_id, data_chegada, data_saida, addr_historico, conta)
       
        cliente = Cliente(cliente_nome,pet, conta, endereco, cliente_id)
        print(f"Nome Tutor: {cliente.nome} com pet {pet.nome} ({pet.especie}) de raça {pet.raca} cadastrado com sucesso!")
        messagebox.showwarning("Cadastro Salvo", "Cliente e pet cadastrado com sucesso!")
        
if __name__ == "__main__":
    root = Tk()
    root.title("Cadastro de Clientes e Pets")
    root.geometry("800x800")
    PaginaCadastro(root)
    root.mainloop()
