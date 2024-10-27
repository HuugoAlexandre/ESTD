class Noh:
    def __init__(self, valor_inicial):
        self.dados = valor_inicial
        self.proximo = None
    
    def get_data(self):
        return self.dados
    
    def get_next(self):
        return self.proximo

    def set_data(self, novo_valor):
        self.dados = novo_valor

    def set_next(self, novo_proximo):
        self.proximo = novo_proximo

class Lista:
    def __init__(self):
        self.head = None
        self.tamanho = 0

    def is_empty(self):
        return self.head == None

    def insert(self, item, pos):
        if pos < 0 or pos > self.size():
            raise IndexError("Posição fora do intervalo.")
        temp = Noh(item)
        if pos == 0:
            temp.set_next(self.head)
            self.head = temp
        else:
            atual = self.head
            contador = 0
            while contador < pos - 1:
                atual = atual.get_next()
                contador+=1
            temp.set_next(atual.get_next())
            atual.set_next(temp)
        self.tamanho+=1

    # Adiciona no final da lista
    def append(self, item):
        novo_noh = Noh(item)
        if self.head is None:
            self.head = novo_noh
        else:
            atual = self.head
            while atual.get_next() is not None:
                atual = atual.get_next()
            atual.set_next(novo_noh)
        self.tamanho+=1

    # Adiciona no inicio da lista
    def add(self, item):
        temp = Noh(item)
        temp.set_next(self.head)
        self.head = temp
        self.tamanho+=1

    def add_ordenada(self, item):
        atual = self.head
        anterior = None
        parar = False

        while atual != None and not parar:
            if atual.get_data() > item:
                parar = True
            else:
                anterior = atual
                atual = atual.get_next()
        
        temp = Noh(item)
        if anterior == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(atual)
            anterior.set_next(temp)
        self.tamanho+=1

    def size(self):
        return self.tamanho     # Forma mais eficiente de retornar o tamanho (O(1))
        # Forma menos eficiente, O(n)
        # atual = self.head
        # contador = 0
        # while atual != None:
        #     contador+=1
        #     atual = atual.get_next()
        # return contador

    def search(self, item):
        atual = self.head
        encontrou = False
        while atual != None and not encontrou:
            if atual.get_data == item:
                encontrou = True
            else:
                atual = atual.get_next()
        return encontrou

    def search_ordenada(self, item):
        atual = self.head
        encontrou = False
        parar = False

        while atual != None and not encontrou and not parar:
            if atual.get_data() == item:
                encontrou = True
            else:
                if atual.get_data() > item:
                    parar = True
                else:
                    atual = atual.get_next()
    
    # Remove pela posição
    def pop(self, pos=None):
        if self.head is None:
            raise IndexError("Lista vazia para remoção.")

        tamanho = self.size()
        if pos == None:
            pos = tamanho - 1    
        if pos < 0 or pos >= tamanho:
            raise IndexError("Fora do intervalo para remoção.")
        
        atual = self.head
        anterior = None
        contador = 0
        while contador < pos:
            anterior = atual
            atual = atual.get_next()         
            contador+=1
        
        if anterior is None:
            self.head = atual.get_next()
        else:
            anterior.set_next(atual.get_next())
        self.tamanho-=1
        return atual.get_data()
    
    # Remove pelo item
    def remove(self, item):
        atual = self.head
        anterior = None
        encontrou = False
        while atual is not None and not encontrou:
            if atual.get_data() == item:
                encontrou = True
            else:
                anterior = atual
                atual = atual.get_next()
        
        if not encontrou:
            raise IndexError(f"O item {item} não está na lista.")

        if anterior == None:
            self.head = atual.get_next()
        else:
            anterior.set_next(atual.get_next())
        self.tamanho-=1

    def reverse(self):  
        anterior = None
        atual = self.head
        while atual is not None:
            proximo = atual.get_next()
            atual.set_next(anterior)
            anterior = atual
            atual = proximo
        self.head = anterior

    def clear(self):
        self.head = None
        self.tamanho = 0

    def concat(self, outra_lista):
        if outra_lista.is_empty():
            return
        if self.is_empty():
            self.head = outra_lista.head
        else:
            # Percorre até o final da lista atual
            atual = self.head
            while atual.get_next() is not None:
                atual = atual.get_next()
            atual.set_next(outra_lista.head) # Anexa a head da outra lista ao final da lista atual
        self.tamanho += outra_lista.size()
    
    def slice(self, start, end):
        if start < 0 or end > self.size() or start > end:
            raise IndexError("Índices fora do intervalo.")
        
        sublista = Lista()
        atual = self.head
        
        # Avança até o índice start
        for _ in range(start):
            if atual is not None:
                atual = atual.get_next()

        # Coleta os nós da lista até o índice end
        for _ in range(start, end):
            if atual is not None:
                sublista.append(atual.get_data())
                atual = atual.get_next()
            else:
                break  # Pra evitar erro se end for maior que o tamanho da lista

        return sublista

    def merge(self, outra_lista):
        merged_lista = Lista()
        atual1 = self.head
        atual2 = outra_lista.head

        # Percorre as duas listas e combina os elementos
        while atual1 is not None and atual2 is not None:
            if atual1.get_data() <= atual2.get_data():
                merged_lista.append(atual1.get_data())
                atual1 = atual1.get_next()
            else:
                merged_lista.append(atual2.get_data())
                atual2 = atual2.get_next()

        # Se ainda houver elementos em uma das listas, adiciona à lista mesclada
        while atual1 is not None:
            merged_lista.append(atual1.get_data())
            atual1 = atual1.get_next()

        while atual2 is not None:
            merged_lista.append(atual2.get_data())
            atual2 = atual2.get_next()

        return merged_lista

    # Retorna o número de vezes que um item aparece na lista
    def count(self, item):
        atual = self.head
        contador = 0
        
        while atual is not None:
            if atual.get_data() == item:
                contador += 1
            atual = atual.get_next()
        
        return contador

    #Rotaciona a lista encadeada para a esquerda em k posições
    def rotate(self, k):
        if self.is_empty() or k == 0:
            return
    
        tamanho = self.tamanho
        
        # Ajustar k
        k = k % tamanho
        if k == 0:
            return
        
        # Encontrar o novo head e o nó anterior
        atual = self.head
        contador = 1  # 1 porque começa contando a partir do head
        
        while contador < k and atual.get_next() is not None:
            atual = atual.get_next()
            contador += 1
        
        # novo_head será o próximo nó após o k-ésimo nó
        novo_head = atual.get_next()
        
        # Se novo_head é None, k é igual ao tamanho, então não precisamos rotacionar
        if novo_head is None:
            return
        
        # Encontrar o último nó da lista
        ultimo = novo_head
        while ultimo.get_next() is not None:
            ultimo = ultimo.get_next()
        
        # Desvincular e reconectar
        atual.set_next(None)  # Desvincula o k-ésimo nó
        ultimo.set_next(self.head)  # Conecta o último nó ao head
        self.head = novo_head  # Atualiza o head para o novo_head
    
    def sort(self):
        if self.head is None:
            return

        current = self.head
        while current is not None:
            min_node = current
            next_node = current.get_next()

            # Encontrar o menor valor na parte não ordenada da lista
            while next_node is not None:
                if next_node.get_data() < min_node.get_data():
                    min_node = next_node
                next_node = next_node.get_next()
            
            # Trocar os dados entre o nó atual e o nó mínimo encontrado
            if min_node != current:
                current_data = current.get_data()
                min_node_data = min_node.get_data()
                current.set_data(min_node_data)
                min_node.set_data(current_data)

            current = current.get_next()

    # Pra visualizar melhor
    def __repr__(self):
        elementos = []
        atual = self.head
        while atual is not None:
            elementos.append(str(atual.get_data()))
            atual = atual.get_next()
        return " -> ".join(elementos)

# Não ordenada     
teste = Lista()
teste.add(3)
teste.add(1)
teste.add(2)
teste.add(4)
teste.insert(5, 2)
print(teste)
teste.append(8)
teste.append(7)
teste.append(6)
print(teste)
print("Tamanho: ", teste.size())
print("Vazio? " ,teste.is_empty())
teste.remove(2)
print(teste)
print("Elemento removido: ", teste.pop(2))
print(teste)
print("Tamanho: ", teste.size())
teste.reverse()
print(teste)

# print("#########################")
# # Ordenada
# teste2 = Lista()
# teste2.add_ordenada(3)
# teste2.add_ordenada(1)
# teste2.add_ordenada(2)
# teste2.add_ordenada(4)
# print(teste2)
# print("Tamanho: ", teste2.size())
# print("Vazio? " ,teste2.is_empty())
# teste2.remove(2)
# print(teste2)
# print("Tamanho: ", teste2.size())