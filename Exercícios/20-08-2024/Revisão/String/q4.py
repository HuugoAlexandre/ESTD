def formatacao_nome(texto: str):
    lista = texto.split()
    ultimo_nome = lista[-1]
    primeiro_nome = lista[0]
    return f"{ultimo_nome}/{primeiro_nome}"

print(formatacao_nome("Carlos Drumond de Andrade "))