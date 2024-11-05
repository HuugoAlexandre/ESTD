"""
Implemente a busca binária usando recursividade sem o operador slice. Você precisará passar
o índice dos valores iniciais e finais na sublistas.
"""

def busca_binaria_recursiva(uma_lista, item_procurado, inicio, fim):
    if inicio > fim:
        return False
    
    meio = (inicio + fim) // 2
    print("Meio: ", meio)

    if uma_lista[meio] == item_procurado:
        print("Achei o número: ", item_procurado)
        return True
    else:
        print("####")
        print("Indice: ", meio)
        print("Elemento: ", uma_lista[meio])
        print("####")
        print()
        if item_procurado < uma_lista[meio]:
                return busca_binaria_recursiva(uma_lista, item_procurado, inicio, meio -1)
        else:
            return busca_binaria_recursiva(uma_lista, item_procurado, meio + 1, fim)

newlist = [x for x in range(0, 1000, 2)]
busca_binaria_recursiva(newlist, 500, 0, len(newlist) - 1)