from typing import List
from Animal import Animal, Tamanho
from datetime import date
from Cachorro import Cachorro
from Tosador import Tosador, TipoTosa

# Definição da classe Cliente
class Cliente:
    # Inicializador da classe Cliente
    def __init__(self, nome: str, pet: List[Animal], conta: float, endereco: str, ID: int) -> None:
        self.nome = nome  # Nome do cliente
        self.pet = pet  # Lista de animais do cliente
        self.conta = conta  # Valor total da conta do cliente
        self.endereco = endereco  # Endereço do cliente
        self.ID = ID  # ID do cliente

    # Método para adicionar um animal ao cliente
    def adicionar_animal(self, animal: Animal) -> None:
        self.pet.append(animal)  # Adiciona o animal à lista de pets do cliente
        self.conta += animal.conta  # Atualiza o valor da conta do cliente com o valor da conta do animal

    # Método para calcular a conta total do cliente
    def calcular_conta_total(self) -> float:
        return sum(animal.conta for animal in self.pet)  # Retorna a soma das contas de todos os animais do cliente

    # Método para imprimir a conta total do cliente
    def conta_total(self) -> None:
        print(f"Conta total do cliente {self.nome}: R$ {self.calcular_conta_total():.2f}")  # Imprime o valor total da conta do cliente

    # Método para pagar parte da conta do cliente
    def pagar_conta(self, valor: float) -> None:
        self.conta -= valor  # Deduz o valor pago da conta total do cliente

# Criação de um objeto Cachorro com valores de exemplo
animal = Cachorro(
    nome="Rex",
    idade=3,
    cor="Marrom",
    tamanho=Tamanho.GRANDE,
    cliente=123,
    ID=456,
    data_chegada=date.today(),
    data_saida=date.today(),
    addr_historico="Rua Exemplo, 123",
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

# Adiciona o mesmo animal novamente à lista de animais do cliente (duplicação intencional para exemplo)
cliente.adicionar_animal(animal)

# Realiza uma consulta veterinária para o animal
animal.consulta_veterinaria()

# Criação de um objeto Tosador com valores de exemplo
tosador = Tosador("Pedro", 1, True)

# Realiza a tosa do animal
animal.tosa(tosador, TipoTosa.TESOURA)

# Imprime a conta total do cliente
cliente.conta_total()
