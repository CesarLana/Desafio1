
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[ss] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("informe o valor do deposito: ")) 
      
        if valor > 0:
            saldo +=valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("A Operação falhou! Tente Noamente.")

        
    elif opcao == "s":
        valor = float(input("informe o valor do saque: "))
        
        execedeu_saldo = valor > saldo
        execedeu_limite = valor > limite
        execedeu_saques = numero_saques >= LIMITE_SAQUES

        if execedeu_saldo: 
            print("vc nao tem saldo suficiente!")

        elif execedeu_limite:
            print("o valor do saque exede o limite")

        elif execedeu_saques:
            print("o valor do saque se foi")  

        if valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1 

        else:
            print("o valor é invalido")
    
    elif opcao == "e":
    
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
