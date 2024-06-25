# Escreva uma função que conte o número de vogais em uma string.

frase = input('qual sua frase?:')
vogais = ({'a','e','i','o','u'})

contador_de_vogais = 0
for i in frase:
    if i in vogais:
        contador_de_vogais +=1
    print(f'a sua frase {frase} tem {contador_de_vogais} vogais!')