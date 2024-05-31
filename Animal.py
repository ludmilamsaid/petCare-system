from abc import ABC, abstractmethod
from enum import Enum
from datetime import date

class Especie(Enum):
    CACHORRO = "Cachorro"
    GATO = "Gato"

class Tamanho(Enum):
    MINI = "Mini"
    PEQUENO = "Pequeno"
    MEDIO = "Médio"
    GRANDE = "Grande"

class Animal(ABC):
    def __init__(self, nome, idade, especie, cor, tamanho, cliente, ID, data_chegada, data_saida, addr_historico, conta):
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

    def consulta_veterinaria(self):
        pass

    def tosa(self, tosador, TipoTosa):
        pass

    def banho(self, tosador):
        pass