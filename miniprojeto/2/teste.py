from main import *

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