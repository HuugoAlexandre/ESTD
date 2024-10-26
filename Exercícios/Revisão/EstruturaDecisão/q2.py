notas = list()

for i in range(1, 4):
    num = float(input(f"Número {i}: "))
    notas.append(num)

if notas[0] >= notas[1] and notas[0] >= notas[2]:
    maior = notas[0]
elif notas[1] >= notas[0] and notas[1] >= notas[2]:
    maior = notas[1]
else:
    maior = notas[2]

if notas[0] <= notas[1] and notas[0] <= notas[2]:
    menor = notas[0]
elif notas[1] <= notas[0] and notas[1] <= notas[2]:
    menor = notas[1]
else:
    menor = notas[2]

print("Maior: ", maior)
print("Menor: ", menor)