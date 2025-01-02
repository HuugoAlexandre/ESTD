from main import *

fila = FilaArray()

# Adiciona elementos na fila
fila.enqueue(10)
fila.enqueue(20)
fila.enqueue(30)

# Consulta o elemento no início
print(fila.peek())  # Saída: 10

# Remove elementos
print(fila.dequeue())  # Saída: 10
print(fila.dequeue())  # Saída: 20

# Verifica se está vazia
print(fila.is_empty())  # Saída: False

# Remove o último elemento
print(fila.dequeue())  # Saída: 30

# Verifica novamente
print(fila.is_empty())  # Saída: True
