from enum import Enum
from Animal import Animal, Tamanho, Especie
from Tosador import Tosador, TipoTosa
from Cliente import Cliente
from Veterinario import Veterinario
from datetime import date

class Gato(Animal):
    def __init__(self, nome: str, idade: int, cor: str, tamanho: Tamanho, cliente: int, ID: int, data_chegada: date, data_saida: date, addr_historico: str, conta: float, raca: str):
        super().__init__(nome, idade, Especie.GATO, cor, tamanho, cliente, ID, data_chegada, data_saida, addr_historico, conta)
        self.raca = raca

raca = ["Abissínio", "American Curl", "American Shorthair", "American Wirehair", "Angorá Turco", "Australian Mist", "Azul Russo", "Balinês", "Bambino", "Bengal",
        "Bobtail Americano", "Bobtail Japonês", "Bombaim", "British Longhair", "British Shorthair", "Burmês", "Burmilla", "California Spangled", "Chantilly Tiffany",
        "Chartreux", "Chausie", "Colorpoint Shorthair", "Cornish Rex", "Cymric", "Devon Rex", "Donskoy", "Egípcio Mau", "Europeu Comum", "Exótico de Pelo Curto",
        "Havana Brown", "Highlander", "Himalaio", "Khao Manee", "Korat", "Kurilian Bobtail", "LaPerm", "Maine Coon", "Manx", "Munchkin", "Nebelung", "Norueguês da Floresta",
        "Ocicat", "Oriental", "Persa", "Peterbald", "Pixie Bob", "Ragamuffin", "Ragdoll", "Savannah", "Scottish Fold", "Scottish Fold Longhair", "Scottish Straight",
        "Scottish Straight Longhair", "Selkirk Rex", "Selkirk Rex Longhair", "Siamês", "Siberiano", "Singapura", "Snowshoe", "Somali", "Sphynx", "SRD", "Thai", "Tonquinês",
        "Toyger", "Turkish Van", "British Curl", "Chantilly Tiffany Longhair", "Highlander Longhair", "Siberiano Longhair", "Singapura Longhair"]

def tosa(self, tosador, tipo_tosa):
        if tosador.disponivel:
                valor_tosa = tosador.calcular_valor_tosa_gato(self.tamanho, tipo_tosa)
                print(f"Tosador {tosador.nome} está tosando o gato {self.nome}.")
                print(f"Valor da tosa: R$ {valor_tosa:.2f}")
        else:
                print(f"Tosador {tosador.nome} não está disponível no momento.")

def banho(self, tosador):
        if tosador.disponivel:
                valor_banho = tosador.calcular_valor_banho_gato(self.tamanho)
                print(f"Tosador {tosador.nome} está dando banho no gato {self.nome}.")
                print(f"Valor do banho: R$ {valor_banho:.2f}")
        else:
                print(f"Tosador {tosador.nome} não está disponível no momento.")


animal1 = Animal(
    nome="Mia",
    idade=2,
    especie=Especie.GATO,
    cor="Branco",
    tamanho=Tamanho.PEQUENO,
    cliente=124,
    ID=455,
    data_chegada=date.today(),
    data_saida=date.today(),
    addr_historico="Rua Exemplo, 123",
    conta=200.0
)

tosador = Tosador("Pedro", 1, True)

tosa(animal1, tosador, TipoTosa.MAQUINA)
