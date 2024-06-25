import string


def contar_palavras(texto):
    # Remover pontuações e normalizar para minúsculas
    texto_processado = texto.translate(str.maketrans('', '', string.punctuation)).lower()

    # Dividir o texto em palavras
    palavras = texto_processado.split()

    # Criar um dicionário para armazenar a frequência das palavras
    frequencia = {}

    # Contar a frequência de cada palavra
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1

    return frequencia


# Exemplo de uso da função
texto = "Olá, mundo! Olá banana!"
resultado = contar_palavras(texto)
print(resultado)