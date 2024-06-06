from Funcionario import Funcionario
from Animal import Tamanho, Especie
from enum import Enum
from datetime import date

class TipoTosa(Enum):
    MAQUINA = "Máquina"
    TESOURA = "Tesoura"

class Tosador(Funcionario):
    def __init__(self, nome: str, ID: int, disponivel: bool = False) -> None:
        super().__init__(nome, ID, disponivel)

    def calcular_valor_tosa_cachorro(self, tamanho: Tamanho, tipo_tosa: TipoTosa) -> float:

        if tipo_tosa == TipoTosa.MAQUINA:
            valor_base = 65
        elif tipo_tosa == TipoTosa.TESOURA:
            valor_base = 75
        else:
            raise ValueError("Tipo de tosa inválido")

        if tamanho == Tamanho.MINI:
            fator_tamanho = 0.8
        elif tamanho == Tamanho.PEQUENO:
            fator_tamanho = 1.0
        elif tamanho == Tamanho.MEDIO:
            fator_tamanho = 1.2
        elif tamanho == Tamanho.GRANDE:
            fator_tamanho = 1.5
        else:
            raise ValueError("Tamanho inválido")

        valor_tosa_cachorro = valor_base * fator_tamanho

        return valor_tosa_cachorro

    def calcular_valor_tosa_gato(self, tamanho: Tamanho, tipo_tosa: TipoTosa) -> float:

        if tipo_tosa == TipoTosa.MAQUINA:
            valor_base = 65
        elif tipo_tosa == TipoTosa.TESOURA:
            valor_base = 75
        else:
            raise ValueError("Tipo de tosa inválido")

        if tamanho == Tamanho.MINI:
            fator_tamanho = 0.8
        elif tamanho == Tamanho.PEQUENO:
            fator_tamanho = 1.0
        elif tamanho == Tamanho.MEDIO:
            fator_tamanho = 1.2
        elif tamanho == Tamanho.GRANDE:
            fator_tamanho = 1.5
        else:
            raise ValueError("Tamanho inválido")

        valor_tosa_gato = valor_base * fator_tamanho * 0.9
        return valor_tosa_gato

    def calcular_valor_banho_cachorro(self, tamanho: Tamanho) -> float:
        
        valor_base = 45

        if tamanho == Tamanho.MINI:
            fator_tamanho = 0.8
        elif tamanho == Tamanho.PEQUENO:
            fator_tamanho = 1.0
        elif tamanho == Tamanho.MEDIO:
            fator_tamanho = 1.2
        elif tamanho == Tamanho.GRANDE:
            fator_tamanho = 1.5

        valor_banho_cachorro = valor_base * fator_tamanho

        return valor_banho_cachorro

    def calcular_valor_banho_gato(self, tamanho: Tamanho) -> float:
        
        valor_base = 45

        if tamanho == Tamanho.MINI:
            fator_tamanho = 0.8
        elif tamanho == Tamanho.PEQUENO:
            fator_tamanho = 1.0
        elif tamanho == Tamanho.MEDIO:
            fator_tamanho = 1.2
        elif tamanho == Tamanho.GRANDE:
            fator_tamanho = 1.5

        valor_banho_gato = valor_base * fator_tamanho * 0.9
        return valor_banho_gato

tosador = Tosador("Pedro", 1, True)

tosador.calcular_valor_banho_cachorro(Tamanho.GRANDE)