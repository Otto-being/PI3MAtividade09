horas = int(input("Quantas horas serão registradas? "))

contador = 1
total = 0

while contador <= horas:
    producao = int(input(f"Produção da hora {contador}: "))
    total += producao
    contador += 1

media = total / horas if horas > 0 else 0

print("Produção total =", total)
print("Produção média por hora =", media)
