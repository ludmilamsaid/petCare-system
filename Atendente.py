from Funcionario import Funcionario  # Importa a classe Funcionario do módulo Funcionario
from Animal import Animal, Especie  # Importa as classes Animal, Tamanho e Especie do módulo Animal
from Cliente import Cliente  # Importa a classe Cliente do módulo Cliente
from datetime import date  # Importa a classe date do módulo datetime
from Cachorro import Cachorro  # Importa a classe Cachorro do módulo Cachorro
from Gato import Gato  # Importa a classe Gato do módulo Gato
import sys  # Importa o módulo sys para manipulação de sistema
import os  # Importa o módulo os para manipulação de sistema
sys.path.append(os.path.join(os.path.dirname(__file__), 'Bancos'))  # Adiciona o caminho 'Bancos' ao sys.path
from Bancos.BancoClientes import BancoClientes  # Importa a classe BancoClientes do módulo Bancos.BancoClientes
from Bancos.BancoAnimais import BancoAnimais  # Importa a classe BancoAnimais do módulo Bancos.BancoAnimais
from Bancos.BancoFuncionarios import BancoFuncionarios  # Importa a classe BancoFuncionarios do módulo Bancos.BancoFuncionarios
from Bancos.BancoAgendamentos import BancoAgendamentos, DataHorario  # Importa as classes BancoAgendamentos e DataHorario do módulo Bancos.BancoAgendamentos
from Tamanho import Tamanho
class Atendente(Funcionario):  # Define a classe Atendente que herda da classe Funcionario
    def __init__(self, nome: str, ID: int, disponivel: bool=False) -> None:
        super().__init__(nome, ID, disponivel)  # Chama o construtor da classe base Funcionario
        self.banco_agendamentos = BancoAgendamentos()  # Instancia a classe BancoAgendamentos
        self.banco_clientes = BancoClientes()  # Instancia a classe BancoClientes
        self.banco_animais = BancoAnimais()  # Instancia a classe BancoAnimais
        self.banco_funcionarios = BancoFuncionarios()  # Instancia a classe BancoFuncionarios

    def cadastrarClientes(self, cliente_id: int, cliente_nome: str, cliente_pets: int, cliente_endereco: str, cliente_conta: float) -> None:
        cliente_id = cliente_id 
        cliente_nome = cliente_nome
        cliente_pets = cliente_pets
        cliente_endereco = cliente_endereco  
        cliente_conta = cliente_conta
        
        nova_linha = [cliente_id, cliente_nome, cliente_pets, cliente_endereco, cliente_conta]  # Cria uma nova linha com as informações do cliente
        sucesso = self.banco_clientes.adicionar(nova_linha)  # Adiciona o cliente ao banco de clientes

        if sucesso:
            print(f"Cliente {cliente_nome} cadastrado com sucesso.")  # Mensagem de sucesso ao cadastrar cliente
        else:
            print(f"Erro ao cadastrar o cliente {cliente_nome}.")  # Mensagem de erro ao cadastrar cliente

    def agendar(self, cliente: Cliente, animal: Animal, servico: str, data_horario:str) -> None:
        if not isinstance(data_horario, DataHorario):  # Verifica se data_horario é do tipo DataHorario
            raise ValueError("O data_horario deve ser do tipo horas, dia.")  # Lança um erro se data_horario não for do tipo esperado

        nova_linha = [cliente.nome, animal.nome, servico, data_horario.horario()]  # Cria uma nova linha com as informações do agendamento
        sucesso = self.banco_agendamentos.adicionar(nova_linha)  # Adiciona o agendamento ao banco de agendamentos

        if sucesso:
            print(f"Agendamento para o animal {animal.nome} em {data_horario.horario()} registrado com sucesso.")  # Mensagem de sucesso ao registrar agendamento
        else:
            print(f"Erro ao registrar o agendamento para o animal {animal.nome}.")  # Mensagem de erro ao registrar agendamento

    def getHistorico(self, animal: Animal):  # Método para obter histórico do animal
        print(f"Nenhum histórico encontrado para o animal {animal.nome}.")  # Mensagem padrão indicando que não há histórico

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
                      animal_tamanho, tutor_id, horario_chegada, horario_saida, conta]  # Cria uma nova linha com as informações do animal
        sucesso = self.banco_animais.adicionar(nova_linha)  # Adiciona o animal ao banco de animais

        if sucesso:
            print(f"{sucesso}")  # Imprime o resultado do sucesso
            print(f"Animal {animal_nome} cadastrado com sucesso.")  # Mensagem de sucesso ao cadastrar animal
            return sucesso
        else:
            print(f"Erro ao cadastrar o animal {animal_nome}.")  # Mensagem de erro ao cadastrar animal
            return sucesso

    def cadastrar_funcionario(self, funcionario):  # Método para cadastrar um funcionário
        if not isinstance(funcionario, Funcionario):  # Verifica se funcionario é uma instância da classe Funcionario
            raise ValueError("O parâmetro 'funcionario' deve ser uma instância da classe Funcionario.")  # Lança um erro se não for

        funcionario_id = funcionario.ID
        funcionario_nome = funcionario.nome
        funcionario_disponibilidade = funcionario.disponivel
        
        nova_linha = [funcionario_id, funcionario_nome, funcionario_disponibilidade]  # Cria uma nova linha com as informações do funcionário
        sucesso = self.banco_funcionarios.adicionar(nova_linha)  # Adiciona o funcionário ao banco de funcionários

        if sucesso:
            print(f"Funcionário {funcionario_nome} cadastrado com sucesso.")  # Mensagem de sucesso ao cadastrar funcionário
        else:
            print(f"Erro ao cadastrar o funcionário {funcionario_nome}.")  # Mensagem de erro ao cadastrar funcionário

    def excluirCliente(self, cliente_id: int) -> None:  # Método para excluir um cliente
        sucesso = self.banco_clientes.remover(cliente_id, "ID")  # Remove o cliente do banco de clientes

        if sucesso:
            print(f"Cliente com ID {cliente_id} excluído com sucesso.")  # Mensagem de sucesso ao excluir cliente
        else:
            print(f"Erro ao excluir o cliente com ID {cliente_id}.")  # Mensagem de erro ao excluir cliente

    def excluirFuncionario(self, funcionario_id: int) -> None:  # Método para excluir um funcionário
        sucesso = self.banco_funcionarios.remover(funcionario_id, "ID")  # Remove o funcionário do banco de funcionários

        if sucesso:
            print(f"Funcionário com ID {funcionario_id} excluído com sucesso.")  # Mensagem de sucesso ao excluir funcionário
        else:
            print(f"Erro ao excluir o funcionário com ID {funcionario_id}.")  # Mensagem de erro ao excluir funcionário

    def excluirAnimal(self, animal_id: int) -> None:  # Método para excluir um animal
        sucesso = self.banco_animais.remover(animal_id, "ID")  # Remove o animal do banco de animais

        if sucesso:
            print(f"Animal com ID {animal_id} excluído com sucesso.")  # Mensagem de sucesso ao excluir animal
        else:
            print(f"Erro ao excluir o animal com ID {animal_id}.")  # Mensagem de erro ao excluir animal

# Criação de instâncias para testes
novo_funcionario = Funcionario(1, "Geraldo Magela", True)  # Cria uma instância de Funcionario
atendente1 = Atendente("Jussara", 101, True)  # Cria uma instância de Atendente
#atendente1.cadastrar_funcionario(novo_funcionario)  # Comenta a chamada do método cadastrar_funcionario
#atendente1.cadastrar_animal(520, "Leticia", 3, "Cachorro", "Chihuahua", "Branca", "Mini", 510, date.today(), date.today(),float(0.0))  # Comenta a chamada do método cadastrar_animal
