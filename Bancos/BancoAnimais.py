from Banco import *

class BancoAnimais(Banco):

    #ID, Nome, Idade, Espécie, Raça, Cor, Tamanho, Tutor (ID), Horário Chegada, Horário Saída, Endereço Histórico, Conta

    def __init__(self) -> None:

        dataType = {
             "ID" : str,
             "Nome" : str,
             "Idade" : int, 
             "Espécie" : str,
             "Raça" : str,
             "Cor" : str,
             "Tamanho" : str,
             "Tutor" : str,
             "Horário Chegada" : str,
             "Horário Saída" : str,
             "Endereço Histórico" : str,
             "Conta" : float 
        }

        colunas = ["ID", "Nome", "Idade", "Espécie", "Raça", "Cor","Tamanho", "Tutor",
                    "Horário Chegada", "Horário Saída", "Endereço Histórico", "Conta"]
        addr = "Bancos/Planilhas/Animais.xlsx"

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
            self.colunas[4] : novaLinha[4],
            self.colunas[5] : novaLinha[5],
            self.colunas[6] : novaLinha[6],
            self.colunas[7] : novaLinha[7],
            self.colunas[8] : novaLinha[8],
            self.colunas[9] : novaLinha[9],
            self.colunas[10] : f"Históricos/{novaLinha[0]}.txt",
            self.colunas[11] : novaLinha[10],
            
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

    def ler_ID_animais(self) -> list:

        self.ler_banco()
        IDs_utilizados = self.banco["ID"].tolist()

        return IDs_utilizados

def teste() -> None:
    banco = BancoAnimais()
    #"Nome", "Idade", "Espécie", "Raça", "Cor","Tamanho", "Tutor","Horário Chegada", "Horário Saída", "Endereço Histórico", "Conta"
    banco.adicionar(["Joao", "rex", "preto", "médio",  123, "23h43", "123h1", 0])

#teste()