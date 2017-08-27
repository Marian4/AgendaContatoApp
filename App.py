import json
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