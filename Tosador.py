from Funcionario import Funcionario
from Animal import Animal, Tamanho, Especie
from enum import Enum
from datetime import date

class TipoTosa(Enum):
    MAQUINA = "Máquina"
    TESOURA = "Tesoura"

class Tosador(Funcionario):
    def __init__(self, nome:str, ID: int, disponivel=False):
        super().__init__(nome, ID, disponivel)

def calcular_valor_tosa_cachorro(tamanho, tipo_tosa) -> float:

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
    print(f"Valor da tosa: R$ {valor_tosa_cachorro:.2f}")

    return valor_tosa_cachorro

def calcular_valor_tosa_gato(tamanho, tipo_tosa) -> float:

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

def calcular_valor_banho_cachorro(tamanho) -> float:
        
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
        print(f"Valor do banho: R$ {valor_banho_cachorro:.2f}")

        return valor_banho_cachorro

def calcular_valor_banho_gato(tamanho) -> float:
        
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


animal = Animal(
    nome="Rex",
    idade=3,
    especie=Especie.CACHORRO,
    cor="Marrom",
    tamanho=Tamanho.GRANDE.value,
    cliente=123,
    ID=456,
    data_chegada=date.today(),
    data_saida=date.today(),
    addr_historico="Rua Exemplo, 123",
    conta=200.0
)

calcular_valor_banho_cachorro(Tamanho.GRANDE)