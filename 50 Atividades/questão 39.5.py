def mergesort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2  # Encontra o meio da lista
        lista_esquerda = lista[:meio]  # Divide a lista em duas partes
        lista_direita = lista[meio:]

        # Chama recursivamente mergesort para as sublistas
        mergesort(lista_esquerda)
        mergesort(lista_direita)

        # Inicializa índices para percorrer as duas sublistas e a lista final
        i = j = k = 0

        # Combina as sublistas ordenadamente
        while i < len(lista_esquerda) and j < len(lista_direita):
            if lista_esquerda[i] < lista_direita[j]:
                lista[k] = lista_esquerda[i]
                i += 1
            else:
                lista[k] = lista_direita[j]
                j += 1
            k += 1

        # Verifica se ainda há elementos restantes nas sublistas
        while i < len(lista_esquerda):
            lista[k] = lista_esquerda[i]
            i += 1
            k += 1

        while j < len(lista_direita):
            lista[k] = lista_direita[j]
            j += 1
            k += 1


# Exemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", numeros)

mergesort(numeros)
print("Lista ordenada:", numeros)