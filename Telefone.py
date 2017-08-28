import datetime
class telefone
    def main(self, Numero, DDD, CodigoPais):
        self.Numero = Numero
        self.DDD = DDD
        self.CodigoPais = CodigoPais

class Contato():
    def __init__(self, criacao):
        self.criacao = criacao(datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))

    def listarTelefone(self):
        pass
