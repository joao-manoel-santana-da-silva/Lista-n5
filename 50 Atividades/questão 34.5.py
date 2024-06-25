def bubble_sort(lista):
    n = len(lista)

    # Loop para percorrer todos os elementos da lista
    for i in range(n):
        # Últimos i elementos já estão na posição correta
        for j in range(0, n - i - 1):
            # Troca se o elemento encontrado for maior que o próximo elemento
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


# Exemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90]

print("Lista original:", numeros)
bubble_sort(numeros)
print("Lista ordenada:", numeros)