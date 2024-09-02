lados = list()
for i in range(1, 4):
    lado = float(input(f"{i}° lado: "))
    lados.append(lado)

if lados[0] + lados[1] > lados[2] and lados[1] + lados[2] > lados[0] and lados[0] + lados[2] > lados[1]:
    if lados[0] == lados[1] and lados[0] == lados[2]:
        print("Triângulo Equilátero")
    elif lados[0] == lados[1] or lados[0] == lados[2] or lados[1] == lados[2]:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")

else:
    print("Não pode ser triângulo.")