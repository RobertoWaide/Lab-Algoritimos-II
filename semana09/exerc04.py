def listagem(lista):
    while True:
        try:
            position = int(input("Digite a posição que procur o produto: "))

            print(f"Item {position}: {lista[position-1]}")
            break
        except ValueError as error:
            print(error)
        except IndexError:
            print("Posição for da lista")
        except BaseException as error:
            print(error)


def main():
    lista = ["Maça","Banana","Abacaxi","Pera","Carne","Batata"]
    listagem(lista)


main()
