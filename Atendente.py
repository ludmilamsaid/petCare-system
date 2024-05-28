from Funcionario import Funcionario

class Atendente(Funcionario):
    def __init__(self, nome, ID, disponivel=False):
        super().__init__(nome, ID, disponivel)