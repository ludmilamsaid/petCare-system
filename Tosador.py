from Funcionario import Funcionario
from Gato import Gato
from Cachorro import Cachorro
from Animal import Tamanho
from enum import Enum

class TipoTosa(Enum):
    MAQUINA = "Na máquina"
    TESOURA = "Na tesoura"

class Tosador(Funcionario):
    def __init__(self, nome, ID, valor_tosa, disponivel=False):
        super().__init__(nome, ID, disponivel)
        self.valor_tosa = valor_tosa

def calcular_valor_tosa(self, animal, tipo_tosa):
        valor_base = self.valor_tosa
        if tipo_tosa == TipoTosa.MAQUINA:
            valor_tosa = 65
        elif tipo_tosa == TipoTosa.TESOURA:
            valor_tosa = 75
        valor_base = self.valor_tosa
        fator_tamanho = 1.0
        fator_especie = 1.0

        if animal.tamanho == Tamanho.MINI:
            fator_tamanho = 0.8
        elif animal.tamanho == Tamanho.PEQUENO:
            fator_tamanho = 1.0
        elif animal.tamanho == Tamanho.MEDIO:
            fator_tamanho = 1.2
        elif animal.tamanho == Tamanho.GRANDE:
            fator_tamanho = 1.5

        if isinstance(animal, Cachorro):
            fator_especie = 1.0
        elif isinstance(animal, Gato):
            fator_especie = 0.9

        valor_tosa = valor_base * fator_tamanho * fator_especie
        return valor_tosa

def tosar(self, animal):
        if isinstance(animal, Cachorro) or isinstance(animal, Gato):
            if self.disponivel:
                valor_tosa = self.calcular_valor_tosa(animal)
                print(f"Tosador {self.nome} está tosando o {animal.especie.value} {animal.nome}.")
                print(f"Valor da tosa: R$ {valor_tosa:.2f}")
                animal.tosa()
            else:
                print(f"Tosador {self.nome} não está disponível no momento.")
        else:
            print("O animal fornecido não pode ser tosado por este tosador.")
