class PilhaVazia(Exception):
    pass

class PilhaArray:
    def __init__(self):
        self._pilha = []

    def __len__(self):
        return len(self._pilha)

    def size(self):
        return self.__len__()

    def is_empty(self):
        return len(self._pilha) == 0

    def push(self, e):
        self._pilha.append(e)

    def top(self):
        if self.is_empty():
            raise PilhaVazia('A pilha está vazia')
        return self._pilha[-1]

    def pop(self):
        if self.is_empty():
            raise PilhaVazia('A pilha está vazia')
        return self._pilha.pop()
    
    def inverte_texto(texto):
        pilha = PilhaArray()
        for letra in texto:
            pilha.push(letra)
        palavra = ""
        while not pilha.is_empty():
            palavra += pilha.pop()
        return palavra
    
    def inverte_arquivo(nome_arquivo):
        p = PilhaArray()
        arquivo = open(nome_arquivo) #abre o arquivo

        for linha in arquivo: #lê cada linha do arquivo
            p.push(linha.rstrip('\n')) # insere a linha na pilha
        arquivo.close() # fecha o arqui

        output = open(nome_arquivo, 'w') # reabre o arquivo e sobrescreve
        while not p.is_empty():
            output.write(p.pop() + '\n') # re-insert newline characters
        output.close()

    def is_matched(expr):
        abre = '({[' # delimitadores - abertura
        fecha = ')}]' # delimitadoers - fechamento
        pilha = PilhaArray()
        for d in expr:
            if d in abre:
                pilha.push(d) # push o delimitador de abertura
            elif d in fecha:
                if pilha.is_empty():
                    return False # não bate
                if fecha.index(d) != abre.index(pilha.pop()):
                    return False # não bate
        return pilha.is_empty() # tem mais delimitadores na pilha?