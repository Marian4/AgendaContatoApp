import json
from Agenda import Agenda
from Contato import Contato
from Pessoa import Pessoa
from Telefone import Telefone

def main():
    a1 = Agenda("sajdn")

    #a1.AdicionaContado(Contato(Pessoa("Rennan", "23/34/323245", "hotmail").__dict__, [Telefone("8888", 83, "+55").__dict__]).__dict__)
    #a1.salvarContatos()



    while True:
        print("Escolha uma opção: ")
        print("1- Adicionar contato")
        print("2- Listar Contatos")
        print("3- Pesquisar contato")
        print("4- Quantidade de contatos")
        print("5- Remover contato")
        print("6- Sair")
        opcao = int(input())

        if opcao == 1:
            a1.AdicionaContado(Pessoa)
        elif opcao == 2:
            a1.ListarContato()
        elif opcao == 3:
            a1.pesquisar()
        elif opcao == 4:
            a1.QuantContatos()
        elif opcao == 5:
            a1.ExcluirContato()
        elif opcao == 6:
            break


if __name__ == '__main__':
    main()
