def eh_data_valida(dia, mes, ano):
    if dia < 0 or dia > 31:
        return False
    elif mes < 0 or mes > 12:
        return False
    elif ano < 0 or ano > 2024:
        return False
    return True
