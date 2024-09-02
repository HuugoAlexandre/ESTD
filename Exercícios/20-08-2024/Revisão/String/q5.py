def nome_normas_bibliografia(nome_completo: str):
    lista = nome_completo.split()
    ultimo_nome = lista[-1]
    primeiro_nome_primeira_letra = lista[0][0]
    segundo_nome_primeira_letra = lista[1][0]
    return f"{ultimo_nome.capitalize()}, {primeiro_nome_primeira_letra.capitalize()}. {segundo_nome_primeira_letra.capitalize()}."

print(nome_normas_bibliografia("antônio carlos jobim"))