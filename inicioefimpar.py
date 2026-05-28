inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))

while inicio <= fim:
    if inicio % 2 == 0:
        print(inicio, end=" ")
    inicio += 1
