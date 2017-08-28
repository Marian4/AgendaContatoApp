import datetime
class Agenda():
    def main(self, proprietario, contato):
        self.proprietario = proprietario
        self.contato = contato[]

    def NovoContado (self):
        pass

    def ListarContato (self):
        pass

    def ExcluirContato (self):
        pass

    def QuantContatos(self):
        pass


class Pessoa():
    def main(self, nome, nascimento, email):
        global Agenda
        self.nome = nome
        self.nascimento = nascimento(datetime.date(2001, 4, 26))
        self.email = email
        Agenda.append([nome, nascimento, email])

    def pesquisa(nome) :
        nome = nome.lower()
        for a, b in enumerate (Agenda) :
            if b [0].lower() == nome :
                return (a)
            return (None)
