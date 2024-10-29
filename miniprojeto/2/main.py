class Membro:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.proximo = None

class ListaEncadeadaCircular:
    def __init__(self):
        self.head = None
        self.tail = None
        self.atual = None  # Ponteiro para o próximo responsável

    def adicionar_membro(self, nome, email):
        novo_membro = Membro(nome, email)
        if self.head is None:
            # Primeira inserção precisa apontar pra si mesmo
            self.head = novo_membro
            self.tail = novo_membro
            novo_membro.proximo = novo_membro
            self.atual = novo_membro  # Atualiza o ponteiro atual para o primeiro membro
        else:
            # Adiciona o membro no final da lista
            self.tail.proximo = novo_membro
            novo_membro.proximo = self.head
            self.tail = novo_membro
           
            # Atualiza o ponteiro atual para o novo membro
            self.atual = novo_membro  

    def remover_membro(self, nome):
        if self.head is None:
            return

        atual = self.head
        anterior = self.tail
        while True:
            if atual.nome == nome:
                if atual == self.head:  # Remoção do primeiro elemento
                    self.head = atual.proximo
                    self.tail.proximo = self.head
                elif atual == self.tail:  # Remoção do último elemento
                    self.tail = anterior
                    self.tail.proximo = self.head
                else:  # Remoção de um elemento intermediário
                    anterior.proximo = atual.proximo

                # Ajuste do ponteiro 'atual' se necessário
                if self.atual == atual:
                    self.atual = atual.proximo
                print(f"Membro {nome} removido.")
                return
            anterior = atual
            atual = atual.proximo
            if atual == self.head:
                break
        print(f"Membro {nome} não encontrado na lista.")

    def proximo_responsavel(self):
        if self.atual is None:
            print("A lista está vazia.")
            return
        print(f"Próximo responsável: {self.atual.nome}")
        # Avança o ponteiro 'atual' para o próximo membro
        self.atual = self.atual.proximo  

    # Pra ficar mais fácil de ver
    def mostrar_lista(self):
        if self.head is None:
            print("A lista está vazia.")
            return
        atual = self.head
        elementos = []
        while True:
            elementos.append(atual.nome)
            atual = atual.proximo
            if atual == self.head:
                break
        print(" -> ".join(elementos) + " -> (volta para " + self.head.nome + ")")

grupo = ListaEncadeadaCircular()

# Adiciona membros e exibe resultados intermediários
grupo.adicionar_membro("Abel", "abel444@gmail.com")
grupo.mostrar_lista()
grupo.proximo_responsavel()
print("=============")

grupo.adicionar_membro("Bia", "biazinha@gmail.com")
grupo.mostrar_lista()
grupo.proximo_responsavel()
print("=============")

grupo.adicionar_membro("Carlos", "carlinhos@gmail.com")
grupo.mostrar_lista()
grupo.proximo_responsavel()
print("=============")

grupo.adicionar_membro("Davi", "davii@gmail.com")
grupo.mostrar_lista()
grupo.proximo_responsavel()
print("=============")

# Tenta remover um membro inexistente
grupo.remover_membro("Bruno")
grupo.mostrar_lista()
grupo.proximo_responsavel()
print("=============")
