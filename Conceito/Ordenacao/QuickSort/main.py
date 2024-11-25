def quick_sort(lista):
    if len(lista) <= 1:  # Base da recursão: uma lista com 0 ou 1 elemento já está ordenada
        return lista
    else:
        # Escolhendo o pivô (n precisa ser o último elemento)
        pivô = lista[-1]
        # Particionando a lista em duas: menores e maiores que o pivô
        menores = [x for x in lista[:-1] if x <= pivô]
        maiores = [x for x in lista[:-1] if x > pivô]
        # Recursão nas sublistas e juntando o resultado
        return quick_sort(menores) + [pivô] + quick_sort(maiores)
