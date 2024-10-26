def fatorial(numero):
    if numero == 1 or numero == 0:
        return 1
    elif numero < 0:
        return None
    return numero * fatorial(numero - 1)

print(fatorial(4))