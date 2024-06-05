from Funcionario import Funcionario
from Animal import Animal
from Animal import Especie

class Veterinario(Funcionario):
    def __init__(self, nome: str, ID: int, CRMV: int, disponivel: bool=False) -> None:
        super().__init__(nome, ID, disponivel)
        self.CRMV = CRMV

    def prescrever_receita (self, animal: int) -> str:
        print(f"Veterinário {self.nome} está prescrevendo uma receita para o {animal.especie.value} {animal.nome}.")

    def atualizar_historico (self, animal: int) -> str:
        print(f"Veterinário {self.nome} está atualizando o histórico do {animal.especie.value} {animal.nome}.")

    def vacinar (self, animal: int) -> str:
        print(f"Veterinário {self.nome} está vacinando o {animal.especie.value} {animal.nome}.")