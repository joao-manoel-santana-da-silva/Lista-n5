# O professor deseja dividir uma turma com N alunos em dois grupos: um com M alunos e outro com
# (N-M) alunos. Faça o programa que lê o valor de N e M e informa o número de combinações possíveis.
# a. Número de combinações é igual a 𝑁!/(𝑀! ∗ (𝑁 − 𝑀)!)

import math
N = int(input('M é o tanto de alunos na sala é de:'))

M = int(input('N é o tanto de alunos na sala é:'))

soma = math.pi/ N/(M*(N-M))
print(soma)