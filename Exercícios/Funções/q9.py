def eh_bissexto(ano: str):
    temp = ano[-2] + ano[-1]
    return True if int(temp) % 4 == 0 else False
