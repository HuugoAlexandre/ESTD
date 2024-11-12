class HashTable:
    def __init__(self):
        self._tamanho = 11
        self._slots = [None] * self._tamanho
        self._valores = [None] * self._tamanho
        self._quantidade_itens = 0

    def hashfunction(self, chave, tamanho):
        return chave % tamanho

    def rehash(self, oldhash, tamanho):
        return (oldhash + 1) % tamanho

    def put(self, chave, valor):
        valor_hash = self.hashfunction(chave, len(self._slots))
        if self._slots[valor_hash] is None:
            self._slots[valor_hash] = chave
            self._valores[valor_hash] = valor
            self._quantidade_itens += 1
        else:
            if self._slots[valor_hash] == chave:
                self._valores[valor_hash] = valor
            else:
                proximo_slot = self.rehash(valor_hash, len(self._slots))
                while self._slots[proximo_slot] is not None and \
                        self._slots[proximo_slot] != chave:
                    proximo_slot = self.rehash(proximo_slot, len(self._slots))
                if self._slots[proximo_slot] is None:
                    self._slots[proximo_slot] = chave
                    self._valores[proximo_slot] = valor
                    self._quantidade_itens += 1
                else:
                    self._valores[proximo_slot] = valor

    def get(self, chave):
        slot_inicial = self.hashfunction(chave, len(self._slots))
        valor = None
        parar = False
        encontrou = False
        posicao = slot_inicial
        while self._slots[posicao] is not None and not encontrou and not parar:
            if self._slots[posicao] == chave:
                encontrou = True
                valor = self._valores[posicao]
            else:
                posicao = self.rehash(posicao, len(self._slots))
                if posicao == slot_inicial:
                    parar = True
        return valor

    def __getitem__(self, chave):
        return self.get(chave)

    def __len__(self):
        return self._quantidade_itens

    def __contains__(self, chave):
        slot_inicial = self.hashfunction(chave, len(self._slots))
        pos = slot_inicial
        while self._slots[pos] is not None:
            if self._slots[pos] == chave:
                return True
            pos = self.rehash(pos, len(self._slots))
            if pos == slot_inicial:
                break
        return False

    def __setitem__(self, chave, valor):
        self.put(chave, valor)