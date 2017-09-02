import json
import time
from Telefone import Telefone
from Pessoa import Pessoa
from Contato import Contato
class Agenda():
    def __init__(self, nomeProprietario, nascimentoProprietario, emailProprietario,contatos):
        self.proprietario = Pessoa(nomeProprietario,nascimentoProprietario,emailProprietario)
        p = open("Proprietario.json","w")
        proprietario = json.dumps(self.proprietario.__dict__)
        p.write(proprietario)
        p.close()
        self.contatos = contatos
        self.salvarContatos()


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
        telefones.append(telefone.__dict__)
        outroTelefone = eval(input("Adicionar outro telefone?(1)-sim,(2)-não"))
        #talvez seja bom usar excessão aqui tbm
        while outroTelefone == 1:
            codigoPais = input("Código do país:")
            ddd = input("DDD:")
            numero = input("Número:")
            telefone = Telefone(numero, ddd, codigoPais)
            telefones.append(telefone.__dict__)
            outroTelefone = eval(input("Adicionar outro telefone?(1)-sim,(2)-não:"))
        contato = Contato(pessoa.__dict__,telefones)
        self.contatos.append(contato.__dict__)
        self.salvarContatos()

    def ListarContato (self):
        print()
        for contato in self.contatos:
            pessoa = contato['pessoa']
            print(pessoa['nome'])

    def pesquisarContato(self,opcao):
        nome = input("Digite o nome do contato:")
        nome = nome.lower()
        for contato in self.contatos:
            pessoa = contato['pessoa']
            telefones =contato['telefones']
            if pessoa['nome'].lower() == nome:
                if opcao == 1:
                    print("->Email:",pessoa['email'])
                    print("->Telefones:")
                    for telefone in telefones:
                        print("%s(%s)%s"%(telefone['CodigoPais'], telefone['DDD'], telefone['Numero']))
                    break
                elif opcao == 2:
                    self.contatos.remove(contato)
                    print("Excluindo...")
                    time.sleep(2)
                    print("Contato excluído.")
                    self.salvarContatos()
                    break
            if self.contatos[len(self.contatos)-1] == contato:
                print("Contato não encontrado.")

    def QuantContatos(self):
        print("\nEssa agenda tem %i contato(s)."%len(self.contatos))

    def ExcluirContato(self):
        p = self.pesquisarContato(2)

    def salvarContatos(self):
        arquivo = open("Agenda.json", "w")
        contatos_jsn = json.dumps(self.contatos)
        arquivo.write(contatos_jsn)
        arquivo.close()
