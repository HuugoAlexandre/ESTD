from main import *

# Cria uma árvore binária com raiz 3
arvore = BinaryTree(3)
print("Árvore inicial:", arvore)

# Insere filhos na árvore
arvore.insertLeft(4)
arvore.insertRight(5)
print("Árvore após inserções:", arvore)

# Adiciona mais um nível de filhos
arvore.getLeftChild().insertLeft(6)
arvore.getLeftChild().insertRight(7)
print("Árvore após inserções adicionais:", arvore)

# Obtém e modifica valores
print("Valor da raiz:", arvore.getRootVal())
arvore.setRootVal(10)
print("Nova raiz:", arvore.getRootVal())
print("Filho esquerdo:", arvore.getLeftChild())
print("Filho direito:", arvore.getRightChild())
