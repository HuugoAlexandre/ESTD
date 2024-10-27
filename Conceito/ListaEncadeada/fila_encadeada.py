class Noh:
    def __init__(self, valor):
        self.dados = valor
        self.proximo = None

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def is_empty(self):
        return self.inicio is None

    def enqueue(self, valor):
        novo_noh = Noh(valor)
        if self.is_empty():
            self.inicio = novo_noh
            self.fim = novo_noh
        else:
            self.fim.proximo = novo_noh
            self.fim = novo_noh
        self.tamanho += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("A fila está vazia.")
        valor_removido = self.inicio.dados
        self.inicio = self.inicio.proximo
        if self.inicio is None:  # Caso a fila fique vazia
            self.fim = None
        self.tamanho -= 1
        return valor_removido

    def peek(self):
        if self.is_empty():
            raise IndexError("A fila está vazia.")
        return self.inicio.dados

    def size(self):
        return self.tamanho

    def __repr__(self):
        elementos = []
        atual = self.inicio
        while atual is not None:
            elementos.append(str(atual.dados))
            atual = atual.proximo
        return " <- ".join(elementos)

fila = Fila()
fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
print(fila)
fila.dequeue()
fila.dequeue()
print(fila)


