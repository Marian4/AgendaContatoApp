import json
def menu():
    print("1- Adicionar contato")
    print("2- Editar contato")
    print("3-Pesquisar contato")
    print("4-Visualisar lista de contatos")
    print("5-Aapagar contato")
    print("6- Sair")

 
while True:
    opção = menu()
    if opção == 6
        break

def main():
    while True:
        try:
            f = open("meses.txt", encoding="utf8")
            linhas = f.readlines()

            for linha in linhas:
                print(linha.strip())

            break

        except FileNotFoundError:
            print("arquivo não encontrado")


if __name__ == '__main__':
    main()
