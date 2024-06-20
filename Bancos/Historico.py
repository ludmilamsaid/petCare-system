class FileNotCreated (Exception):

    #Erro criado para pasta não criada mesmo com o método utilizado

    def __init__(self) -> None:
        super().__init__("Erro ao criar arquivo não criado")

class Historico:

    def __init__(self, addr : str, ID_pet : int, ID_tutor : int) -> None:

        self.__addr = addr
        self.__pet = ID_pet
        self.__tutor = ID_tutor

    @property
    def addr (self) -> str:
        return self.__addr
    
    @property
    def pet (self) -> int:
        return self.__pet
    
    @property
    def tutor (self) -> int:
        return self.__tutor
    
    def __criarHistorico(self) -> bool:

        """
        Método privado para criar o histórico

        Parameters:
        None

        Return:
        True se não houver erros, caso contrário, False
        """

        try:
            print("Arquivo não existe")
            with open(self.addr, "x") as arquivo:
                arquivo.write(f"{self.pet} {self.tutor}\n")
                arquivo.write("\n")
                arquivo.close()
                return True

        except Exception as e:
            print("Erro ao criar arquivo", e)
            return False
        
    def lerHistorico(self) -> str:

        """
        Lê o histórico no endereço self.addr.Caso o historico não exista, o método cria um
        arquivo e depois abre-o.

        Parameters:
        None

        Return:
        Retorna o texto do arquivo. Retorna None, caso haja erros
        """

        while True:
            try:
                arquivo = open(self.addr, "r")
                texto = arquivo.read()
                arquivo.close()
                return texto
            
            except FileNotFoundError as e:
                if not self.__criarHistorico():
                    raise FileNotCreated

            except Exception as e:
                print(e)
                return None

    def atualizarHistorico(self, adendo : str) -> bool:

        """
        Adiciona/atualiza o histórico no endereço self.addr

        Parameters:
        adendo : str - Novo texto a ser adicionado ao histórico

        Return:
        True se não hover erros, False se houver erros
        """
        
        try:
            arquivo = open(self.addr, "a", encoding="utf-8") #enconding : utf-8 para incluir caracteres do português
            arquivo.write(adendo + "\n")
            arquivo.close()
            return True
        
        except Exception as e:
            print("Erro em atualizar historico", e)
            return False
            