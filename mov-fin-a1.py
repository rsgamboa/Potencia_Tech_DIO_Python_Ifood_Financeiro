menu ="""

[d] Despositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMIT_SAQUES = 3 

while True:

    opcao = input(menu)

    if opcao == "q":
        break

    elif opcao == "d":
        valor = float(input("Informe o valor do deposito: "))
        saldo += valor
        extrato += "Depósito: " + str(valor) + "\n"

    elif opcao == "s":
        if numero_saques < LIMIT_SAQUES:
            valor = float(input("Valor: "))
            if valor <= saldo + limite:
                saldo -= valor
                extrato += "Saque: " + str(valor) + "\n"
                numero_saques += 1
            else:
                print("Saldo insuficiente!")
        else:
            print("Limite de saques atingido!")

    elif opcao == "e":
        print("Saldo: ", saldo)
        print("Limite: ", limite)
        print(extrato)

    else:
        print("Opção inválida!")