from enum import Enum
from Animal import Animal, Especie
from Tosador import Tosador, TipoTosa

from datetime import date
from Tamanho import Tamanho
# Classe Gato herda da classe Animal
class Gato(Animal):
    # Inicializador da classe Gato
    def __init__(self, nome: str, idade: int, cor: str, tamanho: Tamanho, cliente: int, ID: int, data_chegada: date, data_saida: date, addr_historico: str, conta: float, raca: str) -> None:
        # Chama o inicializador da classe pai (Animal)
        super().__init__(nome, idade, Especie.GATO, cor, tamanho, cliente, ID, data_chegada, data_saida, addr_historico, conta)
        self.raca = raca  # Define o atributo raça

    # Método para realizar uma consulta veterinária
    def consulta_veterinaria(self) -> None:
        print(f"Consulta veterinária para o gato {self.nome}.")  # Imprime mensagem de consulta veterinária
        self.adicionar_servico("Consulta Veterinária", 100.0)  # Adiciona o serviço de consulta veterinária ao histórico do gato

    # Método para realizar a tosa do gato
    def tosa(self, tosador: Tosador, tipo_tosa: TipoTosa) -> None:
        if tosador.disponivel:  # Verifica se o tosador está disponível
            valor_tosa = tosador.calcular_valor_tosa_gato(self.tamanho, tipo_tosa)  # Calcula o valor da tosa
            print(f"Tosador {tosador.nome} está tosando o gato {self.nome}.")  # Imprime mensagem indicando o início da tosa
            print(f"Valor da tosa: R$ {valor_tosa:.2f}")  # Imprime o valor da tosa
            self.adicionar_servico("Tosa", valor_tosa)  # Adiciona o serviço de tosa ao histórico do gato
        else:
            print(f"Tosador {tosador.nome} não está disponível no momento.")  # Imprime mensagem caso o tosador não esteja disponível

    # Método para realizar o banho do gato
    def banho(self, tosador: Tosador) -> None:
        if tosador.disponivel:  # Verifica se o tosador está disponível
            valor_banho = tosador.calcular_valor_banho_gato(self.tamanho)  # Calcula o valor do banho
            print(f"Tosador {tosador.nome} está dando banho no gato {self.nome}.")  # Imprime mensagem indicando o início do banho
            print(f"Valor do banho: R$ {valor_banho:.2f}")  # Imprime o valor do banho
            self.adicionar_servico("Banho", valor_banho)  # Adiciona o serviço de banho ao histórico do gato
        else:
            print(f"Tosador {tosador.nome} não está disponível no momento.")  # Imprime mensagem caso o tosador não esteja disponível

# Lista de raças de gato
raca_gato = [
    "Abissínio", "American Curl", "American Shorthair", "American Wirehair", "Angorá Turco", "Australian Mist",
    "Azul Russo", "Balinês", "Bambino", "Bengal", "Bobtail Americano", "Bobtail Japonês", "Bombaim", "British Longhair",
    "British Shorthair", "Burmês", "Burmilla", "California Spangled", "Chantilly Tiffany", "Chartreux", "Chausie",
    "Colorpoint Shorthair", "Cornish Rex", "Cymric", "Devon Rex", "Donskoy", "Egípcio Mau", "Europeu Comum",
    "Exótico de Pelo Curto", "Havana Brown", "Highlander", "Himalaio", "Khao Manee", "Korat", "Kurilian Bobtail",
    "LaPerm", "Maine Coon", "Manx", "Munchkin", "Nebelung", "Norueguês da Floresta", "Ocicat", "Oriental", "Persa",
    "Peterbald", "Pixie Bob", "Ragamuffin", "Ragdoll", "Savannah", "Scottish Fold", "Scottish Fold Longhair",
    "Scottish Straight", "Scottish Straight Longhair", "Selkirk Rex", "Selkirk Rex Longhair", "Siamês", "Siberiano",
    "Singapura", "Snowshoe", "Somali", "Sphynx", "SRD", "Thai", "Tonquinês", "Toyger", "Turkish Van", "British Curl",
    "Chantilly Tiffany Longhair", "Highlander Longhair", "Siberiano Longhair", "Singapura Longhair"
]

# Criação de uma instância de Gato
animal1 = Gato(
    nome="Mia",
    idade=2,
    cor="Branco",
    tamanho=Tamanho.PEQUENO,
    cliente=124,
    ID=455,
    data_chegada=date.today(),
    data_saida=date.today(),
    addr_historico="Rua Exemplo, 123",
    conta=200.0,
    raca="Persa"
)

# Criação de uma instância de Tosador
tosador = Tosador("Pedro", 1, True)

# Realização da tosa do gato usando o método tosa da classe Gato
Gato.tosa(animal1, tosador, TipoTosa.MAQUINA)
