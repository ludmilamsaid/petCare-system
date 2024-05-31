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
    
    def adicionar(self, novaLinha: list) -> bool:

        novaLinha = [{
            "ID" : novaLinha[0],
            "Nome" : novaLinha[1],
            "Disponibilidade" : novaLinha[2]
        }]
        try:
            novaLinha_df = pd.DataFrame(novaLinha).astype(self.__dataType)
            self.banco = pd.concat([self.banco, novaLinha_df], ignore_index=True)
            self.atualizarBanco()
            return True

        except Exception as e:
            print(f"Erro ao adicionar linha: {e}")
            return False

teste = BancoFuncionarios()
print(teste.addr)
teste.adicionar([int(101), "Joao", True])
teste.atualizarBanco()
teste.imprimir()