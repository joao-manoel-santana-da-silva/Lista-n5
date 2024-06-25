# Escreva uma função que remova elementos duplicados de uma lista enquanto mantém a ordem original
# dos elementos.

def remover_dupicatas(lista):
    elementos_unicos = set()
    lista_sem_duplicatas = []
    for i in lista:
        if i not in elementos_unicos:
            elementos_unicos.add(i)
            lista_sem_duplicatas.append(i)

    return lista_sem_duplicatas


lista1 = [1,2,3,3,4,5,2,6,7,1]
lista_sem_duplicatas = remover_dupicatas(lista1)
print(lista_sem_duplicatas)