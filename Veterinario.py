from Funcionario import Funcionario  # Importa a classe Funcionario do módulo Funcionario
from Animal import Animal  # Importa a classe Animal do módulo Animal
import sys  # Importa o módulo sys para manipulação de sistema
import os  # Importa o módulo os para funcionalidades relacionadas ao sistema operacional
sys.path.append(os.path.join(os.path.dirname(__file__), 'Bancos'))  # Adiciona o diretório 'Bancos' ao path do sistema
from Bancos.Historico import Historico  # Importa a classe Historico do módulo Bancos.Historico

# Classe Veterinario que herda da classe Funcionario
class Veterinario(Funcionario):
    # Inicializador da classe Veterinario
    def __init__(self, nome, ID, CRMV: int, disponivel=False):
        super().__init__(nome, ID, disponivel)  # Chama o inicializador da classe pai (Funcionario)
        self.CRMV = CRMV  # Atribui o CRMV ao veterinário

    # Método para prescrever uma receita para um animal
    def prescrever_receita(self, animal, receita):
        if not isinstance(animal, Animal):
            raise ValueError("O parâmetro 'animal' deve ser uma instância da classe Animal.")
        
        # Cria uma instância de Historico para o animal com o ID correspondente
        historico = Historico(f"Historicos/{animal.ID}.txt", animal.ID, animal.tutor)
        sucesso = historico.atualizarHistorico(f"Receita prescrita: {receita}")  # Atualiza o histórico com a receita
        
        # Verifica se a atualização foi bem sucedida e imprime uma mensagem apropriada
        if sucesso:
            print(f"Veterinário {self.nome} prescreveu uma receita para o animal {animal.nome}.")
        else:
            print(f"Erro ao prescrever receita para o animal {animal.nome}.")

    # Método para atualizar o histórico de consulta de um animal
    def atualizar_historico(self, animal, consulta):
        if not isinstance(animal, Animal):
            raise ValueError("O parâmetro 'animal' deve ser uma instância da classe Animal.")
        
        # Cria uma instância de Historico para o animal com o ID correspondente
        historico = Historico(f"Historicos/{animal.ID}.txt", animal.ID, animal.tutor)
        sucesso = historico.atualizarHistorico(f"Consulta: {consulta}")  # Atualiza o histórico com a consulta
        
        # Verifica se a atualização foi bem sucedida e imprime uma mensagem apropriada
        if sucesso:
            print(f"Veterinário {self.nome} atualizou o histórico do animal {animal.nome}.")
        else:
            print(f"Erro ao atualizar o histórico do animal {animal.nome}.")

    # Método para vacinar um animal e registrar no histórico
    def vacinar(self, animal, vacina):
        if not isinstance(animal, Animal):
            raise ValueError("O parâmetro 'animal' deve ser uma instância da classe Animal.")
        
        # Cria uma instância de Historico para o animal com o ID correspondente
        historico = Historico(f"Historicos/{animal.ID}.txt", animal.ID, animal.tutor)
        sucesso = historico.atualizarHistorico(f"Vacina aplicada: {vacina}")  # Atualiza o histórico com a vacina aplicada
        
        # Verifica se a atualização foi bem sucedida e imprime uma mensagem apropriada
        if sucesso:
            print(f"Veterinário {self.nome} vacinou o animal {animal.nome}.")
        else:
            print(f"Erro ao vacinar o animal {animal.nome}.")
