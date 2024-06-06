from Funcionario import Funcionario
from Cliente import Cliente
from datetime import date
from Animal import Animal, Especie, Tamanho
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from enum import Enum
from Cachorro import Cachorro
from Gato import Gato

class Entregador(Funcionario):
    def __init__(self, nome: str, ID: int, disponivel: bool=False) -> None:
        super().__init__(nome, ID, disponivel)
        self.geolocator = Nominatim(user_agent="pet_care")

    def buscar(self, animal: Animal, cliente: Cliente) -> None:
        if self.disponivel:
            print(f"Entregador {self.nome} está buscando o {animal.especie.value} {animal.nome}.")
            endereco_clinica = "Rua Reitor Píres Albuquerque, 308, Pampulha, Belo Horizonte, MG, 31270-901"
            distancia, duracao = self.calcular_distancia_tempo(cliente.endereco, endereco_clinica)
            duracao_arredondada = round(duracao, 2)
            print(f"Distância até a clínica: {distancia:.2f} km")
            print(f"Tempo estimado de entrega: {duracao_arredondada} minutos")
        else:
            print(f"Entregador {self.nome} não está disponível para buscar animais no momento.")

    def entregar(self, animal: Animal, cliente: Cliente) -> None:
        if self.disponivel:
            print(f"Entregador {self.nome} está entregando o {animal.especie.value} {animal.nome}.")
            endereco_clinica = "Rua Reitor Píres Albuquerque, 308, Pampulha, Belo Horizonte, MG, 31270-901"
            distancia, duracao = self.calcular_distancia_tempo(endereco_clinica, cliente.endereco)
            print(f"Distância até o endereço: {distancia:.2f} km")
            duracao_arredondada = round(duracao, 2)
            print(f"Tempo estimado de entrega: {duracao_arredondada} minutos")
        else:
            print(f"Entregador {self.nome} não está disponível para entregar animais no momento.")

    def calcular_distancia_tempo(self, origem: str, destino: str) -> tuple:
        origem_location = self.geolocator.geocode(origem)
        destino_location = self.geolocator.geocode(destino)

        if origem_location and destino_location:
            origem_coords = (origem_location.latitude, origem_location.longitude)
            destino_coords = (destino_location.latitude, destino_location.longitude)
            distancia = geodesic(origem_coords, destino_coords).km

            velocidade_media = 30  # km/h
            duracao = ((distancia * 4)/ velocidade_media) * 60 # minutos
            return distancia, duracao
        else:
            return 0, 0

animal = Animal(
    nome="Rex",
    idade=3,
    especie=Especie.CACHORRO,
    cor="Marrom",
    tamanho=Tamanho.GRANDE.value,
    cliente= 789,
    ID=456,
    data_chegada=date.today(),
    data_saida=date.today(),
    addr_historico=[{"endereco": "Rua Exemplo, 123"}],
    conta=200.0
)

cliente = Cliente(
    nome="Maria",
    pet= [animal],
    conta=500.0,
    endereco="Rua Apucarana, 11, Ouro Preto, Belo Horizonte, MG",
    ID=789
)

entregador = Entregador("João", 1, True)

entregador.entregar(animal, cliente)