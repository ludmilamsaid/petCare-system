from Funcionario import Funcionario
from Animal import Animal, Tamanho, Especie
from Cliente import Cliente
from datetime import date
from Cachorro import Cachorro 
from Gato import Gato
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'Bancos'))
from Bancos.BancoClientes import BancoClientes
from Bancos.BancoAgendamentos import BancoAgendamentos, DataHorario

class Atendente(Funcionario):
    def __init__(self, nome: str, ID: int, disponivel: bool=False) -> None:
        super().__init__(nome, ID, disponivel)
        self.banco_agendamentos = BancoAgendamentos()
        self.banco_clientes = BancoClientes()

    def cadastrarClientes(self, cliente_id: int, cliente_nome: str, cliente_pets: int, cliente_endereco: str, cliente_conta: float) -> None:
        cliente_id = cliente.ID 
        cliente_nome = cliente.nome
        cliente_pets = cliente.pets  
        cliente_endereco = cliente.endereco  
        cliente_conta = cliente.conta
        
        nova_linha = [cliente_id, cliente_nome, cliente_pets, cliente_endereco, cliente_conta]
        sucesso = self.banco_clientes.adicionar(nova_linha)

        if sucesso:
            print(f"Cliente {cliente_nome} cadastrado com sucesso.")
        else:
            print(f"Erro ao cadastrar o cliente {cliente_nome}.")
        print(f"Animal {animal.nome} cadastrado para o cliente {cliente.nome}.")

    def agendar(self, cliente: Cliente, animal: Animal, servico: str, data_horario:str) -> None:
        if not isinstance(data_horario, DataHorario):
            raise ValueError("O data_horario deve ser do tipo horas, dia.")

        nova_linha = [cliente.nome, animal.nome, servico, data_horario.horario()]
        sucesso = self.banco_agendamentos.adicionar(nova_linha)

        if sucesso:
            print(f"Agendamento para o animal {animal.nome} em {data_horario.horario()} registrado com sucesso.")
        else:
            print(f"Erro ao registrar o agendamento para o animal {animal.nome}.")

    def getHistorico(self, animal: Animal):
        print(f"Nenhum histórico encontrado para o animal {animal.nome}.")

    def cadastrar_animal(self, animal_id: int, animal_nome: str, animal_idade: int, animal_especie: Especie, animal_raca: str, animal_cor: str, animal_tamanho: Tamanho, tutor_id: int, horario_chegada: date, horario_saida: date, conta: float) -> None:
        animal_id = animal.ID  
        animal_nome = animal.nome
        animal_idade = animal.idade  
        animal_especie = animal.especie
        animal_raca = animal.raca
        animal_cor = animal.cor
        animal_tamanho = animal.tamanho  
        tutor_id = cliente.ID
        horario_chegada = animal.horario_chegada
        horario_saida = animal.horario_saida
        conta = animal.conta
        
        nova_linha = [animal_id, animal_nome, animal_idade, animal_especie, animal_raca, animal_cor, 
                      animal_tamanho, tutor_id, horario_chegada, horario_saida, "", conta]
        sucesso = self.banco_animais.adicionar(nova_linha)

        if sucesso:
            print(f"Animal {animal_nome} cadastrado com sucesso.")
        else:
            print(f"Erro ao cadastrar o animal {animal_nome}.")


cliente = Cliente(
    nome="Ana",
    pet=Animal,
    conta=500.0,
    endereco="Rua Apucarana, 11, Ouro Preto, Belo Horizonte, MG",
    ID=123
)

animal = Cachorro(
    nome="Rex",
    idade=3,
    cor="Marrom",
    tamanho=Tamanho.GRANDE.value,
    cliente=123,
    ID=456,
    data_chegada=date.today(),
    data_saida=date.today(),
    addr_historico="Rua Exemplo, 123",
    conta=200.0,
    raca= "Fila"
)

atendente1 = Atendente("Jussara", 101, True)
atendente1.agendar(cliente, animal, "Tosa", DataHorario("12h30", "12/06"))