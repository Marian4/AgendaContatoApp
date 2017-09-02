import time
import json
from Agenda import Agenda

def main():
    try:
        contatos = open("Agenda.json", "r")
        print("=========== Agenda aberta. ===========")
        p = open("Proprietario.json","r")
        proprietario = json.load(p)
        a1 = Agenda(proprietario['nome'], proprietario['nascimento'], proprietario['email'], json.load(contatos))
    except FileNotFoundError:
        print("=========== Crie sua agenda! ===========\n")
        nomep = input("Digite seu nome:")
        nascimentop = input("Digite a data do seu nascimento:")
        emailp = input("Digite seu email:")
        a1 = Agenda(nomep,nascimentop,emailp,[])

    while True:
        print("\nEscolha uma opção: ")
        print("1- Adicionar contato")
        print("2- Listar Contatos")
        print("3- Pesquisar contato")
        print("4- Quantidade de contatos")
        print("5- Remover contato")
        print("6- Sair")
        opcao = int(input())

        if opcao == 1:
            a1.AdicionaContato()
        elif opcao == 2:
            a1.ListarContato()
        elif opcao == 3:
            a1.pesquisarContato(1)
        elif opcao == 4:
            a1.QuantContatos()
        elif opcao == 5:
            a1.ExcluirContato()
        elif opcao == 6:
            print("=========== Saindo... ===========")
            time.sleep(2)
            print("=========== Você saiu. ===========")
            break


if __name__ == '__main__':
    main()
