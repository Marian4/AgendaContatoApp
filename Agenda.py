import json
from Telefone import Telefone
from Pessoa import Pessoa
from Contato import Contato
class Agenda():
    def __init__(self, nomeProprietario, nascimentoProprietario, emailProprietario):
        self.proprietario = Pessoa(nomeProprietario,nascimentoProprietario,emailProprietario)
        self.contatos = []


    def AdicionaContato (self):
        nome = input("Nome:")
        nascimento = input("Nascimento:")
        email = input("Email:")
        pessoa = Pessoa(nome,nascimento,email)
        telefones = []
        codigoPais = input("Código do país:")
        ddd = input("DDD:")
        numero = input("Número:")
        telefone = Telefone(numero,ddd,codigoPais)
        telefones.append(telefone)
        outroTelefone = eval(input("Adicionar outro telefone?(1)-sim,(2)-não"))
        while outroTelefone == 1:
            codigoPais = input("Código do país:")
            ddd = input("DDD:")
            numero = input("Número:")
            telefone = Telefone(numero, ddd, codigoPais)
            telefones.append(telefone)
            outroTelefone = eval(input("Adicionar outro telefone?(1)-sim,(2)-não"))
        contato = Contato(pessoa,telefones)
        self.contatos.append(contato)
    def ListarContato (self):
        for contato in self.contatos:
            print(contato.pessoa.nome)

    def pesquisarContato(self,opcao):
        nome = input("Digite o nome do contato:")
        nome = nome.lower()
        for contato in self.contatos:
            if contato.pessoa.nome.lower() == nome:
                if opcao == 1:
                    print("->Email:",contato.pessoa.email)
                    print("->Telefones:")
                    for telefone in contato.telefones:
                        print("%s(%s)%s"%(telefone.CodigoPais, telefone.DDD, telefone.Numero))
                elif opcao == 2:
                    self.contatos.remove(contato)
                    print("Contato excluído.")

    def QuantContatos(self):
        quantContatos = 0
        for i in self.contatos:
            quantContatos +=1
        print("\nEssa agenda tem %i contatos."%quantContatos)

    def ExcluirContato(self):
        p = self.pesquisarContato(2)
#botar uma certa coisa de opção no pesquisar que o usuário n vai precisar escolher o parametro opção vai receber 1 ou 2, no pesquisarcontatps vai ter o 1 e por isso vai mostrar os contatos da pessoa e o outro n
        '''if p != None:
            del self.contatos[p]
        while True:
            try:
                p == None
                break
            except:
                print("Nao encontrado")'''

    def salvarContatos(self):
        f = open("Agenda.json", "w")

        dic = json.dumps(self.contatos)
        f.write(dic)
        f.close()
