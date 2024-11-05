"""
Gere uma lista de números aleatórios, ordene-os e verifique o desempenho dos algoritmos de
busca sequencial binária com slide, binária sem slide.
"""
import random
import time

tamanho_lista = 1000000
lista = [random.randint(1, 1000000) for _ in range(tamanho_lista)]
lista.sort()

def busca_sequencial(lista, numero):
    for i in range(len(lista)):
        if lista[i] == numero:
            print(f"O número {numero} está na lista na posição {i}")
            return i
    return -1

def busca_binaria_com_slice(lista, numero):
    if len(lista) == 0:
        return -1
    meio = len(lista) // 2
    if lista[meio] == numero:
        return meio
    elif numero < lista[meio]:
        return busca_binaria_com_slice(lista[:meio], numero)
    else:
        resultado = busca_binaria_com_slice(lista[meio + 1:], numero)
        if resultado != -1:
            return meio + 1 + resultado  # Ajusta o índice corretamente
        return -1

def busca_binaria_sem_slice(lista, numero, inicio, fim):
    if inicio > fim:
        return -1
    meio = (inicio + fim) // 2
    if lista[meio] == numero:
        print(f"O número {numero} está na lista na posição {meio}")
        return meio
    elif numero < lista[meio]:
        return busca_binaria_sem_slice(lista, numero, inicio, meio - 1)
    else:
        return busca_binaria_sem_slice(lista, numero, meio + 1, fim)
    
numero_a_buscar = random.randint(1, 1000000)
print("Número a buscar: ", numero_a_buscar)
print()

# Medindo o tempo da busca sequencial
start_time = time.time()
resultado_sequencial = busca_sequencial(lista, numero_a_buscar)
end_time = time.time()
print(f"Índice da busca sequencial: {resultado_sequencial}, Tempo: {end_time - start_time:.6f} segundos")
print()

# Medindo o tempo da busca binária com slice
start_time = time.time()
resultado_binaria_com_slice = busca_binaria_com_slice(lista, numero_a_buscar)
end_time = time.time()
print(f"Índice da busca binária com slice: {resultado_binaria_com_slice}, Tempo: {end_time - start_time:.6f} segundos")
print()

# Medindo o tempo da busca binária sem slice
start_time = time.time()
resultado_binaria_sem_slice = busca_binaria_sem_slice(lista, numero_a_buscar, 0, len(lista) - 1)
end_time = time.time()
print(f"Índice da busca binária sem slice: {resultado_binaria_sem_slice}, Tempo: {end_time - start_time:.6f} segundos")
