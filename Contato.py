import datetime
class Contato():
    def __init__(self, pessoa, telefones):
        self.criacao = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
        self.pessoa = pessoa
        self.telefones = telefones

    def listarTelefone(self):
        pass