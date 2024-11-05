"""
11. Apresente uma versão recursiva da busca binária em Python. Explique como a recursão
funciona nesse caso.
"""
def busca_binaria_recursiva(uma_lista, item_procurado, inicio=0, fim=None):
    if fim is None:
        fim = len(uma_lista) - 1
    
    if inicio > fim:
        return -1
    
    meio = (inicio + fim) // 2
    if uma_lista[meio] == item_procurado:
        return meio
    elif uma_lista[meio] < item_procurado:
        return busca_binaria_recursiva(uma_lista, item_procurado, meio + 1, fim)
    else:
        return busca_binaria_recursiva(uma_lista, item_procurado, inicio, meio - 1)

# Exemplo de uso
lista_de_numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
item_a_procurar = 10
resultado = busca_binaria_recursiva(lista_de_numeros, item_a_procurar)

if resultado != -1:
    print(f"O número {item_a_procurar} foi encontrado no índice {resultado}.")
else:
    print(f"O número {item_a_procurar} não foi encontrado na lista.")
