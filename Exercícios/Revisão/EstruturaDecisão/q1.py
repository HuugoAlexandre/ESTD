nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
soma = nota1 + nota2
if soma/2 >= 7:
    if soma/2 == 10:
        print("Aprovado com distinção")
    else:
        print("Aprovado")
else:
    print("Reprovado")