from abc import ABC, abstractmethod
from enum import Enum
from datetime import date
from Tosador import TipoTosa

class Especie(Enum):
    CACHORRO = "Cachorro"
    GATO = "Gato"

class Tamanho(Enum):
    MINI = "Mini"
    PEQUENO = "Pequeno"
    MEDIO = "Médio"
    GRANDE = "Grande"

class Animal(ABC):
    def __init__(self, nome: str, idade: int, especie: Especie, cor: str, tamanho: Tamanho, cliente: int, ID: int, data_chegada: date, data_saida: date, addr_historico: str, conta: float) -> None:
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.cor = cor
        self.tamanho = tamanho
        self.cliente = cliente
        self.ID = ID
        self.data_chegada = data_chegada
        self.data_saida = data_saida
        self.addr_historico = addr_historico
        self.conta = conta

    def consulta_veterinaria(self) -> None:
        pass

    def tosa(self, tosador: int, TipoTosa: TipoTosa) -> None:
        pass

    def banho(self, tosador: int) -> None:
        pass