def imprime_ultima_palavra(texto: str):
    lista = texto.split()
    return lista[-1]

print(imprime_ultima_palavra("José da Silva"))