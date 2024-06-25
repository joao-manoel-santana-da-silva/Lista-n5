# Escreva uma função que substitua palavras censuradas em um texto por asteriscos (*), mantendo o
# comprimento das palavras censuradas. Pergunte ao usuário quais são as palavras censuradas.

def substituir_censura(frase, palavras_censuradas):
    for palavra in palavras_censuradas:
        frase = frase.replace(palavra, '*' * len(palavra))
    return frase

# Exemplo de uso da função
frase = input('Qual é a sua frase? ')
palavras_censuradas = input('Quais são as palavras censuradas? (separadas por vírgula): ').split(',')

frase_censurada = substituir_censura(frase, palavras_censuradas)
print(frase_censurada)