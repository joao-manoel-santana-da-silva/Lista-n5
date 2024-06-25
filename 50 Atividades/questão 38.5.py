import math


def distancia_euclidiana(ponto1, ponto2):
    soma_quadrados = 0.0
    # Itera sobre as coordenadas de ambos os pontos
    for i in range(len(ponto1)):
        diferenca = ponto1[i] - ponto2[i]
        soma_quadrados += diferenca ** 2

    distancia = math.sqrt(soma_quadrados)
    return distancia


# Exemplo de uso
ponto1 = (1, 2, 3)
ponto2 = (4, 5, 6)
distancia = distancia_euclidiana(ponto1, ponto2)
print(f"A distância euclidiana entre {ponto1} e {ponto2} é {distancia}.")