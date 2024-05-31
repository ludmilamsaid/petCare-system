from Banco import *

class BancoFuncionarios(Banco):

    def __init__(self) -> None:

        dataType = {
             "ID" : int, 
             "Nome" : str, 
             "Disponibilidade" : bool 
        }
        colunas = ["ID", "Nome", "Disponibilidade"]
        addr = "Planilhas/Funcionarios.xlsx"

        super().__init__(addr, dataType, colunas)
    
    def adicionar(self, novaLinha: list) -> bool:

        #Conferir se o item já existe
        ID = novaLinha[0]
        #Converter nova linha para dict
        novaLinha = {
            self.colunas[0] : novaLinha[0],
            self.colunas[1] : novaLinha[1],
            self.colunas[2] : novaLinha[2]
        }

        try:
            novaLinha = pd.DataFrame([novaLinha]).astype(self.dataType)
            
            if not self.procurarItem(ID, "ID").empty:
                #Erro, pois a pessoa já existe no banco
                raise RegisteredItem
            else:
                self.banco = pd.concat([self.banco, novaLinha], ignore_index=True)
                self.atualizarBanco()
                return True

        except Exception as e:
            print(f"Erro ao adicionar linha: {e}")
            return False

def teste() -> None:

    teste = BancoFuncionarios()
    print(teste.addr)
    teste.adicionar([101, "Joao", True])
    teste.atualizarBanco()
    teste.imprimir()

#teste()