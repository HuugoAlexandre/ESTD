dia = int(input("Dia: "))
if dia < 0 or dia > 31:
    print("Dia inválido.")
    exit(1)
mes = int(input("Mês: "))
if mes < 0 or mes > 12:
    print("Mês inválido.")
    exit(1)
if mes < 10:
    mes = '0' + str(mes)
ano = int(input("Ano: "))
if ano < 1900 or ano > 2024: # Considerando que a data não posso ser maior que o presente ou menor que 1900
    print("Ano inválido.")
    exit(1)

print(f"{dia}/{mes}/{ano}")
    