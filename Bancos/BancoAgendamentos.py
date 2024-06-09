from Banco import *

class DataHorario:
    def __init__(self, horas : str, dia : str) -> None:
        self.horas = horas
        self.dia = dia
    
    def horario (self) -> str:
        return self.horas+" "+self.dia

class BancoAgendamentos(Banco):

    #Tutor, PET, Serviço, Horário

    def __init__(self) -> None:

        dataType = {
             "Tutor" : str,
             "PET" : str,
             "Serviço" : str,
             "Horário" : object
        }

        colunas = ["Tutor", "PET", "Serviço", "Horário"]
        addr = "Bancos/Planilhas/Agendamentos.xlsx"

        super().__init__(addr, dataType, colunas)
    
    def adicionar(self, novaLinha: list) -> bool:

        #Conferir se o item já existe
        PET = novaLinha[1]
        #Converter nova linha para dict
        novaLinha = {
            self.colunas[0] : novaLinha[0],
            self.colunas[1] : novaLinha[1],
            self.colunas[2] : novaLinha[2],
            self.colunas[3] : novaLinha[3],
        }

        try:
            novaLinha = pd.DataFrame([novaLinha]).astype(self.dataType)
            
            if not self.procurarItem(PET, "PET").empty:
                #Erro, pois a pessoa já existe no banco
                raise RegisteredItem
            else:
                self.banco = pd.concat([self.banco, novaLinha], ignore_index=True)
                self.atualizarBanco()
                return True

        except Exception as e:
            print(f"Erro ao adicionar linha: {e}")
            return False
        
    def removerTopo(self) -> bool:
        try:
            self.banco = self.banco.drop(0).reset_index(drop=True)
            return True
        except Exception as e:
            print("Erro ao remover topo:", e)
            return False
        
def teste() -> None:
    
    teste = BancoAgendamentos()
    print(teste.addr)
    data = DataHorario("12h34", "30/04")
    teste.adicionar(["Joao", "Totó", "Tosa", data.horario()])
    teste.adicionar(["Geraldo","Poodle", "Banho", data.horario()])
    teste.removerTopo()
    teste.atualizarBanco()
    teste.imprimir()

#teste()