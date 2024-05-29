from Banco import *

class BancoFuncionarios(Banco):

    def __init__(self) -> None:

        dataType = {
             "ID" : int, 
             "Nome" : str, 
             "Disponibilidade" : bool 
        }

        addr = "Planilhas/Funcionarios.xlsx"

        super().__init__(addr, dataType)

teste = BancoFuncionarios()
teste.ler_banco()
teste.adicionar([int(101), "Joao", True])
teste.imprimir()