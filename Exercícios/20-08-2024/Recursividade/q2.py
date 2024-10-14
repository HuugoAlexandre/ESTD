def inverte_palavra(palavra):
    if len(palavra) == 1:
        return palavra
    
    return inverte_palavra(palavra[1:]) + palavra[0]

print(inverte_palavra("python"))