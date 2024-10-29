class SetWithQueue:
    def __init__(self):
        self.itens = []
        self.inicio = 0
        self.tamanho = 0
        self.verifica_elemento = {}

    def size(self):
        return self.tamanho

    def is_empty(self):
        return self.tamanho == 0

    def add(self, item):
        if item in self.verifica_elemento:
            pass # vai ignorar se o elemento já estiver no dict
        else:
            self.verifica_elemento[item] = True
            # lista dinâmica, mas faço a verificação pra manter circularidade
            if self.tamanho == len(self.itens):  
                self.itens = self.itens + [item]
            else:
                self.itens[(self.inicio + self.tamanho) % len(self.itens)] = item
            self.tamanho += 1

    # O(n)
    def list(self):
        # gera uma lista ordenada com base na posição circular
        return [self.itens[(self.inicio + i) % len(self.itens)] for i in range(self.tamanho)]

    # O(n)
    def remove(self, item):
        if item not in self.verifica_elemento:
            raise ValueError("Element not found")

        # encontra a posição do item na fila circular
        posicao = self.inicio
        for i in range(self.tamanho):
            if self.itens[posicao] == item:
                break
            posicao = (posicao + 1) % len(self.itens)

        # remove o item da lista e reorganiza os elementos
        self.verifica_elemento.pop(item)
        for i in range(posicao, self.inicio + self.tamanho - 1):
            self.itens[i % len(self.itens)] = self.itens[(i + 1) % len(self.itens)]

        self.tamanho -= 1
        if self.tamanho == 0:
            self.inicio = 0  # reseta o início se a fila ficar vazia

    def contains(self, item):
        return item in self.verifica_elemento  # O(1)

    # só pra não ficar dando print(f1.list()) direto
    def __repr__(self):
        return f"{self.list()}"
