def eh_primo(numero):
    for i in range(2, numero // 2 + 1):
        if numero % i == 0 or numero < 2:
            return False
    return True
