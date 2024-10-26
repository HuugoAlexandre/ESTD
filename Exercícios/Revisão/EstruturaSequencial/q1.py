soma_das_notas = 0
for i in range(1, 5):
    nota = float(input(f"Nota {i}: "))
    soma_das_notas+=nota

media = soma_das_notas/4
print(media)
