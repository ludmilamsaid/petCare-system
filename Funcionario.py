class Funcionario:
    def __init__(self, ID: int,nome: str, disponivel: bool) -> None:
        self.ID = ID
        self.nome = nome
        self.disponivel = disponivel
        
    def chegar(self) -> None:
        self.disponivel = True
        return f"O funcionário {self.nome} (ID: {self.ID}) está na clínica."

    def sair(self) -> None:
        self.disponivel = False
        return f"O funcionário {self.nome} (ID: {self.ID}) saiu da clínica."