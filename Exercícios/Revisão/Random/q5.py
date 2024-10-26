def verifica_paridade(numero):
    if numero % 2 == 0:
        numero = numero / 2
    else:
        numero = 3 * numero + 1
    return numero

x = 4
print("Antes: ", x)
x = verifica_paridade(x)
print("Depois: ", x)