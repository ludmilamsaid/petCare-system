from Banco import *

class BancoClientes(Banco):

    #ID, Nome, PETs (ID), Endereço, Conta

    def __init__(self) -> None:

        dataType = {
             "ID" : str, 
             "Nome" : str, 
             "PETs" : object,
             "Endereço" : str,
             "Conta" : float 
        }

        colunas = ["ID", "Nome", "PETs", "Endereço", "Conta"]
        addr = "Bancos/Planilhas/Clientes.xlsx"

        super().__init__(addr, dataType, colunas)
    
    def adicionar(self, novaLinha: list) -> bool:

        #Conferir se o item já existe
        ID = novaLinha[0]
        #Converter nova linha para dict
        novaLinha = {
            self.colunas[0] : novaLinha[0],
            self.colunas[1] : novaLinha[1],
            self.colunas[2] : novaLinha[2],
            self.colunas[3] : novaLinha[3],
            self.colunas[4] : novaLinha[4]
        }

        try:
            novaLinha = pd.DataFrame([novaLinha]).astype(self.dataType)
            self.ler_banco()
            if not self.procurarItem(ID, "ID").empty:
                #Erro, pois a pessoa já existe no banco
                raise RegisteredItem
            else:
                self.banco = pd.concat([self.banco, novaLinha], ignore_index=True)
                self.atualizarBanco()
                return True

        except Exception as e:
            print(f"Banco Animais: Erro ao adicionar linha: {e}")
            return False

def teste() -> None:
    
    teste = BancoClientes()
    # print(teste.addr)
    # teste.adicionar([101, "Joao", [101, 102, 103], "35180184", 234.23])
    teste.remover("4", "ID")
    teste.atualizarBanco()
    teste.imprimir()
    

#teste()