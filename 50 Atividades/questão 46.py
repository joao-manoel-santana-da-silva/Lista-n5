# Escreva uma função que combine duas strings intercalando seus caracteres. Se uma string for mais
# longa que a outra, anexe o restante ao final.

def encontrar_intersecao(lista1, lista2):
    intersecao = []

    for i in lista1:
        if i in lista2 and i not in intersecao:
            intersecao.append(i)
    return intersecao

lista1 = [1,2,3,4,5]
lista2 = [4,5,6,7,8]
resultado = encontrar_intersecao(lista1, lista2)
print(f'Interseção das listas {lista1} e {lista2}: {resultado}")')