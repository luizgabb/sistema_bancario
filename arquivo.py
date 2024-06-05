menu = f"""
   \n ===== MENU =====
    Digite [d] para Depósitar
    Digite [s] para Sacar
    Digite [e] para Ver o Extrato
    Digite [q] para sair

    ==>
""" 
SAQUES_DIARIOS = 3
saldo = 0
limite = 500
extrato =""
numero_saques = 0

while True: 

    opcao =input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor do Depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"

        else:
            print("Operação falhou! o valor informado é invalido!")

    elif opcao == "s":
        valor = float(input("Digite o valor do saque:"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= SAQUES_DIARIOS

        if excedeu_saldo: 
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite: 
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou!O numero máximo de saques foi atingido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1

        else :
            print("Operação falhou! O valor inoformado é invalido.")

    elif opcao == "e": 
        print("\n===== EXTRATO =====")
        print("Não foram realizadas movimentações!" if not extrato else extrato) #verifica se o extrato ta vazio ou se ja houve movimentação
        print(f"\nSaldo: R${saldo:.2f}")

    elif opcao == "q":
        print("Você saiu!")
        break

    else: 
        print("Operação invalida!, por favor selecione novamente a opção desejada.")

