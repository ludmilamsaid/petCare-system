import pandas as pd
from abc import ABC, abstractmethod

class NotFoundItem (Exception):
    def __init__(self) -> None:
        self.erro = "Item não encontrado"
        super().__init__(self.erro)

class RegisteredItem (Exception):
    def __init__(self) -> None:
        self.erro = "Item já existe no sistema"
        super().__init__(self.erro)

class Banco(ABC):
    def __init__(self, addr: str, dataType, colunas : list) -> None:

        self.__addr = addr #Endereço da planilha
        self.__colunas = colunas #Nome das colunas
        self.banco = pd.DataFrame(columns=self.colunas)
        self.__dataType = dataType #Tipo dos dados
        self.ler_banco()

    def setNewAddr(self, addr: str) -> None:
        self.__addr = addr

    @property
    def addr(self) -> str:
        return self.__addr

    @property
    def dataType(self) -> dict:
        return self.__dataType
    
    @property
    def colunas (self) ->list:
        return self.__colunas

    def ler_banco(self) -> bool:

        try:
            self.banco = pd.read_excel(self.addr, dtype=self.dataType, engine="openpyxl")
            self.banco = pd.DataFrame(self.banco)
            return True
        except ValueError as e:
            print(f"Erro ao ler o arquivo Excel: {e}")
            return False
        except:
            #Qualquer outro erro
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

    @abstractmethod
    def adicionar(self, novaLinha : list) -> bool:
        pass
    
    def procurarItem(self, item, tipo: str) -> pd.DataFrame:
        
        try:
            itemProcurado = self.banco[self.banco[tipo] == item]
            return pd.DataFrame(itemProcurado)
        except:
            print("Erro ao procurar item")
            return pd.DataFrame()

    def atualizarBanco(self) -> bool:

        try:
            self.banco.to_excel(self.addr, index=False, sheet_name="planilha", engine="openpyxl")
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

    def alterarItem(self, itemNovo, itemAntigo, tipo: str) -> bool:
       
        try:
            itemProcurado = self.procurarItem(itemAntigo, tipo)
            
            if not itemProcurado.empty:
                indiceLinha = itemProcurado.index[0]
                self.banco.at[indiceLinha, tipo] = itemNovo
                self.atualizarBanco()
                return True
            else:
                erro = NotFoundItem()
                raise erro
            
        except NotFoundItem:
            print(erro.erro)
            return False
        except:
            print("Erro ao alterar item")
            return False
