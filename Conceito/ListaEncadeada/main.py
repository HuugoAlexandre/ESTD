class Noh:
    def __init__(self, valor_inicial):
        self.dados = valor_inicial
        self.proximo = None
    
    def getData(self):
        return self.dados
    
    def getNext(self):
        return self.proximo

    def setData(self, novo_valor):
        self.dados = novo_valor

    def setNext(self, novo_proximo):
        self.proximo = novo_proximo

class Lista:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Noh(item)
        temp.setNext(self.head)
        self.head = temp

    def add_ordenada(self, item):
        atual = self.head
        anterior = None
        parar = False

        while atual != None and not parar:
            if atual.getData() > item:
                parar = True
            else:
                anterior = atual
                atual = atual.getNext()
        
        temp = Noh(item)
        if anterior == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(atual)
            anterior.setNext(temp)

    def size(self):
        atual = self.head
        contador = 0
        while atual != None:
            contador+=1
            atual = atual.getNext()
        return contador

    def search(self, item):
        atual = self.head
        encontrou = False
        while atual != None and not encontrou:
            if atual.getData == item:
                encontrou = True
            else:
                atual = atual.getNext()
        return encontrou

    def search_ordenada(self, item):
        atual = self.head
        encontrou = False
        parar = False

        while atual != None and not encontrou and not parar:
            if atual.getData() == item:
                encontrou = True
            else:
                if atual.getData() > item:
                    parar = True
                else:
                    atual = atual.getNext()

    def remove(self, item):
        atual = self.head
        anterior = None
        encontrou = False
        while not encontrou:
            if atual.getData() == item:
                encontrou = True
            else:
                anterior = atual
                atual = atual.getNext()
        if anterior == None:
            self.head = atual.getNext()
        else:
            anterior.setNext(atual.getNext())

    # Pra visualizar melhor
    def __repr__(self):
        elementos = []
        atual = self.head
        while atual is not None:
            elementos.append(str(atual.getData()))
            atual = atual.getNext()
        return " -> ".join(elementos)

# Não ordenada     
teste = Lista()
teste.add(3)
teste.add(1)
teste.add(2)
teste.add(4)
print(teste)
print("Tamanho: ", teste.size())
print("Vazio? " ,teste.is_empty())
teste.remove(2)
print(teste)
print("Tamanho: ", teste.size())

print("#########################")
# Ordenada
teste2 = Lista()
teste2.add_ordenada(3)
teste2.add_ordenada(1)
teste2.add_ordenada(2)
teste2.add_ordenada(4)
print(teste2)
print("Tamanho: ", teste2.size())
print("Vazio? " ,teste2.is_empty())
teste2.remove(2)
print(teste2)
print("Tamanho: ", teste2.size())