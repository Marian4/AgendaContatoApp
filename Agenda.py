import json
from Telefone import Telefone
class Agenda():
    def __init__(self, proprietario):
        self.proprietario = proprietario
        self.contatos = {}
        self.quantContatos = 0

    def AdicionaContato (self):
        nome = input("Digite o nome do contato:")
        #pedir nascimento
        #peidr email
        pessoa = input("Digite o nome do contato:")
        ddd = input("Digite o ddd:")
        numero = input("Digite o número:")
        codigoPais = input("Digite o codigoPais:")
        telefone = Telefone(numero,ddd,codigoPais)
        self.contatos[pessoa] = numero
        self.quantContatos += 1

    def ListarContato (self):
        for contato in self.contatos:
            print (contato,":+%s(%s) %s"%(self.contatos[contato].CodigoPais, self.contatos[contato].DDD, self.contatos[contato].Numero))
        '''def __str__ (self):
            return"%s" % (self.contatos)'''

    def pesquisar(self):
        nome = input("Digite o nome do contato:")
        nome = nome.lower()
        for contato in self.contatos:
            if contato.lower == nome:
                print(contato, ":+%s(%s) %s" % (
                self.contatos[contato].CodigoPais, self.contatos[contato].DDD, self.contatos[contato].Numero))




    def QuantContatos(self):
        print("Essa agenda tem %i contatos."%self.quantContatos)

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
