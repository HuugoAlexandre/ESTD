def troca_palavra(texto: str, palavra_antiga: str, palavra_nova: str):
    novo_texto = ''
    palavras = texto.split()

    for palavra in palavras:
        if palavra == palavra_antiga:
            novo_texto+= palavra_nova
        else:
            novo_texto+= palavra
        novo_texto+= " "

    novo_texto = novo_texto.strip() # por conta do último espaço da última iteração
    return novo_texto

print(troca_palavra("claudia da silva", "silva", "conceição"))