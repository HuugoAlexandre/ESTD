ano = input("Ano: ")
temp = ano[-2] + ano[-1]
if int(temp) % 4 == 0:
    print("Bissexto")
else:
    print("Não é bissexto")
