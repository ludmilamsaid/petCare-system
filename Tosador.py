from Funcionario import Funcionario  # Importa a classe Funcionario do módulo Funcionario
from enum import Enum  # Importa a classe Enum para criar enumerações
from Tamanho import Tamanho
# Enumeração para os tipos de tosa
class TipoTosa(Enum):
    MAQUINA = "Máquina"  # Tosa com máquina
    TESOURA = "Tesoura"  # Tosa com tesoura

# Classe Tosador herda de Funcionario
class Tosador(Funcionario):
    # Inicializador da classe Tosador
    def __init__(self, nome: str, ID: int, disponivel: bool = False) -> None:
        super().__init__(nome, ID, disponivel)  # Chama o inicializador da classe pai (Funcionario)

    # Método para calcular o valor da tosa de um cachorro
    def calcular_valor_tosa_cachorro(self, tamanho: Tamanho, tipo_tosa: TipoTosa) -> float:
        # Define o valor base de acordo com o tipo de tosa
        if tipo_tosa == TipoTosa.MAQUINA:
            valor_base = 65
        elif tipo_tosa == TipoTosa.TESOURA:
            valor_base = 75
        else:
            raise ValueError("Tipo de tosa inválido")  # Levanta um erro se o tipo de tosa for inválido

        # Define o fator de multiplicação de acordo com o tamanho do cachorro
        if tamanho == Tamanho.MINI:
            fator_tamanho = 0.8
        elif tamanho == Tamanho.PEQUENO:
            fator_tamanho = 1.0
        elif tamanho == Tamanho.MEDIO:
            fator_tamanho = 1.2
        elif tamanho == Tamanho.GRANDE:
            fator_tamanho = 1.5
        else:
            raise ValueError("Tamanho inválido")  # Levanta um erro se o tamanho for inválido

        # Calcula o valor final da tosa do cachorro
        valor_tosa_cachorro = valor_base * fator_tamanho

        return valor_tosa_cachorro

    # Método para calcular o valor da tosa de um gato
    def calcular_valor_tosa_gato(self, tamanho: Tamanho, tipo_tosa: TipoTosa) -> float:
        # Define o valor base de acordo com o tipo de tosa
        if tipo_tosa == TipoTosa.MAQUINA:
            valor_base = 65
        elif tipo_tosa == TipoTosa.TESOURA:
            valor_base = 75
        else:
            raise ValueError("Tipo de tosa inválido")  # Levanta um erro se o tipo de tosa for inválido

        # Define o fator de multiplicação de acordo com o tamanho do gato
        if tamanho == Tamanho.MINI:
            fator_tamanho = 0.8
        elif tamanho == Tamanho.PEQUENO:
            fator_tamanho = 1.0
        elif tamanho == Tamanho.MEDIO:
            fator_tamanho = 1.2
        elif tamanho == Tamanho.GRANDE:
            fator_tamanho = 1.5
        else:
            raise ValueError("Tamanho inválido")  # Levanta um erro se o tamanho for inválido

        # Calcula o valor final da tosa do gato aplicando um desconto de 10%
        valor_tosa_gato = valor_base * fator_tamanho * 0.9
        return valor_tosa_gato

    # Método para calcular o valor do banho de um cachorro
    def calcular_valor_banho_cachorro(self, tamanho: Tamanho) -> float:
        valor_base = 45  # Define o valor base do banho

        # Define o fator de multiplicação de acordo com o tamanho do cachorro
        if tamanho == Tamanho.MINI:
            fator_tamanho = 0.8
        elif tamanho == Tamanho.PEQUENO:
            fator_tamanho = 1.0
        elif tamanho == Tamanho.MEDIO:
            fator_tamanho = 1.2
        elif tamanho == Tamanho.GRANDE:
            fator_tamanho = 1.5

        # Calcula o valor final do banho do cachorro
        valor_banho_cachorro = valor_base * fator_tamanho

        return valor_banho_cachorro

    # Método para calcular o valor do banho de um gato
    def calcular_valor_banho_gato(self, tamanho: Tamanho) -> float:
        valor_base = 45  # Define o valor base do banho

        # Define o fator de multiplicação de acordo com o tamanho do gato
        if tamanho == Tamanho.MINI:
            fator_tamanho = 0.8
        elif tamanho == Tamanho.PEQUENO:
            fator_tamanho = 1.0
        elif tamanho == Tamanho.MEDIO:
            fator_tamanho = 1.2
        elif tamanho == Tamanho.GRANDE:
            fator_tamanho = 1.5

        # Calcula o valor final do banho do gato aplicando um desconto de 10%
        valor_banho_gato = valor_base * fator_tamanho * 0.9
        return valor_banho_gato

# Criação de uma instância de Tosador
tosador = Tosador("Pedro", 1, True)

# Cálculo do valor do banho para um cachorro de tamanho grande
tosador.calcular_valor_banho_cachorro(Tamanho.GRANDE)
