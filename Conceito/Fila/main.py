class FilaVazia(Exception):  # Herda de Exception para funcionar como exceção
    pass

class FilaArray:
    CAPACIDADE_PADRAO = 5  # Capacidade padrão inicial da fila
    
    def __init__(self):
        self._dados = [None] * FilaArray.CAPACIDADE_PADRAO  # Inicializa o array com None
        self._tamanho = 0
        self._inicio = 0

    def __len__(self):
        return self._tamanho

    def is_empty(self):
        return self._tamanho == 0

    def peek(self):  # Corrigido o nome do método
        if self.is_empty():
            raise FilaVazia('A fila está vazia')
        return self._dados[self._inicio]

    def dequeue(self):
        if self.is_empty():
            raise FilaVazia('A fila está vazia')
        result = self._dados[self._inicio]
        self._dados[self._inicio] = None  # Remove referência ao dado
        self._inicio = (self._inicio + 1) % len(self._dados)
        self._tamanho -= 1
        return result

    def enqueue(self, e):
        if self._tamanho == len(self._dados):  # Verifica se precisa expandir a capacidade
            self._aumenta_tamanho(2 * len(self._dados))
        disponivel = (self._inicio + self._tamanho) % len(self._dados)
        self._dados[disponivel] = e
        self._tamanho += 1

    def _aumenta_tamanho(self, novo_tamanho):
        dados_antigos = self._dados
        self._dados = [None] * novo_tamanho  # Nova lista com maior capacidade
        posicao = self._inicio
        for k in range(self._tamanho):  # Reorganiza os elementos existentes
            self._dados[k] = dados_antigos[posicao]
            posicao = (1 + posicao) % len(dados_antigos)
        self._inicio = 0  # Reseta o índice de início
