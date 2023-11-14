def main():
    while True:
        try:
            note = int(input("Dê uma avaliação ao produto (0-10):"))

            assert note < 10 and note > 0, "Valor fora da escala!"
            print("Obrigado pela review!")
            break

        except ValueError:
            print("Valor invalido!")
        except AssertionError as error:
            print(error)
        except BaseException as error:
            print(error)

main()
