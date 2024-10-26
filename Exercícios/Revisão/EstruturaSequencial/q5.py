altura = float(input("Altura: "))
sexo = input("Sexo (h ou m): ")
if sexo == 'h' or sexo == 'H':
    pesoIdeal = (72.7 * altura) - 58
elif sexo == 'm' or sexo == 'M':
    pesoIdeal = (62.1 * altura) - 44.7
else:
    print("Inválido")
print("Peso ideal: ", pesoIdeal)