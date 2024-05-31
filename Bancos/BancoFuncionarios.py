from Banco import *

class BancoFuncionarios(Banco):

    def __init__(self) -> None:

        dataType = {
             "ID" : int, 
             "Nome" : str, 
             "Disponibilidade" : bool 
        }

        addr = "Planilhas/Funcionarios.xlsx"
        colunas = ["ID", "Nome", "Disponibilidade"]

        super().__init__(addr, dataType, colunas)
    
    def adicionar(self, novaLinha: list) -> bool:

        ID = novaLinha[0]

        novaLinha = {
            "ID" : novaLinha[0],
            "Nome" : novaLinha[1],
            "Disponibilidade" : novaLinha[2]
        }

        print("Fez dicionario")
        try:
            novaLinha = pd.DataFrame([novaLinha]).astype(self.dataType)
            
            if not self.procurarItem(ID, "ID").empty:
                raise ValueError("Já existe essa pessoa")
            else:
                self.banco = pd.concat([self.banco, novaLinha], ignore_index=True)
                self.atualizarBanco()
                return True

        except Exception as e:
            print(f"Erro ao adicionar linha: {e}")
            return False

teste = BancoFuncionarios()
print(teste.addr)
teste.adicionar([101, "Joao", True])
teste.atualizarBanco()
teste.imprimir()