from Banco import *

class BancoCliente(Banco):

    def __init__(self) -> None:

        dataType = {
            "ID" : int, 
            "Nome" : str, 
            "PET" : list, 
            "Endereço" : str, 
            "Conta" : float
            }
        
        addr = "Planilhas/Clientes.xlsx"
        
        super().__init__(addr, dataType)