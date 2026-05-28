soma = 0

print("Digite números inteiros (0 para encerrar):")

numero = int(input())
while numero != 0:
    soma += numero
    numero = int(input())

print("Soma total =", soma)
