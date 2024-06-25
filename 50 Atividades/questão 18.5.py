# ) Implemente um algoritmo de compressão de string que utilize a contagem de caracteres repetidos (por
# exemplo, "aaabbc" se torna "a3b2c1").

def compressao_string(frase):
    if len(frase) == 0:
        return ""

    comprimido = ""
    caractere_atual = frase[0]
    contador = 1

    for i in range(1, len(frase)):
        if frase[i] == caractere_atual:
            contador += 1
        else:
            comprimido += caractere_atual + str(contador)
            caractere_atual = frase[i]
            contador = 1

    # Adicionar o último caractere e sua contagem ao resultado
    comprimido += caractere_atual + str(contador)

    # Verifica se a string comprimida é menor ou igual à original
    if len(comprimido) < len(frase):
        return comprimido
    else:
        return frase


# Exemplo de uso da função
frase = input('Qual é a sua frase? ')
frase_comprimida = compressao_string(frase)
print("Frase comprimida:", frase_comprimida)