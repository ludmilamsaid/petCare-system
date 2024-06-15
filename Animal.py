from abc import ABC, abstractmethod
from typing import List
from enum import Enum
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Tosador import TipoTosa, Tosador

class Especie(Enum):
    CACHORRO = "Cachorro"
    GATO = "Gato"

class Tamanho(Enum):
    MINI = "Mini"
    PEQUENO = "Pequeno"
    MEDIO = "Médio"
    GRANDE = "Grande"

class Animal(ABC):
    def __init__(self, 
                 nome: str, 
                 idade: int, 
                 especie: Especie, 
                 cor: str, 
                 tamanho: Tamanho, 
                 cliente: int, 
                 ID: int, 
                 data_chegada: date, 
                 data_saida: date, 
                 addr_historico: str,
                 servicos_prestados: List[str],
                 conta: float = 0.0) -> None:
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.cor = cor
        self.tamanho = tamanho
        self.cliente = cliente
        self.data_chegada = data_chegada
        self.data_saida = data_saida
        self.addr_historico = addr_historico
        self.servicos_prestados = []
        self.conta = conta

    def adicionar_servico(self, servico: str, custo: float) -> None:
        self.servicos_prestados.append((servico, custo))
        self.conta += custo

    @abstractmethod
    def consulta_veterinaria(self) -> None:
        pass

    @abstractmethod
    def tosa(self, tosador: 'Tosador', tipo_tosa: 'TipoTosa') -> None:
        pass

    @abstractmethod
    def banho(self, tosador: 'Tosador') -> None:
        pass