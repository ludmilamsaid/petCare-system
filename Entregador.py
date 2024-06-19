from Funcionario import Funcionario
from Cliente import Cliente
from datetime import date
from Animal import Animal
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from Cachorro import Cachorro
from Tamanho import Tamanho

# Definição da classe Entregador que herda de Funcionario
class Entregador(Funcionario):
    # Inicializador da classe Entregador
    def __init__(self, nome: str, ID: int, disponivel: bool=False) -> None:
        super().__init__(nome, ID, disponivel)  # Chama o inicializador da classe base Funcionario
        self.geolocator = Nominatim(user_agent="pet_care")  # Inicializa o geolocator para buscar coordenadas geográficas

    # Método para buscar um animal na casa do cliente
    def buscar(self, animal: Animal, cliente: Cliente) -> None:
        if self.disponivel:  # Verifica se o entregador está disponível
            print(f"Entregador {self.nome} está buscando o {animal.especie.value} {animal.nome}.")
            endereco_clinica = "Rua Reitor Píres Albuquerque, 308, Pampulha, Belo Horizonte, MG, 31270-901"  # Endereço da clínica
            distancia, duracao = self.calcular_distancia_tempo(cliente.endereco, endereco_clinica)  # Calcula a distância e tempo
            duracao_arredondada = round(duracao, 2)
            print(f"Distância até a clínica: {distancia:.2f} km")
            print(f"Tempo estimado de entrega: {duracao_arredondada} minutos")
        else:
            print(f"Entregador {self.nome} não está disponível para buscar animais no momento.")

    # Método para entregar um animal na casa do cliente
    def entregar(self, animal: Animal, cliente: Cliente) -> None:
        if self.disponivel:  # Verifica se o entregador está disponível
            print(f"Entregador {self.nome} está entregando o {animal.especie.value} {animal.nome}.")
            endereco_clinica = "Rua Reitor Píres Albuquerque, 308, Pampulha, Belo Horizonte, MG, 31270-901"  # Endereço da clínica
            distancia, duracao = self.calcular_distancia_tempo(endereco_clinica, cliente.endereco)  # Calcula a distância e tempo
            print(f"Distância até o endereço: {distancia:.2f} km")
            duracao_arredondada = round(duracao, 2)
            print(f"Tempo estimado de entrega: {duracao_arredondada} minutos")
        else:
            print(f"Entregador {self.nome} não está disponível para entregar animais no momento.")

    # Método para calcular a distância e o tempo de viagem entre dois endereços
    def calcular_distancia_tempo(self, origem: str, destino: str) -> tuple:
        origem_location = self.geolocator.geocode(origem)  # Obtém a localização da origem
        destino_location = self.geolocator.geocode(destino)  # Obtém a localização do destino

        if origem_location and destino_location:  # Verifica se ambas as localizações foram encontradas
            origem_coords = (origem_location.latitude, origem_location.longitude)
            destino_coords = (destino_location.latitude, destino_location.longitude)
            distancia = geodesic(origem_coords, destino_coords).km  # Calcula a distância em quilômetros

            velocidade_media = 30  # km/h - velocidade média do entregador
            duracao = ((distancia * 4) / velocidade_media) * 60  # minutos - calcula a duração da viagem
            return distancia, duracao
        else:
            return 0, 0  # Retorna 0, 0 se não for possível calcular a distância e o tempo

# Criação de um objeto Cachorro com valores de exemplo
animal = Cachorro(
    nome="Rex",
    idade=3,
    cor="Marrom",
    tamanho=Tamanho.GRANDE.value,
    cliente=789,
    ID=456,
    data_chegada=date.today(),
    data_saida=date.today(),
    addr_historico=[{"endereco": "Rua Exemplo, 123"}],
    conta=200.0,
    raca="Fila"
)

# Criação de um objeto Cliente com valores de exemplo
cliente = Cliente(
    nome="Maria",
    pet=[animal],  # Inicialmente o cliente tem um animal
    conta=500.0,  # Valor inicial da conta do cliente
    endereco="Rua Apucarana, 11, Ouro Preto, Belo Horizonte, MG",
    ID=789
)

# Criação de um objeto Entregador com valores de exemplo
entregador = Entregador("João", 1, True)

# Realiza a entrega do animal na casa do cliente
entregador.entregar(animal, cliente)
