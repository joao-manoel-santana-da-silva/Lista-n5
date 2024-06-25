def remove_duplicatas(lista):
    elementos_unicos = set()  # Conjunto para armazenar elementos únicos
    lista_sem_duplicatas = []  # Lista auxiliar para construir a nova lista sem duplicatas

    for item in lista:
        if item not in elementos_unicos:
            elementos_unicos.add(item)  # Adiciona o elemento ao conjunto de elementos únicos
            lista_sem_duplicatas.append(item)  # Adiciona o elemento à lista sem duplicatas

    return lista_sem_duplicatas


# Exemplo de uso
lista_original = [1, 2, 3, 3, 4, 5, 2, 6, 7, 1]
lista_sem_duplicatas = remove_duplicatas(lista_original)
print(lista_sem_duplicatas)  # Saída esperada: [1, 2, 3, 4, 5, 6, 7]