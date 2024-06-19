class Funcionario:
    # Inicializador da classe Funcionario
    def __init__(self, ID: int, nome: str, disponivel: bool) -> None:
        self.ID = ID  # Atributo que armazena o ID do funcionário
        self.nome = nome  # Atributo que armazena o nome do funcionário
        self.disponivel = disponivel  # Atributo que indica se o funcionário está disponível (True) ou não (False)

    # Método para marcar a chegada do funcionário
    def chegar(self) -> None:
        self.disponivel = True  # Define o atributo 'disponivel' como True
        return f"O funcionário {self.nome} (ID: {self.ID}) está na clínica."  # Retorna uma mensagem informando que o funcionário está na clínica

    # Método para marcar a saída do funcionário
    def sair(self) -> None:
        self.disponivel = False  # Define o atributo 'disponivel' como False
        return f"O funcionário {self.nome} (ID: {self.ID}) saiu da clínica."  # Retorna uma mensagem informando que o funcionário saiu da clínica
