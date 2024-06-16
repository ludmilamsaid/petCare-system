from Funcionario import Funcionario
from Animal import Animal, Tamanho, Especie
from Cliente import Cliente
from datetime import date
from Cachorro import Cachorro 
from Gato import Gato
from Funcionario import Funcionario
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'Bancos'))
from Bancos.BancoClientes import BancoClientes
from Bancos.BancoAnimais import BancoAnimais
from Bancos.BancoFuncionarios import BancoFuncionarios
from Bancos.BancoAgendamentos import BancoAgendamentos, DataHorario

class Atendente(Funcionario):
    def __init__(self, nome: str, ID: int, disponivel: bool=False) -> None:
        super().__init__(nome, ID, disponivel)
        self.banco_agendamentos = BancoAgendamentos()
        self.banco_clientes = BancoClientes()
        self.banco_animais = BancoAnimais()
        self.banco_funcionarios = BancoFuncionarios()

    def cadastrarClientes(self, cliente_id: int, cliente_nome: str, cliente_pets: int, cliente_endereco: str, cliente_conta: float) -> None:
        cliente_id = cliente_id 
        cliente_nome = cliente_nome
        #mudei cliente.pets para cliente.pet
        cliente_pets = cliente_pets 
        cliente_endereco = cliente_endereco  
        cliente_conta = cliente_conta
        
        nova_linha = [cliente_id, cliente_nome, cliente_pets, cliente_endereco, cliente_conta]
        sucesso = self.banco_clientes.adicionar(nova_linha)

        if sucesso:
            print(f"Cliente {cliente_nome} cadastrado com sucesso.")
        else:
            print(f"Erro ao cadastrar o cliente {cliente_nome}.")

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

    def cadastrar_animal(self, animal_id: int, animal_nome: str, animal_idade: int, animal_especie: Especie, animal_raca: str, animal_cor: str, animal_tamanho: Tamanho, tutor_id: int, horario_chegada: date, horario_saida: date, conta: float) -> bool:
        animal_id = animal_id  
        animal_nome = animal_nome
        animal_idade = animal_idade  
        animal_especie = animal_especie
        animal_raca = animal_raca
        animal_cor = animal_cor
        animal_tamanho = animal_tamanho  
        tutor_id = tutor_id
        horario_chegada = horario_chegada
        horario_saida = horario_saida
        conta = conta
        
        nova_linha = [animal_id, animal_nome, animal_idade, animal_especie, animal_raca, animal_cor, 
                      animal_tamanho, tutor_id, horario_chegada, horario_saida, conta]
        sucesso = self.banco_animais.adicionar(nova_linha)

        if sucesso:
            print(f"{sucesso}")
            print(f"Animal {animal_nome} cadastrado com sucesso.")
            return sucesso
        else:
            print(f"Erro ao cadastrar o animal {animal_nome}.")
            return sucesso
    def cadastrar_funcionario(self, funcionario):
        if not isinstance(funcionario, Funcionario):
            raise ValueError("O parâmetro 'funcionario' deve ser uma instância da classe Funcionario.")
        
        funcionario_id = funcionario.ID
        funcionario_nome = funcionario.nome
        funcionario_disponibilidade = funcionario.disponivel
        
        nova_linha = [funcionario_id, funcionario_nome, funcionario_disponibilidade]
        sucesso = self.banco_funcionarios.adicionar(nova_linha)

        if sucesso:
            print(f"Funcionário {funcionario_nome} cadastrado com sucesso.")
        else:
            print(f"Erro ao cadastrar o funcionário {funcionario_nome}.")

    def excluirCliente(self, cliente_id: int) -> None:
        sucesso = self.banco_clientes.remover(cliente_id, "ID")

        if sucesso:
            print(f"Cliente com ID {cliente_id} excluído com sucesso.")
        else:
            print(f"Erro ao excluir o cliente com ID {cliente_id}.")

    def excluirFuncionario(self, funcionario_id: int) -> None:
        sucesso = self.banco_funcionarios.remover(funcionario_id, "ID")

        if sucesso:
            print(f"Funcionário com ID {funcionario_id} excluído com sucesso.")
        else:
            print(f"Erro ao excluir o funcionário com ID {funcionario_id}.")

    def excluirAnimal(self, animal_id: int) -> None:
        sucesso = self.banco_animais.remover(animal_id, "ID")

        if sucesso:
            print(f"Animal com ID {animal_id} excluído com sucesso.")
        else:
            print(f"Erro ao excluir o animal com ID {animal_id}.")




novo_funcionario = Funcionario(1, "Geraldo Magela", True)
atendente1 = Atendente("Jussara", 101, True)
#atendente1.cadastrar_funcionario(novo_funcionario)
#atendente1.cadastrar_animal(520, "Leticia", 3, "Cachorro", "Chihuahua", "Branca", "Mini", 510, date.today(), date.today(),float(0.0))