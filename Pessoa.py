'''
    Pessoa - Agregação de contato.
'''
class Pessoa():
    def __init__ (self, nome, nascimento, email):
        global Agenda
        self.nome = nome
        self.nascimento = nascimento
        self.email = email

