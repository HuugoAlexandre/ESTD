class NohDuplo:
    def __init__(self, valor_inicial):
        self.dados = valor_inicial
        self.proximo = None
        self.anterior = None

    def get_data(self):
        return self.dados

    def get_next(self):
        return self.proximo

    def get_prev(self):
        return self.anterior

    def set_next(self, novo_proximo):
        self.proximo = novo_proximo

    def set_prev(self, novo_anterior):
        self.anterior = novo_anterior

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    # Adiciona um item ao final da lista
    def append(self, item):
        novo_noh = NohDuplo(item)
        if self.is_empty():
            self.head = novo_noh
            self.tail = novo_noh
        else:
            self.tail.set_next(novo_noh)  # Atualiza o próximo do último nó
            novo_noh.set_prev(self.tail)   # Atualiza o anterior do novo nó
            self.tail = novo_noh           # Atualiza o tail para o novo nó

    def remove(self, item):
        atual = self.head
        while atual is not None:
            if atual.get_data() == item:
                # Caso o nó seja o único na lista
                if atual == self.head and atual == self.tail:
                    self.head = None
                    self.tail = None
                # Caso o nó seja o primeiro
                elif atual == self.head:
                    self.head = atual.get_next()
                    self.head.set_prev(None)
                # Caso o nó seja o último
                elif atual == self.tail:
                    self.tail = atual.get_prev()
                    self.tail.set_next(None)
                # Caso o nó esteja no meio
                else:
                    anterior = atual.get_prev()
                    proximo = atual.get_next()
                    anterior.set_next(proximo)
                    proximo.set_prev(anterior)
                return
            atual = atual.get_next()
        raise ValueError(f"Item {item} não encontrado na lista.")

    def pop(self):
        if self.is_empty():
            raise IndexError("A lista está vazia.")
        valor = self.tail.get_data()
        if self.head == self.tail:  # Se há apenas um nó
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
        return valor

    def __repr__(self):
        elementos = []
        atual = self.head
        while atual is not None:
            elementos.append(str(atual.get_data()))
            atual = atual.get_next()
        return " <-> ".join(elementos)

lista = ListaDuplamenteEncadeada()
lista.append(1)
lista.append(2)
lista.append(3)
print("Lista após adição:", lista)

lista.remove(2)
print("Lista após remoção do 2:", lista)

ultimo = lista.pop()
print("Último elemento removido:", ultimo)
print("Lista após pop:", lista)

try:
    lista.remove(4)  # Deve levantar um erro
except ValueError as e:
    print(e)
