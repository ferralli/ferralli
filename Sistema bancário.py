menu = """
[1] Depositar
[2] Sacar 
[3] Extrato
[0] Sair 
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3  

while True:

    opcao = input(menu)

    if opcao == "1":  
        valor = float(input("Quanto você quer depositar? "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Erro na operação! O valor informado é inválido.")

    elif opcao == "2":  
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha na operação! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Falha na operação! O valor excede o limite.")
        elif excedeu_saques:
            print("Falha na operação! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor  
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Falha na operação! O valor informado é inválido.")

    elif opcao == "3":  
        print('\n============= EXTRATO =============')
        print("Sem movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================")

    elif opcao == "0":  
        break

    else:
        print("Erro! Por favor, selecione uma opção válida.")
