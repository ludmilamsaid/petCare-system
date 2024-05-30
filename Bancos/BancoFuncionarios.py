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
        dataAdicionar = {
            "ID" : novaLinha[0],
            "Nome" : novaLinha[1],
            "Disponibilidade" : novaLinha[2]}
        try:
            dataAdicionar = pd.DataFrame.from_dict(data=dataAdicionar, dtype=self.dataType)
            self.banco = self.banco._append(dataAdicionar, ignore_index=True)
            self.atualizarBanco()
            return True
        
        except:
            print("Erro ao adicionar linha")
            return False

teste = BancoFuncionarios()
print(teste.addr)
teste.ler_banco()
teste.adicionar([int(101), "Joao", True])
teste.atualizarBanco()
teste.imprimir()