def main():
    while True:
        try:
            a = int(input("Digite o primeiro lado: "))
            b = int(input("Digite o segundo lado: "))
            c = int(input("Digite o terceiro lado: "))


            if a+b < c or b+c < a or c+a < b:
                raise ValueError("Triângulo inválido")

            if a == b == c:
                print("\nTriângulo equilátero")
            elif a == b or b == c or c == a:
                print("\nTriângulo isósceles")
            else:
                print("\nTriângulo escaleno")

        except ValueError as error:
            print(error)
        except BaseException as error:
            print(error)

main()
