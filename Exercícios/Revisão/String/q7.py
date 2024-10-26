def gerar_login(nome_completo):
    palavras = nome_completo.split()    
    login = ''.join([palavra[0] for palavra in palavras]).lower()
    return login

nome = "Maria da Silva"
login = gerar_login(nome)
print(f"O login gerado para '{nome}' é: {login}")
