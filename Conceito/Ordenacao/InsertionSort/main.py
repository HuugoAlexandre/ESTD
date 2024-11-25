def insertion_sort(uma_lista):
    for index in range(1,len(uma_lista)):
        valor_atual = uma_lista[index]
        posicao = index
        while posicao>0 and uma_lista[posicao-1]>valor_atual:
            uma_lista[posicao]=uma_lista[posicao-1]
            posicao = posicao-1
        uma_lista[posicao]=valor_atual
    return uma_lista