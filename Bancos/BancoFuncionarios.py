from Banco import *

class BancoFuncionarios(Banco):

    def __init__(self) -> None:

        dataType = {
             "ID" : int, 
             "Nome" : str, 
             "Disponibilidade" : bool 
        }
        colunas = ["ID", "Nome", "Disponibilidade"]
        addr = "Bancos/Planilhas/Funcionarios.xlsx"

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
            print(f"Banco Funcionarios: Erro ao adicionar linha: {e}")
            return False
        
    def alterar_disponibilidade(self, nome):
        try:
            index = self.banco[self.banco["Nome"] == nome].index[0]
            self.banco.at[index, "Disponibilidade"] = not self.banco.at[index, "Disponibilidade"]
            self.atualizarBanco()
            print("Alteracao concluida")
            return True
        except Exception as e:
            print(f"Banco Funcionarios: Erro ao alterar disponibilidade: {e}")
            return False
        
        
def teste() -> None:

    teste = BancoFuncionarios()
    print(teste.addr)
    teste.adicionar([101, "Joao", True])
    teste.alterarItem("Maria", "Joao", "Nome")
    teste.imprimir()
    teste.remover("Maria", "Nome")
    teste.atualizarBanco()
    teste.imprimir()
    teste.alterar_disponibilidade("Geraldo Magela")
#teste()