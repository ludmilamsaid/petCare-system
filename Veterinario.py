from Funcionario import Funcionario
from Animal import Animal
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'Bancos'))
from Bancos.Historico import Historico

class Veterinario(Funcionario):
    def __init__(self, nome, ID, CRMV: int, disponivel=False):
        super().__init__(nome, ID, disponivel)
        self.CRMV = CRMV

    def prescrever_receita(self, animal, receita):
        if not isinstance(animal, Animal):
            raise ValueError("O parâmetro 'animal' deve ser uma instância da classe Animal.")
        
        historico = Historico(f"Historicos/{animal.ID}.txt", animal.ID, animal.tutor)
        sucesso = historico.atualizarHistorico(f"Receita prescrita: {receita}")
        
        if sucesso:
            print(f"Veterinário {self.nome} prescreveu uma receita para o animal {animal.nome}.")
        else:
            print(f"Erro ao prescrever receita para o animal {animal.nome}.")

    def atualizar_historico(self, animal, consulta):
        if not isinstance(animal, Animal):
            raise ValueError("O parâmetro 'animal' deve ser uma instância da classe Animal.")
        
        historico = Historico(f"Historicos/{animal.ID}.txt", animal.ID, animal.tutor)
        sucesso = historico.atualizarHistorico(f"Consulta: {consulta}")
        
        if sucesso:
            print(f"Veterinário {self.nome} atualizou o histórico do animal {animal.nome}.")
        else:
            print(f"Erro ao atualizar o histórico do animal {animal.nome}.")

    def vacinar(self, animal, vacina):
        if not isinstance(animal, Animal):
            raise ValueError("O parâmetro 'animal' deve ser uma instância da classe Animal.")
        
        historico = Historico(f"Historicos/{animal.ID}.txt", animal.ID, animal.tutor)
        sucesso = historico.atualizarHistorico(f"Vacina aplicada: {vacina}")
        
        if sucesso:
            print(f"Veterinário {self.nome} vacinou o animal {animal.nome}.")
        else:
            print(f"Erro ao vacinar o animal {animal.nome}.")
