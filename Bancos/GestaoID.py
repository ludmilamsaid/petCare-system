from typing import List
import random

class GestaoID:

    def __init__(self, addr : str) -> None:

        """
        Classe para gestão de IDs. Os IDs que já foram utilizados são guardados num arquivo txt

        Atributos:
        - addr : str (endereço do banco de dados)
        + ID_existentes : List[int] (lista de IDs que j[á existem])

        Métodos:
        + <<get>> addr () -> str
        + lerBanco () -> List[int]
        + criarID () -> int
        + adicionarID (ID : int) -> bool
        + removerID (ID : int) -> bool

        """

        self.__addr_ID = addr #banco de IDs utilizados
        self.ID_existentes = List[int] #lista de IDs existentes

    @property #<<get>>
    def addr(self) -> str:
        return self.__addr_ID
    
    def lerBanco(self) -> List[int]:

        """
        Lê o banco de IDs que já foram utilizados

        Parameters:
        Nenhum

        Return:
        Retorna a lista de IDs já utilizados e gravados no arquivo em self.addr. Caso
        haja erro, retorna uma lista vazia
        """

        try:
            arquivo = open(self.addr, "r")
            IDs = arquivo.read()
            #formatação do arquivo
            IDs = IDs.split('\n')
            IDs = filter(None, IDs)
            self.ID_existentes = list(map(int, IDs))
            arquivo.close()
            return self.ID_existentes

        except Exception as e:
            print("Erro em ler banco: ", e)
            return []
        
    def criarID(self) -> int:

        """
        Cria um ID que não existe em self.addr. Utiliza a biblioteca Random

        Parameters:
        Nenhum

        Return:
        Inteiro ID que não existe em self.addr. Caso haja algum erro, retorna -1
        """
        
        try:
            while True:
                numero_novo = int(random.randrange(1, 1000000))
                if numero_novo not in self.ID_existentes:
                    return numero_novo
        
        except Exception as e:
            print("Erro em criar ID:", e)
            return -1
    
    def atualizaBanco(self) -> bool:

        """
        Sobrescreve o arquivo em self.addr com self.TD_existentes

        Parameters:
        Nenhum

        Return:
        False se houver erros, caso contrário, True
        """
        try:
            arquivo = open(self.addr, "w")
            for i in self.ID_existentes:
                arquivo.write(f"{i}\n")
            
            arquivo.close()
            return True
        
        except Exception as e:
            print("Erro em atualizar banco IDs:", e)
            return False
    
    def adicionarID(self, ID : int) -> bool:

        """
        Adiciona um ID a self.ID_existentes, depois chama self.atualizaBanco()

        Parameters:
        ID : int - novo ID a ser adicionado

        Return:
        True se não houver erros, caso contrário, False
        """
        
        try:
            self.ID_existentes.append(ID)
            self.atualizaBanco()
            return True
        
        except Exception as e:
            print("Erro em adicionar novo ID:", e)
            return False
        
    def removerID(self, ID : int) -> bool:

        """
        Remove um ID a self.ID_existentes, depois chama self.atualizaBanco()

        Parameters:
        ID : int - novo ID a ser removido

        Return:
        True se não houver erros, caso contrário, False
        """

        try:
            if ID in self.ID_existentes:
                self.ID_existentes.remove(ID)
                self.atualizaBanco()
                return True
            else:
                raise Exception("ID nao pertence a lista")
        
        except Exception as e:
            print("Erro remove ID:", e)
            return False

def inicializarBanco():

    lista_ID_animais = GestaoID("Bancos/IDs/ID_animais.txt")
    