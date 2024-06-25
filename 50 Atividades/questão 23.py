# Faça um programa que contém uma função que recebe um número inteiro que corresponde a um mês
# do ano e retorna o nome desse mês. Por exemplo, se o mês informado como parâmetro for 1 a função
#deverá retornar "janeiro", se o mês enviado como parâmetro for 2 a função deverá retornar "fevereiro"
#e assim por diante.

numero= int(input('qual número você quer?: (de 1 até 12)'))

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto',
  'setembro', 'outubro', 'novembro', 'dezembro']

if 1 <= numero <= 12:
    nome_mes = meses[numero-1]

    if 1 <= numero <= 12:
        nome_mes = meses[numero - 1]
        print(f'O mês correspondente ao número {numero} é {nome_mes}.')
    else:
        print('Número de mês inválido. Por favor, digite um número entre 1 e 12.')