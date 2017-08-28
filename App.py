import json
from Agenda import Agenda
from Contato import Contato
from Pessoa import Pessoa
from Telefone import Telefone

def menu():
    print("1- Adicionar contato")
    print("2-Listar Contatos")
    print("3-Pesquisar contato")
    print("4- Quantidade de contatos")
    print("5- Remover contato")
    print("6- Sair")

while True:
    opção = menu()
    if opção == 6:
        break
    elif opção == 1:
        Agenda()
    elif opção == 2:
        Editar()
    elif opção == 3:
        pesquisa2()
    elif opção == 4:
        listar()
    elif opção == 5:
        apagar()

def main():

    a1 = Agenda("sajdn")
    a1.AdicionaContado(Contato(Pessoa("Rennan", "23/34/323245", "hotmail").__dict__, [Telefone("8888", 83, "+55").__dict__]).__dict__)
    a1.salvarContatos()



if __name__ == '__main__':
    main()
