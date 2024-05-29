from enum import Enum
from Animal import Animal, Tamanho, Especie
from Tosador import Tosador, TipoTosa
from Cliente import Cliente
from Veterinario import Veterinario
from datetime import date

class Gato(Animal):
    def __init__(self, nome: str, idade: int, cor: str, tamanho: Tamanho, cliente: int, ID: int, data_chegada: date, data_saida: date, addr_historico: str, conta: float, raca: str):
        super().__init__(nome, idade, "Gato", cor, tamanho, cliente, ID, data_chegada, data_saida, addr_historico, conta)
        self.raca = raca

raca = ["Abissínio", "American Curl", "American Shorthair", "American Wirehair", "Angorá Turco", "Australian Mist", "Azul Russo", "Balinês", "Bambino", "Bengal",
        "Bobtail Americano", "Bobtail Japonês", "Bombaim", "British Longhair", "British Shorthair", "Burmês", "Burmilla", "California Spangled", "Chantilly Tiffany",
        "Chartreux", "Chausie", "Colorpoint Shorthair", "Cornish Rex", "Cymric", "Devon Rex", "Donskoy", "Egípcio Mau", "Europeu Comum", "Exótico de Pelo Curto",
        "Havana Brown", "Highlander", "Himalaio", "Khao Manee", "Korat", "Kurilian Bobtail", "LaPerm", "Maine Coon", "Manx", "Munchkin", "Nebelung", "Norueguês da Floresta",
        "Ocicat", "Oriental", "Persa", "Peterbald", "Pixie Bob", "Ragamuffin", "Ragdoll", "Savannah", "Scottish Fold", "Scottish Fold Longhair", "Scottish Straight",
        "Scottish Straight Longhair", "Selkirk Rex", "Selkirk Rex Longhair", "Siamês", "Siberiano", "Singapura", "Snowshoe", "Somali", "Sphynx", "SRD", "Thai", "Tonquinês",
        "Toyger", "Turkish Van", "British Curl", "Chantilly Tiffany Longhair", "Highlander Longhair", "Siberiano Longhair", "Singapura Longhair"]

def tosa(gato: Gato, tosador: Tosador, tipo_tosa: TipoTosa):
    if tosador.disponivel:
        valor_tosa = tosador.valor_tosa * 0.9
        print(f"Tosador {tosador.nome} está tosando o gato {gato.nome}.")
        print(f"Valor da tosa: R$ {valor_tosa:.2f}")
    else:
        print(f"Tosador {tosador.nome} não está disponível no momento.")

def banho(gato: Gato, tosador: Tosador):
    if tosador.disponivel:
        tosador.calcular_valor_banho(Animal)
        valor_banho = tosador.valor_banho * 0.9
        print(f"Tosador {tosador.nome} está dando banho no gato {gato.nome}.")
        print(f"Valor do banho: R$ {valor_banho:.2f}")
    else:
        print(f"Tosador {tosador.nome} não está disponível no momento.")



gato = Gato("Mia", 2, "Branco", Tamanho.PEQUENO, 123, 456, date.today(), date.today(), "Rua Exemplo, 123", 100.0, "Persa")

cliente = Cliente(
        pet=gato,
        conta=500.0,
        endereco="Rua Apucarana, 11, Ouro Preto, Belo Horizonte, MG",
        ID=789
    )

tosador = Tosador("Pedro", 1, 65, 40, True)

tosa(gato, tosador, TipoTosa.MAQUINA)
