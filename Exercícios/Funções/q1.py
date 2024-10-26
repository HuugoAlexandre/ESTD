def fatorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return None
    return n * fatorial(n-1)

print(fatorial(5))