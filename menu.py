opcao = 0

while opcao != 3:
    print("\nMENU")
    print("1. Somar dois números")
    print("2. Subtrair dois números")
    print("3. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print("Resultado =", a + b)
    elif opcao == 2:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print("Resultado =", a - b)
    elif opcao == 3:
        print("Encerrando o programa...")
    else:
        print("Opção inválida.")
