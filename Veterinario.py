from Funcionario import Funcionario
from Animal import Animal
from Animal import Especie

class Veterinario(Funcionario):
    def __init__(self, nome, ID, CRMV: int, disponivel=False):
        super().__init__(nome, ID, disponivel)
        self.CRMV = CRMV

    def prescrever_receita (self, animal):
        print(f"Veterinário {self.nome} está prescrevendo uma receita para o {animal.especie.value} {animal.nome}.")

    def atualizar_historico (self, animal):
        print(f"Veterinário {self.nome} está atualizando o histórico do {animal.especie.value} {animal.nome}.")

    def vacinar (self, animal):
        print(f"Veterinário {self.nome} está vacinando o {animal.especie.value} {animal.nome}.")