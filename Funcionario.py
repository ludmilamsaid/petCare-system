from Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, ID, valor_servico, disponivel):
        super().__init__(nome)
        self.ID = ID
        self.valor_servico = valor_servico
        self.disponivel = disponivel
        
def chegar(self):
        self.disponivel = True
        return f"O funcionário {self.nome} (ID: {self.ID}) está na clínica."

def sair(self):
        self.disponivel = False
        return f"O funcionário {self.nome} (ID: {self.ID}) saiu da clínica."
