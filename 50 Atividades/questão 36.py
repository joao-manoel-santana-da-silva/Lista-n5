# Escreva uma função que conte o número de palavras em uma string.


frase = input('qual sua frase?:')

numero_de_palavras= len(frase.split())
print(f'A sua frase, {frase}, contem esses numeros: {numero_de_palavras}.')