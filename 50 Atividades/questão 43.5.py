def encontrar_intersecao(lista1, lista2):
    # Converte as listas em conjuntos
    set1 = set(lista1)
    set2 = set(lista2)

    # Encontra a interseção usando o operador de interseção (&)
    intersecao = list(set1 & set2)

    return intersecao


# Exemplo de uso
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

resultado = encontrar_intersecao(lista1, lista2)
print(f"Interseção das listas {lista1} e {lista2}: {resultado}")  # Saída esperada: [4, 5]