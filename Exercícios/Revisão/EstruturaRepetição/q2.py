while True:
    nome_usuario = input("Nome de usuário: ")
    senha = input("Senha: ")
    if senha == nome_usuario:
        print("Senha não pode ser igual o nome de usuário.")
        continue
    break