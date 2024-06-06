from typing import List
from Animal import Animal, Tamanho
from datetime import date
from Cachorro import Cachorro
from Tosador import Tosador, TipoTosa

class Cliente:
    def __init__(self, nome: str, pet: List[Animal], conta: float, endereco: str, ID: int) -> None:
        self.nome = nome
        self.pet = pet
        self.conta = conta
        self.endereco = endereco
        self.ID = ID

    def adicionar_animal(self, animal: Animal) -> None:
        self.pet.append(animal)
        self.conta += animal.conta

    def calcular_conta_total(self) -> float:
        return sum(animal.conta for animal in self.pet)

    def conta_total(self) -> None:
        print(f"Conta total do cliente {self.nome}: R$ {self.calcular_conta_total():.2f}")

    def pagar_conta(self, valor: float) -> None:
        self.conta -= valor

animal = Cachorro(
    nome="Rex",
    idade=3,
    cor="Marrom",
    tamanho=Tamanho.GRANDE,
    cliente=123,
    ID=456,
    data_chegada=date.today(),
    data_saida=date.today(),
    addr_historico="Rua Exemplo, 123",
    conta=200.0,
    raca= "Fila"
)

cliente = Cliente(
    nome="Maria",
    pet= [animal],
    conta=500.0,
    endereco="Rua Apucarana, 11, Ouro Preto, Belo Horizonte, MG",
    ID=789
)

cliente.adicionar_animal(animal)
animal.consulta_veterinaria()
tosador = Tosador("Pedro", 1, True)
animal.tosa(tosador, TipoTosa.TESOURA)
cliente.conta_total()