def soma_fibonacci(termo):
    if termo == 0:
        return 0
    elif termo == 1:
        return 1
    
    a, b = 0, 1
    soma = a + b

    for _ in range(2, termo):
        a, b = b, a + b
        soma += b
    return soma

print(soma_fibonacci(7))