def busca_binaria(uma_lista, item_pesquisado):
    inicio = 0
    fim = len(uma_lista) - 1
    encontrou = False
    while inicio <= fim and not encontrou:
        meio = (inicio + fim) // 2
        if uma_lista[meio] == item_pesquisado:
            encontrou = True
        else:
            if item_pesquisado < uma_lista[meio]:
                fim = meio - 1
            else:
                inicio = meio + 1
    return encontrou

lista_teste = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print('Procurando 3 na lista',lista_teste)
print('resultado',busca_binaria(lista_teste, 3))
print('Procurando 13 na lista',lista_teste)
print('resultado',busca_binaria(lista_teste, 13))