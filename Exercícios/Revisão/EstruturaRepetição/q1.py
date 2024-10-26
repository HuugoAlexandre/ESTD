while True:
    try:
        nota = input("Nota entre 0 e 10: ")
        nota = int(nota)
        if nota < 0 or nota > 10:
            print("Nota fora de intervalo.")
            continue
        print("Sua nota: ", nota)
        break
    except:
        print("Nota inválida.")
