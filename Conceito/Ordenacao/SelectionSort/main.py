def selection_sort(uma_lista):
    for posicao_verificada in range(len(uma_lista)-1,0,-1):
        posicao_maior = 0
        for posicao in range(1,posicao_verificada+1):
            if uma_lista[posicao]>uma_lista[posicao_maior]:
                posicao_maior = posicao
            temp = uma_lista[posicao_verificada]
            uma_lista[posicao_verificada] = uma_lista[posicao_maior]
            uma_lista[posicao_maior] = temp
    return uma_lista