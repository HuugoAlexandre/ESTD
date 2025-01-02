class BinaryTree:
    def __init__(self, rootObj):
        """Inicializa a árvore com um nó raiz."""
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        """
        Insere um novo nó como filho esquerdo.
        Se já houver um filho esquerdo, o nó atual será deslocado
        para ser o filho esquerdo do novo nó.
        """
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        """
        Insere um novo nó como filho direito.
        Se já houver um filho direito, o nó atual será deslocado
        para ser o filho direito do novo nó.
        """
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        """Retorna o filho direito da árvore."""
        return self.rightChild

    def getLeftChild(self):
        """Retorna o filho esquerdo da árvore."""
        return self.leftChild

    def setRootVal(self, obj):
        """Define um novo valor para o nó raiz."""
        self.key = obj

    def getRootVal(self):
        """Retorna o valor do nó raiz."""
        return self.key

    def __repr__(self):
        """Retorna uma representação visual da árvore."""
        l = self.leftChild if self.leftChild else "None"
        r = self.rightChild if self.rightChild else "None"
        return f"[{self.key}, {l}, {r}]"
