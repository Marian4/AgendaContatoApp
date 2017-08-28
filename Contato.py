import datetime
from Telefone import Telefone
class Contato(Telefone):
    def __init__(self, pessoa, telefones):
        self.criacao = datetime.datetime().strftime("%y-%m-%d")
        self.pessoa = pessoa
        self.telefones = telefones

    def listarTelefone(self):
        for Telefone in self.Telefone:
            print (Telefone)
        def __str__ (self):
            return"%s" % (self.Telefone)
