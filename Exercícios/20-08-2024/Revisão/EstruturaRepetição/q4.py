numeros = list()
for i in range(1,6):
    numero = int(input(f"{i}° número: "))
    numeros.append(numero)

maior = 0
for i in numeros:
    if i > maior:
        maior = i

print(f"O maior dos números fornecidos é: {maior}")