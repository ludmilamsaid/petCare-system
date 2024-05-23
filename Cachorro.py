from enum import Enum
from Animal import Animal
from datetime import date, datetime, timedelta

class Cachorro(Animal):
    def __init__(self, nome: str, idade: int, raca: str, cor: str, tamanho: str, cliente: int, ID: int, data_chegada: date, data_saida: date, addr_historico: str, conta: float):
        super().__init__(nome, idade, raca.value, cor, tamanho, cliente, ID, data_chegada, data_saida, addr_historico, conta)
        self.raca = raca

raca = ["Norsk Lundehund", "Bulldog Francês Fluffy", "Braco-da-Transilvânia", "Sabujo Colombiano", "American Bully", "Dogue de Bordeaux", "American Pit Bull Terrier", "Cão Esquimó Americano",
        "Manchester Terrier", "Shar Pei", "Coton de Tulear", "Cão Lobo Checoslovaco", "Griffon de Bruxelas", "Cão de Crista Chinês", "Harrier", "Chow Chow", "Dogue Alemão", "Galgo Espanhol",
        "Scottish Terrier", "Boiadeiro Australiano", "Schnauzer Miniatura", "Pinscher Miniatura", "Welsh Corgi Pembroke", "Bearded Collie", "Pastor dos Pirineus de Pelo Longo",
        "Collie de Pelo Curto", "Cão Esquimó Canadense", "Galgo Inglês", "Dogue Canário", "Mastim Tibetano", "Setter Irlandês", "Broholmer", "Pastor-Galego", "Spaniel Bretão", "Lébrel Irlandês",
        "Bloodhound ou Cão-de-Santo-Humberto", "Cavalier King Charles Spaniel", "Pelado Mexicano", "Terrier Americano Sem Pelo", "Terrier Alemão de Caça", "Vulpino Italiano", "Fox Terrier de Pelo Duro",
        "Bichon Frisé", "Papillon", "Basenji", "Husky Siberiano", "Doberman", "Prazsky Krysarik", "Pastor Belga Malinois", "Leão da Rodésia", "West Highland White Terrier", "Chorkie",
        "Cavoodle ou Cavapoo", "Australian Cobberdog", "Goldendoodle", "Cockapoo", "Cão d'água Português", "Terrier Tibetano", "Shichon", "Curly coated retriever", "Perdigueiro de Burgos",
        "Perdigueiro português", "Leonberger", "Silky terrier", "Flat-coated retriever", "Lancashire heeler", "Black mouth cur", "Cachorro pila argentino", "Pastor americano miniatura ou pastor australiano miniatura",
        "Bardino majorero", "Cão d'água irlandês", "Otterhound ou cão de lontra", "Cachorro Mudi", "Cão do faraó", "Tamaskan", "Cão-lobo-de-saarloos", "Clumber spaniel", "Pinscher austríaco",
        "Cão-pelado-peruano", "Alusky: malamute do alasca e husky", "Dandie Dinmont Terrier", "Skye terrier", "Lulu da Pomerânia", "Chesapeake bay retriever", "Pointer inglês", "Sloughi ou galgo árabe",
        "Setter inglês", "Dogo argentino", "Boykin spaniel", "Pastor-da-picardia", "Pastor-croata", "Pequeno brabançon", "Bull Arab", "Azawakh", "Aidi ou cão das montanhas do Atlas", "Pastor-polonês-da-planície",
        "Vizsla ou braco-húngaro-de-pelo-curto", "Jindo-coreano", "Cairn terrier", "Schipperke", "Terrier australiano (Australian Terrier)", "Kuvasz", "Soft coated wheaten terrier", "Spitz finlandês",
        "Spitz de norrbotten", "Collie de pelo longo", "Bouvier des Flandres (Boiadeiro de Flandres)", "Pastor-de-beauce ou beauceron", "Bedlington terrier", "Barbet ou cão d'água francês", "Coonhound inglês",
        "Poodle anão", "Spaniel tibetano", "Spitz dos visigodos ou vallhund sueco", "Samoieda", "Poochon", "Cuvac eslovaco", "Pinscher Alemão", "Catahoula cur", "Vira-lata caramelo", "Labsky ou huskador",
        "Shikoku Inu", "Affenpinscher", "Poodle gigante (caniche gigante)", "Griffon belga", "Mastim inglês ou mastiff", "Springer spaniel inglês", "Pequinês", "Bernedoodle", "Pastor-do-cáucaso",
        "Mastim espanhol", "Kelpie Australiano", "Kerry Blue Terrier", "Shorkie", "Mastim dos Pirinéus", "Podengo Português", "Husky Inu", "Goldador", "Foxhound Americano", "Foxhound Inglês", "Poodle Toy",
        "Ratonero Bodeguero Andaluz", "Schnoodle", "Elkhound Norueguês", "Shih poo", "Eurasier", "Pomsky", "Galgo Italiano ou Pequeno Lébrel Italiano", "Bichon Havanês", "Parson Russell Terrier",
        "Ratonero Valenciano ou Gos Rater Valencià", "Borzoi", "Puggle", "Braco-italiano", "Maltipoo", "Morkie", "Yorkie Poo ou Yorkipoo", "Labradoodle", "Pastor Bergamasco", "Pastor de Shetland", "Deerhound",
        "Labrador Retriever", "Boxer", "Bichon Bolonhês", "Cane Corso", "Mastim Napolitano", "Boiadeiro de Appenzeller", "Tosa Inu", "Cão d'água Espanhol", "Schnauzer Gigante", "Terrier Preto da Rússia",
        "Bulldog Francês", "Pastor Catalão", "Rottweiler", "Border Terrier", "Boiadeiro de Berna", "Staffordshire Bull Terrier", "Welsh Corgi Cardigan", "Bulldog Americano", "Bulldog Inglês", 
        "Braco alemão de pelo curto", "Pastor Australiano", "Pastor Branco Suíço", "Boston terrier", "Poodle ou caniche", "Chihuahua", "Terra-nova", "Malamute do Alasca", "Shih Tzu", "Saluki",
        "Fox Paulistinha ou Terrier Brasileiro", "Bullmastiff", "Cocker Spaniel Inglês", "Whippet", "Fila Brasileiro", "Airedale Terrier", "Pastor Belga Groenendael", "Pastor Belga Tervueren", 
        "Weimaraner ou Braco de Weimar", "Dálmata", "Dachshund ou Teckel", "Spitz Alemão", "Pug", "Lhasa Apso", "Fox Terrier de pelo liso", "Schnauzer", "Boerboel", "Jack Russell Terrier", "São Bernardo",
        "Bobtail", "Bull Terrier Inglês", "Galgo Afegão", "Golden Retriever", "Border Collie", "Basset Hound", "American Staffordshire Terrier", "Bull Terrier Inglês Miniatura", "Akita Inu",
        "Pastor alemão", "Maltês", "Beagle", "Yorkshire Terrier", "Shiba Inu", "Akita Americano"]