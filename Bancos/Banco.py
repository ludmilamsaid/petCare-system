import pandas as pd

class ItemNaoEncontrado (Exception):
    def __init__(self) -> None:
        self.erro = "Item nao encontrado"

class Banco:
    def __init__(self, addr: str, dataType) -> None:

        self.__addr = addr
        self.banco : pd.DataFrame = None
        self.__dataType = dataType
        self.ler_banco()

    def setNewAddr(self, addr: str) -> None:
        self.__addr = addr

    @property
    def addr(self) -> str:
        return self.__addr

    @property
    def dataType(self) -> None:
        return self.__dataType

    def ler_banco(self) -> bool:

        try:
            self.banco = pd.read_excel(self.addr, dtype=self.__dataType, engine="openpyxl")
            self.banco = pd.DataFrame(self.banco)
            return True
        except ValueError as e:
            print(f"Erro ao ler o arquivo Excel: {e}")
            return False
        except:
            print("Banco vazio")
            self.banco = None
            return False

    def imprimir(self) -> bool:

        try:
            print(self.banco)
            return True
        except:
            print("Erro ao imprimir")
            return False

    def adicionar(self, novaLinha : list) -> bool:
        
        try:
            self.banco = self.banco._append(novaLinha, ignore_index=True)
            self.atualizarBanco()
            return True
        except:
            print("Erro ao adicionar linha")
            return False

    def procurarItem(self, item, tipo: str) -> pd.DataFrame:
        
        try:
            itemProcurado = self.banco[self.banco[tipo] == item]
            return pd.DataFrame(itemProcurado)
        except:
            print("Erro ao procurar item")
            return self.banco

    def atualizarBanco(self) -> bool:

        try:
            self.banco.to_excel(self.addr, index=False, sheet_name="testando", engine="openpyxl")
            return True
        except:
            print("Erro ao escrever sobre a planilha")
            return False
        
    def remover(self, item, tipo: str) -> bool:
        try:
            self.banco = self.banco[self.banco[tipo] != item]
            self.atualizarBanco()
            return True
        
        except:
            print("Erro ao remover item")
            return False

    def alterarItem(self, itemNovo, itemAntigo, tipo: str) -> None:
       
        try:

            itemProcurado = self.procurarItem(itemAntigo, tipo)
            
            if not itemProcurado.empty:
                indiceLinha = itemProcurado.index[0]
                self.banco.at[indiceLinha, tipo] = itemNovo
                self.atualizarBanco()
            else:
                erro = ItemNaoEncontrado()
                raise erro
            
        except ItemNaoEncontrado:
            print(erro.erro)
        except:
            print("Erro ao alterar item")
