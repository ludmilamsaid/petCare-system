from Funcionario import Funcionario
from Animal import Animal, Tamanho, Especie
from Cliente import Cliente
from datetime import date
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'Bancos'))
from Bancos.BancoClientes import BancoClientes
from Bancos.BancoAgendamentos import BancoAgendamentos, DataHorario

class Atendente(Funcionario):
    def __init__(self, nome, ID, disponivel=False):
        super().__init__(nome, ID, disponivel)
        self.banco_agendamentos = BancoAgendamentos()
        self.banco_clientes = BancoClientes()

    def cadastrarClientes(self, cliente_id, cliente_nome, cliente_pets, cliente_endereco, cliente_conta):
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

    def agendar(self, cliente, animal, servico, data_horario):
        if not isinstance(data_horario, DataHorario):
            raise ValueError("O data_horario deve ser do tipo horas, dia.")

        nova_linha = [cliente.nome, animal.nome, servico, data_horario.horario()]
        sucesso = self.banco_agendamentos.adicionar(nova_linha)

        if sucesso:
            print(f"Agendamento para o animal {animal.nome} em {data_horario.horario()} registrado com sucesso.")
        else:
            print(f"Erro ao registrar o agendamento para o animal {animal.nome}.")

    def getHistorico(self, animal):
        print(f"Nenhum histórico encontrado para o animal {animal.nome}.")


cliente1 = Cliente(
    nome="Ana",
    pet=Animal,
    conta=500.0,
    endereco="Rua Apucarana, 11, Ouro Preto, Belo Horizonte, MG",
    ID=123
)

animal1 = Animal(
    nome="Rex",
    idade=3,
    especie=Especie.CACHORRO,
    cor="Marrom",
    tamanho=Tamanho.GRANDE.value,
    cliente=123,
    ID=456,
    data_chegada=date.today(),
    data_saida=date.today(),
    addr_historico="Rua Exemplo, 123",
    conta=200.0
)

atendente1 = Atendente("Jussara", 101, True)
atendente1.agendar(cliente1, animal1, "Tosa", DataHorario("12h30", "12/06"))