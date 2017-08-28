import json

class Agenda():
    def __init__(self, proprietario):
        self.proprietario = proprietario
        self.contatos = []

    def AdicionaContado (self, contato):
        self.contatos.append(contato)

    def ListarContato (self):
        for contatos in self.contatos:
            print (contatos)
        def __str__ (self):
            return"%s" % (self.contatos)

    def pesquisar(self, nome):
        nome = nome.lower()
        for a, b in enumerate (Agenda) :
            if b [0].lower() == nome :
                return (a)

        return (None)

    def QuantContatos(self):
        return len(self.contatos)

    def ExcluirContato(self, nome):
        p = self.pesquisar(nome)

        if p != None:
            del self.contatos[p]
        while True:
            try:
                p == None
                break
            except:
                print("Nao encontrado")

    def salvarContatos(self):
        f = open("Agenda.json", "w")

        dic = json.dumps(self.contatos)
        f.write(dic)
        f.close()