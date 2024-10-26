numeros = list()
for i in range(1, 6):
    numero = int(input(f"{i}° número: "))
    numeros.append(numero)

soma = 0
for i in numeros:
    soma+=i

media = soma/len(numeros)

print(f"Soma: {soma}\nMédia: {media}")