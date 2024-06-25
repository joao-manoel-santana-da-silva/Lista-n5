# ) Escreva uma função que verifique se uma string é uma subsequência de outra string.

string = 'abcdefg'
subsequencia = 'aceg'

indice_subsequencia = 0

for i in string:
    if indice_subsequencia<len(subsequencia) and i ==subsequencia[indice_subsequencia]:
        indice_subsequencia +=1

if indice_subsequencia == len(subsequencia):
    print(f'A string {subsequencia} é uma subsequência de {string}')
else:
    print(f'A string {subsequencia} não é uma subsequência de {string}')