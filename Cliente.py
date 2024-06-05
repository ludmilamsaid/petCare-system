class Cliente:
    def __init__(self, nome: str, pet: int, conta: float, endereco: str, ID: int) -> None:
        self.nome = nome
        self.pet = pet
        self.conta = conta
        self.endereco = endereco
        self.ID = ID