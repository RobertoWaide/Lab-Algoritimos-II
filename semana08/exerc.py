def bank_historic(bank_account):
    while True:
        try:
            if bank_account["historic"] == []:
                raise ValueError("Não há movimentações de historico")
            print(bank_account["historic"])
            break
        except ValueError as error:
            print(error)
            break
        except BaseException as error:
            print("Erro detectado:",error)

def bank(bank_account):
    while True:
        try:
            print(f"Saldo atual: {bank_account['balance']}")
            break
        except BaseException as error:
            print("Erro detectado:",error)

def withdraw(bank_account):
    while True:
        try:
            cash = int(input("Digite o saque:"))
            if cash < 0:
                raise ValueError("Quantidade negativa")
            elif cash > bank_account["transaction_limit"]:
                raise ValueError("Quantia acima do limite")
            elif cash > bank_account["balance"]:
                raise ValueError("Saque acima do saldo")
            break
        except ValueError as error:
            print("Valor invalido:",error)
        except BaseException as error:
            print("Erro detectado:",error)

    bank_account["balance"] -= cash
    bank_account["historic"].append(f"Sacados R$ {cash}")
    return bank_account

def deposit(bank_account):
    while True:
        try:
            cash = int(input("Digite o deposito: "))
            if cash < 0:
                raise ValueError("Quantidade negativa")
            break
        except ValueError as error:
            print("Valor invalido:",error)
    bank_account["balance"] += cash
    bank_account["historic"].append(f"Depositados R$ {cash}")
    return bank_account

def manu(bank_account):
    while True:
        print("""1 - Depositar
2 - Sacar
3 - Verificar saldo
4 - Historico
5 - Sair""")
        while True:
            try:
                option = int(input("Digite a opção: "))
                if option < 1 or option > 5:
                    raise ValueError
                break
            except ValueError:
                print("Opção inavida!")
            except BaseException as error:
                print("Erro detectado:",error)
        
        if option == 1:
            deposit(bank_account)
        elif option == 2:
            withdraw(bank_account)
        elif option == 3:
            bank(bank_account)
        elif option == 4:
            bank_historic(bank_account)
        elif option == 5:
            print("Encerrando sistema")
            break

def main():
    bank_account = {"balance" : 3000,
                    "transaction_limit" : 1000,
                    "historic" : []}
    manu(bank_account)

main()
