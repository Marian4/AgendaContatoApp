import datetime
class Pessoa():
    def main(self, nome, nascimento, email):
        self.nome = nome
        self.nascimento = nascimento(datetime.date(2001, 4, 26))
        self.email = email('proprietario@hotmail.com')

class Agenda():
    def main(self, proprietario):
        self.proprietario = proprietario(Pessoa)