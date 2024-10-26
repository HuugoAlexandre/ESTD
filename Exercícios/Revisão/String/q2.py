def contar_palavras(texto: str):
    lista = texto.split()
    return len(lista)

conto = "Este é um conto de um garoto engraçado..."
print(contar_palavras(conto))