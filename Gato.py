from enum import Enum
from Animal import Animal
from datetime import date, datetime, timedelta

class Gato(Animal):
    def __init__(self, nome: str, idade: int, raca, cor: str, tamanho: str, cliente: int, ID: int, data_chegada: date, data_saida: date, addr_historico: str, conta: float):
        super().__init__(nome, idade, raca.value, cor, tamanho, cliente, ID, data_chegada, data_saida, addr_historico, conta)
        self.raca = raca

raca = ["Abissínio", "American Curl", "American Shorthair", "American Wirehair", "Angorá Turco", "Australian Mist", "Azul Russo", "Balinês", "Bambino", "Bengal",
        "Bobtail Americano", "Bobtail Japonês", "Bombaim", "British Longhair", "British Shorthair", "Burmês", "Burmilla", "California Spangled", "Chantilly Tiffany",
        "Chartreux", "Chausie", "Colorpoint Shorthair", "Cornish Rex", "Cymric", "Devon Rex", "Donskoy", "Egípcio Mau", "Europeu Comum", "Exótico de Pelo Curto",
        "Havana Brown", "Highlander", "Himalaio", "Khao Manee", "Korat", "Kurilian Bobtail", "LaPerm", "Maine Coon", "Manx", "Munchkin", "Nebelung", "Norueguês da Floresta",
        "Ocicat", "Oriental", "Persa", "Peterbald", "Pixie Bob", "Ragamuffin", "Ragdoll", "Savannah", "Scottish Fold", "Scottish Fold Longhair", "Scottish Straight",
        "Scottish Straight Longhair", "Selkirk Rex", "Selkirk Rex Longhair", "Siamês", "Siberiano", "Singapura", "Snowshoe", "Somali", "Sphynx", "SRD", "Thai", "Tonquinês",
        "Toyger", "Turkish Van", "British Curl", "Chantilly Tiffany Longhair", "Highlander Longhair", "Siberiano Longhair", "Singapura Longhair"]