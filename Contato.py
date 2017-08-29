import datetime
from Telefone import Telefone
class Contato(Telefone):
    def __init__(self, pessoa, telefones):
        self.criacao = datetime.date.today().strftime("%y/%m/%d")
        self.pessoa = pessoa
        self.telefones = telefones

    def listarTelefone(self):
        for telefone in self.telefones:
            print (telefone)
        '''def __str__ (self):
            return"%s" % (self.telefone)'''
