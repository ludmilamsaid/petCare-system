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

    """
    Classe que descreve um banco de dados do excel

    Attributes
    ----------
    __addr : str
        endereço do banco de dados
    __colunas : list<str>
        nome das colunas
    banco : pd
        Dataframe do banco referente
    __dataType : dict
        contém a tipagem de cada uma das colunas do banco

    Methods
    -------
    setNewAddr (self, addr : str) -> bool
        Altera o endereço __addr
    
    ler_banco(self) -> bool
        Lê o banco de dados do excel
    
    imprimir(self) -> bool
        Imprime o dataframe no terminal

    adicionar(self) -> bool
        Método abstrato, adiciona uma nova linha no Dataframe
    
    remover (self, item, tipo : str) -> bool
        Remove uma linha do dataframe

    procurarItem(self, item, tipo : str) -> pd.DataFrame
        procura linhas de um dataframe conforme o item passado

    alterarItem (self, itemNovo, itemAntigo, tipo : str) -> bool
        altera uma cédula do Dataframe
    """

    def __init__(self, addr: str, dataType, colunas : list) -> None:

        self.__addr = addr #Endereço da planilha
        self.__colunas = colunas #Nome das colunas
        self.banco = pd.DataFrame(columns=self.colunas)
        self.__dataType = dataType #Tipo dos dados
        self.ler_banco()

    def setNewAddr(self, addr: str) -> bool:

        """
        Altera o endereço do banco excel

        Parameters:
            addr : str - novo endereço do banco de dados
        
        Return:
            Se não houver erro, retorna True, caso contrário False
        """
        try:
            self.__addr = addr
            return True
        
        except Exception as e:
            print("Erro em setNewAddr", e)
            return False

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

        """
        Lê o banco de dados excel e transforma num data frame

        Parameters:
            Nenhum parametro

        Return: 
            Retorna True se não houver erros, caso contrário, retorna False
        """

        try:
            self.banco = pd.read_excel(self.addr, dtype=self.dataType, engine="openpyxl")
            self.banco = pd.DataFrame(self.banco)
            return True
        except ValueError as e:
            print(f"Erro ao ler o arquivo Excel: {e}")
            return False
        except Exception as e:
            #Qualquer outro erro
            print("Banco vazio:", e)
            self.banco = None
            return False

    def imprimir(self) -> bool:

        """
        Imprime o banco de dados

        Parameters:
            Nenhum parametro

        Return: 
            Retorna True se não houver erros, caso contrário, retorna False
        """

        try:
            print(self.banco)
            return True
        except:
            print("Erro ao imprimir")
            return False

    @abstractmethod
    def adicionar(self, novaLinha : list) -> bool:

        """
        Adiciona uma nova linha ao dataFrame

        Parameters:
            novaLinha : lis - polimorfico

        Return:
        Retorna True se não houber erros, caso contrário, retorna False
        """
        pass
    
    def procurarItem(self, item, tipo: str) -> pd.DataFrame:

        """
        Procura um item do banco de dados

        Parameters:
            item : Any - polimorfico, depende do atributo instanciado, item a ser procurado
            tipo : str - nome da coluna que o item pode estar inserido

        Return:
            Retorna um data frame com o resultado das buscas
        """
        
        try:
            itemProcurado = self.banco[self.banco[tipo] == item]
            return pd.DataFrame(itemProcurado)
        except:
            print("Banco: Erro ao procurar item")
            return pd.DataFrame()

    def atualizarBanco(self) -> bool:

        """
            Atualiza o banco de dados no excel   

        Parameters:
            Nenhum

        Return:
        Retorna True se não houber erros, caso contrário, retorna False
        """

        try:
            self.banco.to_excel(self.addr, index=False, sheet_name="planilha", engine="openpyxl")
            return True
        except:
            print("Erro ao escrever sobre a planilha")
            return False
        
    def remover(self, item, tipo: str) -> bool:

            # conferir quando tiver mais de um item
        
        """Remove um item do banco de dados

        Parameters:
            item : Any - polimorfico, depende do atributo instanciado, item a ser removido
            tipo : str - nome da coluna que o item pode estar inserido

        Return:
            Retorna um data frame com o resultado das buscas"""
        
        try:
            self.banco = self.banco[self.banco[tipo] != item]
            self.atualizarBanco()
            return True
        
        except:
            print("Erro ao remover item")
            return False

    def alterarItem(self, itemNovo, ID : str, tipo: str) -> bool:
       
        """
        Altera uma cédula do banco de dados. Utiliza do método procurarItem()

        Parameters:
        itemNovo : Any - polimorfico, item a substituir
        tipo : str - nome da cédula
        ID : str - para procurar

        Return:
         True se não houver erros, e False se houver
        """

        try:
            itemProcurado = self.procurarItem(ID, "ID")
            
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
