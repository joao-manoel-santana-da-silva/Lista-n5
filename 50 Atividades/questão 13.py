# Dado uma String com uma frase informada pelo usuário (incluindo espaços em branco), conte:
# a. quantos espaços em branco existem na frase.
# b. quantas vezes aparecem as vogais a, e, i, o, u.

frase= input('diga sua frase:')
numero_de_espacos= frase.count(' ')
print(f'sua frase contem {numero_de_espacos} espaços')

numero_de_vogais= sum (frase.count(vogal) for vogal in 'aeiouAEIOU')
print(f'sua frase contem {numero_de_espacos} vogais')