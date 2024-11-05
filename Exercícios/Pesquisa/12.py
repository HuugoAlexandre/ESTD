"""
Crie uma função de pesquisa binária que retorne todos os índices de um número em uma lista
ordenada que pode conter duplicatas.
"""
def pesquisa_binaria(lista, numero):
    inicio = 0
    fim = len(lista) - 1
    indices = []

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == numero:
            indices.append(meio)
            # Procura para a esquerda e para a direita

            # Buscando à esquerda
            left = meio - 1
            while left >= inicio and lista[left] == numero:
                indices.append(left)
                left -= 1

            # Buscando à direita
            right = meio + 1
            while right <= fim and lista[right] == numero:
                indices.append(right)
                right += 1
            break
        elif numero < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    return sorted(indices)

lista = [1,2,3,4,4,5,5,6,7,8,9,10]
print(pesquisa_binaria(lista, 5))