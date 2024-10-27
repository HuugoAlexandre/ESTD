class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # O próximo do novo nó aponta para ele mesmo
        else:
            current = self.head
            while current.next != self.head:  # Percorre até o último nó
                current = current.next
            current.next = new_node  # O próximo do último nó aponta para o novo nó
            new_node.next = self.head  # O novo nó aponta para o head

    def remove(self, value):
        if self.head is None:
            return "A lista está vazia."
        
        current = self.head
        previous = None

        while True:
            if current.data == value:  # Verifica se o nó atual contém o valor
                if previous is None:  # O nó a ser removido é o head
                    # Se a lista tiver apenas um nó
                    if current.next == self.head:
                        self.head = None
                    else:
                        # Percorre até o último nó para ajustar o ponteiro
                        while current.next != self.head:
                            current = current.next
                        current.next = self.head.next  # O último nó aponta para o próximo do head
                        self.head = self.head.next  # O head é atualizado para o próximo
                else:
                    previous.next = current.next  # O nó anterior aponta para o próximo do nó atual
                return f"Nó com valor {value} removido."
            
            previous = current
            current = current.next

            if current == self.head:  # Se retornamos ao head, o valor não foi encontrado
                break
        
        return f"Nó com valor {value} não encontrado."

    def display(self):
        if self.head is None:
            return "A lista está vazia."
        
        elements = []
        current = self.head
        while True:
            elements.append(current.data)
            current = current.next
            if current == self.head:
                break

        return " -> ".join(map(str, elements))

# Exemplo de uso
circular_list = CircularLinkedList()
circular_list.append(1)
circular_list.append(2)
circular_list.append(3)

print("Lista Circular:", circular_list.display())

print(circular_list.remove(2))  # Remove o nó com valor 2
print("Lista Circular após remoção:", circular_list.display())

print(circular_list.remove(5))  # Tentando remover um valor não existente

circular_list.append(4)
print("Lista Circular após adicionar 4:", circular_list.display())
