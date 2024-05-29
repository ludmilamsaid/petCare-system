from Banco import *

class BancoCliente(Banco):

    def __init__(self, addr: str) -> None:

        dataType = {
            "ID" : int, 
            "Nome" : str, 
            "PET" : list, 
            "Endereço" : str, 
            "Conta" : float
            }
        
        super().__init__(addr, dataType)