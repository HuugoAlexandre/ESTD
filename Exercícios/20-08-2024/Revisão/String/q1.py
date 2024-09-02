def inverte_palavra(palavra: str):
    palavra = palavra.lower()
    tamanho = len(palavra)
    palavra_invertida = ''
    while tamanho != 0:
        palavra_invertida+=palavra[tamanho-1]
        tamanho-=1

    return palavra_invertida

def verifica_palindroma(palavra: str):
    if palavra.lower() == inverte_palavra(palavra):
        print(f"{palavra} é uma palavra palíndroma")
    else:
        print(f"{palavra} não é uma palavra palíndroma")

verifica_palindroma("hugo")
verifica_palindroma("Raiar")
