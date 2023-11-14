class NegativeNumberError(Exception):
    pass

def calculate_square_root():
    while True:
        try:
            numb = int(input("Digite um numero para ver sua raiz: "))
            if numb < 1:
                raise NegativeNumberError("Numeros 0 abaixo não tem raiz")

            for i in range(numb):
                if i*i == numb:
                    print(f"A raiz de {numb} é {i}")
                    break
                if i+1 == numb:
                    print(f"{numb} não tem raiz exata")
            break
        except ValueError as error:
            print(error)
        except BaseException as error:
            print(error)




def main():
    calculate_square_root()

main()
