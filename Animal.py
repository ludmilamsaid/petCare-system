from abc import ABC, abstractmethod # Importação da biblioteca abc para definir classes abstratas e métodos abstratos
from typing import List # Importação da biblioteca typing para usar tipagem de listas
from enum import Enum # Importação da biblioteca enum para definir enumerações
from datetime import date # Importação da biblioteca datetime para manipular datas
from Tosador import TipoTosa, Tosador # Importação das classes TipoTosa e Tosador

class Especie(Enum): # Classe Enum definindo as espécies aceitas
    CACHORRO = "Cachorro"
    GATO = "Gato"

class Tamanho(Enum): # Classe Enum definindo os tamanhos aceitos
    MINI = "Mini"
    PEQUENO = "Pequeno"
    MEDIO = "Médio"
    GRANDE = "Grande"

class Animal(ABC): # Classe abstrata Animal, que serve como base para outras classes de animais
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
        self.nome = nome # Nome do animal
        self.idade = idade # Idade do animal
        self.especie = especie # Espécie do animal, utilizando a Enum Especie
        self.cor = cor # Cor do animal
        self.tamanho = tamanho # Tamanho do animal, utilizando a Enum Tamanho
        self.cliente = cliente # ID do cliente (tutor) do animal
        self.data_chegada = data_chegada # Data de chegada do animal
        self.data_saida = data_saida # Data de saída do animal
        self.addr_historico = addr_historico # Endereço do histórico do animal
        self.servicos_prestados = [] # Lista de serviços prestados ao animal
        self.conta = conta # Conta corrente do animal

    def adicionar_servico(self, servico: str, custo: float) -> None:
        self.servicos_prestados.append((servico, custo)) # Adiciona o serviço prestado à lista de serviços
        self.conta += custo # Atualiza o valor da conta do animal

    @abstractmethod
    def consulta_veterinaria(self) -> None: # Método abstrato para consultas veterinárias
        pass

    @abstractmethod
    def tosa(self, tosador: 'Tosador', tipo_tosa: 'TipoTosa') -> None: # Método abstrato para tosa
        pass

    @abstractmethod
    def banho(self, tosador: 'Tosador') -> None: # Método abstrato para banho
        pass
