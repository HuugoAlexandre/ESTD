def verifica_paridade(numero):
    if numero % 2 == 0:
        numero = numero / 2
    else:
        numero = 3 * numero + 1
    return numero

x = 40
s = ''
while True:
    s+= str(x) + ' -> '
    x = int(verifica_paridade(x))
    if x == 1:
        s+= '1'
        break
print(s)