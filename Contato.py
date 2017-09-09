'''
    Contato - lista os telefones da agenda
'''
import datetime
class Contato():
    def __init__(self, pessoa, telefones):
        self.criacao = datetime.date.today().strftime("%d/%m/%Y")
        self.pessoa = pessoa
        self.telefones = telefones

    def listarTelefone(self):
        for telefone in self.telefones:
            print (telefone)
