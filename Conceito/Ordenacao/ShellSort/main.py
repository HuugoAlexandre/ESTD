def shell_sort(uma_lista):
    contador_sublista = len(uma_lista)//2
    while contador_sublista > 0:
        for posicao_inicial in range(contador_sublista):
            InsertionSortComGap(uma_lista,posicao_inicial,contador_sublista)
        print("Após incrementos de tamanho",contador_sublista,

        "a lista é",uma_lista)
        contador_sublista = contador_sublista // 2
    return uma_lista

def InsertionSortComGap(uma_lista,inicio,gap):
    for i in range(inicio+gap,len(uma_lista),gap):
        currentvalue = uma_lista[i]
        position = i
        while position>=gap and uma_lista[position-gap]>currentvalue:
            uma_lista[position]=uma_lista[position-gap]
            position = position-gap
        uma_lista[position]=currentvalue
