def eh_quadrado_magico(matriz):
    # Verifica se a matriz é quadrada
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    if num_linhas != num_colunas:
        return False

    # Calcula a soma de referência (primeira linha)
    soma_referencia = sum(matriz[0])

    # Verifica as somas das linhas
    for linha in matriz:
        if sum(linha) != soma_referencia:
            return False

    # Verifica as somas das colunas
    for coluna in range(num_colunas):
        soma_coluna = sum(matriz[linha][coluna] for linha in range(num_linhas))
        if soma_coluna != soma_referencia:
            return False

    # Verifica a diagonal principal
    diagonal_principal = sum(matriz[i][i] for i in range(num_linhas))
    if diagonal_principal != soma_referencia:
        return False

    # Verifica a diagonal secundária
    diagonal_secundaria = sum(matriz[i][num_colunas - 1 - i] for i in range(num_linhas))
    if diagonal_secundaria != soma_referencia:
        return False

    # Se todas as verificações passaram, é um quadrado mágico
    return True


# Exemplo de uso
matriz_exemplo = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if eh_quadrado_magico(matriz_exemplo):
    print("A matriz é um quadrado mágico!")
else:
    print("A matriz não é um quadrado mágico.")