def busca_binaria_recursiva(uma_lista, item_procurado):
    if len(uma_lista) == 0:
        return False
    else:
        meio = len(uma_lista) // 2
        print("####")
        print("Indice: ", meio)
        print("Lista: ", uma_lista)
        print("Elemento: ", uma_lista[meio])
        print("####")
        print()
        if uma_lista[meio]==item_procurado:
            print('Achei o número', item_procurado)
            return True
        else:
            if item_procurado < uma_lista[meio]:
                return busca_binaria_recursiva(uma_lista[:meio], item_procurado)
            else:
                return busca_binaria_recursiva(uma_lista[meio + 1:], item_procurado)

# teste = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]
teste = [2, 4, 6, 8, 10]
newlist = [x for x in range(1000)]
busca_binaria_recursiva(newlist, 500)