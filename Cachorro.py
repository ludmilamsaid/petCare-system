from enum import Enum
from Animal import Animal, Especie
from datetime import date
from Tosador import TipoTosa, Tosador
from Tamanho import Tamanho
# Classe Cachorro, que herda de Animal
class Cachorro(Animal):
    # Inicializador da classe Cachorro
    def __init__(self, nome: str, idade: int, raca: str, cor: str, tamanho: Tamanho, cliente: int, ID: int, data_chegada: date, data_saida: date, addr_historico: str, conta: float) -> None:
        # Chama o inicializador da classe pai (Animal)
        super().__init__(nome, idade, Especie.CACHORRO, cor, tamanho, cliente, ID, data_chegada, data_saida, addr_historico, conta)
        # Define o atributo raca específico da classe Cachorro
        self.raca = raca

    # Método para consulta veterinária
    def consulta_veterinaria(self) -> None:
        # Imprime uma mensagem de consulta veterinária
        print(f"Consulta veterinária para o cachorro {self.nome}.")
        # Adiciona o serviço de consulta veterinária com valor 100.0
        self.adicionar_servico("Consulta Veterinária", 100.0)

    # Método para realizar a tosa
    def tosa(self, tosador: Tosador, tipo_tosa: TipoTosa) -> None:
        # Verifica se o tosador está disponível
        if tosador.disponivel:
            # Calcula o valor da tosa com base no tamanho do cachorro e tipo de tosa
            valor_tosa = tosador.calcular_valor_tosa_cachorro(self.tamanho, tipo_tosa)
            # Imprime uma mensagem indicando que o tosador está realizando a tosa
            print(f"Tosador {tosador.nome} está tosando o cachorro {self.nome}.")
            # Imprime o valor da tosa
            print(f"Valor da tosa: R$ {valor_tosa:.2f}")
            # Adiciona o serviço de tosa com o valor calculado
            self.adicionar_servico("Tosa", valor_tosa)
        else:
            # Imprime uma mensagem indicando que o tosador não está disponível
            print(f"Tosador {tosador.nome} não está disponível no momento.")

    # Método para realizar o banho
    def banho(self, tosador: Tosador) -> None:
        # Verifica se o tosador está disponível
        if tosador.disponivel:
            # Calcula o valor do banho com base no tamanho do cachorro
            valor_banho = tosador.calcular_valor_banho_cachorro(self.tamanho)
            # Imprime uma mensagem indicando que o tosador está dando banho
            print(f"Tosador {tosador.nome} está dando banho no cachorro {self.nome}.")
            # Imprime o valor do banho
            print(f"Valor do banho: R$ {valor_banho:.2f}")
            # Adiciona o serviço de banho com o valor calculado
            self.adicionar_servico("Banho", valor_banho)
        else:
            # Imprime uma mensagem indicando que o tosador não está disponível
            print(f"Tosador {tosador.nome} não está disponível no momento.")

# Lista de raças de cachorros
raca_cachorro = [
    "Affenpinscher", "Aidi ou cão das montanhas do Atlas", "Akita Americano", "Akita Inu", "Alusky: malamute do alasca e husky", "American Bully", "American Pit Bull Terrier", "American Staffordshire Terrier",
    "Australian Cobberdog", "Azawakh", "Barbet ou cão d'água francês", "Bardino majorero", "Basenji", "Basset Hound", "Beagle", "Bearded Collie", "Bedlington terrier", "Bernedoodle", "Bichon Bolonhês",
    "Bichon Frisé", "Bichon Havanês", "Black mouth cur", "Bloodhound ou Cão-de-Santo-Humberto", "Bobtail", "Boiadeiro Australiano", "Boiadeiro de Appenzeller", "Boiadeiro de Berna", "Border Collie",
    "Border Terrier", "Borzoi", "Boston terrier", "Boykin spaniel", "Braco alemão de pelo curto", "Braco-da-Transilvânia", "Braco-italiano", "Broholmer", "Bull Arab", "Bull Terrier Inglês", "Bull Terrier Inglês Miniatura",
    "Bullmastiff", "Bulldog Americano", "Bulldog Francês", "Bulldog Francês Fluffy", "Bulldog Inglês", "Cachorro Mudi", "Cachorro pila argentino", "Cairn terrier", "Cane Corso", "Cão d'água Espanhol", "Cão d'água Português",
    "Cão d'água irlandês", "Cão de Crista Chinês", "Cão Esquimó Americano", "Cão Esquimó Canadense", "Cão do faraó", "Cão Lobo Checoslovaco", "Cão-lobo-de-saarloos", "Cão-pelado-peruano", "Cão-pelado-peruano",
    "Catahoula cur", "Cavalier King Charles Spaniel", "Cavoodle ou Cavapoo", "Chesapeake bay retriever", "Chihuahua", "Chorkie", "Chow Chow", "Clumber spaniel", "Cockapoo", "Collie de Pelo Curto", "Collie de pelo longo",
    "Curly coated retriever", "Coton de Tulear", "Coonhound inglês", "Coonhound inglês", "Cuvac eslovaco", "Dachshund ou Teckel", "Dálmata", "Dandie Dinmont Terrier", "Deerhound", "Doberman", "Dogo argentino",
    "Dogue Alemão", "Dogue Canário", "Dogue de Bordeaux", "Elkhound Norueguês", "Eurasier", "Fila Brasileiro", "Flat-coated retriever", "Fox Paulistinha ou Terrier Brasileiro", "Fox Terrier de Pelo Duro", "Fox Terrier de pelo liso",
    "Foxhound Americano", "Foxhound Inglês", "Galgo Afegão", "Galgo Espanhol", "Galgo Inglês", "Galgo Italiano ou Pequeno Lébrel Italiano", "Goldador", "Golden Retriever", "Goldendoodle", "Griffon belga",
    "Griffon de Bruxelas", "Harrier", "Husky Inu", "Husky Siberiano", "Jack Russell Terrier", "Jindo-coreano", "Kelpie Australiano", "Kerry Blue Terrier", "Kuvasz", "Labrador Retriever", "Labradoodle",
    "Labsky ou huskador", "Lancashire heeler", "Leonberger", "Leão da Rodésia", "Lhasa Apso", "Lulu da Pomerânia", "Malamute do Alasca", "Manchester Terrier", "Maltês", "Maltipoo", "Mastim inglês ou mastiff",
    "Mastim espanhol", "Mastim Napolitano", "Mastim Tibetano", "Mastim dos Pirinéus", "Miniature Bull Terrier", "Morkie", "Norwegian Lundehund", "Otterhound ou cão de lontra", "Papillon", "Parson Russell Terrier",
    "Pastor alemão", "Pastor americano miniatura ou pastor australiano miniatura", "Pastor Australiano", "Pastor Belga Groenendael", "Pastor Belga Malinois", "Pastor Belga Tervueren", "Pastor Bergamasco",
    "Pastor Branco Suíço", "Pastor Catalão", "Pastor-croata", "Pastor-da-picardia", "Pastor-de-beauce ou beauceron", "Pastor-de-beauce ou beauceron", "Pastor-do-cáucaso", "Pastor-Galego", "Pastor-polonês-da-planície",
    "Pastor dos Pirineus de Pelo Longo", "Pequeno brabançon", "Pequinês", "Perdigueiro de Burgos", "Perdigueiro português", "Pinscher Alemão", "Pinscher austríaco", "Pinscher Miniatura", "Poodle anão",
    "Poodle gigante (caniche gigante)", "Poodle ou caniche", "Poodle Toy", "Pointer inglês", "Podengo Português", "Pomsky", "Poochon", "Poodle Toy", "Pointer inglês", "Poodle gigante (caniche gigante)", 
    "Saluki", "Samoyed", "Schnauzer", "Schnauzer Gigante", "Schnauzer Miniatura", "Schnoodle", "Schipperke", "Scottish Terrier", "Setter inglês", "Setter Irlandês", "Shar Pei", "Shichon", "Shih Tzu", 
    "Shikoku Inu", "Shih poo", "Silky terrier", "Skye terrier", "Sloughi ou galgo árabe", "Soft coated wheaten terrier", "Spaniel Bretão", "Spaniel tibetano", "Spitz Alemão", "Spitz de norrbotten", 
    "Spitz finlandês", "Spitz dos visigodos ou vallhund sueco", "Springer spaniel inglês", "Staffordshire Bull Terrier", "Tamaskan", "Terrier Alemão de Caça", "Terrier Americano Sem Pelo", "Terrier Australiano (Australian Terrier)",
    "Terrier Preto da Rússia", "Terrier Tibetano", "Terra-nova", "Tosa Inu", "Vira-lata caramelo", "Vizsla ou braco-húngaro-de-pelo-curto", "Vulpino Italiano", "Weimaraner ou Braco de Weimar", "Welsh Corgi Cardigan",
    "Welsh Corgi Pembroke", "West Highland White Terrier", "Whippet", "Yorkie Poo ou Yorkipoo", "Yorkshire Terrier"
]

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

# Criação de um objeto Tosador com valores de exemplo
tosador = Tosador("Pedro", 1, True)

# Chamada do método tosa para o objeto animal com o tosador e o tipo de tosa especificados
Cachorro.tosa(animal, tosador, TipoTosa.TESOURA)
