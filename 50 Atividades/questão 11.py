# Faça um programa que leia 2 Strings e informe o conteúdo delas seguido do seu comprimento. Informe
# também se as duas Strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
# Exemplo:
# String 1: Brasil Hexa 2026
# String 2: Brasil! Hexa 2026!
# Tamanho de "Brasil Hexa 2026": 16 caracteres
# Tamanho de "Brasil! Hexa 2026!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.

opniao1= ('string1: ')
opniao2= ('string2: ')

print(f'tamanho de "{string1}": {len(string1)} cacteres')
print(f'Tamanho de "{string2}": {len(string2)} caracteres')

if len(string1)== len(string2):
    print('as duas strings tem tamanhos iguais')
else:
    print("As duas strings são de tamanhos diferentes.")

if string1 == string2:
        print("As duas strings possuem o mesmo conteúdo.")
    else:
        print("As duas strings possuem conteúdo diferente.")