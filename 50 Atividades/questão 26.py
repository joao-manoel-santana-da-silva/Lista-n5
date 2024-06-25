# Faça um programa que, dado uma figura geométrica que pode ser uma circunferência, triângulo ou
# retângulo, calcule a área e o perímetro da figura
# O programa deve primeiro perguntar qual o tipo da figura:
# (1) circunferência
# (2) triângulo
# (3) retângulo

import math

# Dependendo do tipo de figura, ler o (1) tamanho do raio da circunferência; (2) tamanho de cada um
# dos lados do triângulo; (3) tamanho dos dois lados retângulos.

print ('Qual figura você deseja:')
print('(1) circunferência')
print('(2) triângulo')
print('(3) retângulo')

figura = int(input("Digite o número correspondente à figura desejada: "))

if figura == 1:
    # Cálculo para Circunferência
    raio = float(input("Digite o raio da circunferência: "))

    # Cálculos
    area = math.pi * raio ** 2
    perimetro = 2 * math.pi * raio

    # Exibição dos resultados
    print(f"Área da circunferência: {area:.2f}")
    print(f"Perímetro da circunferência: {perimetro:.2f}")

elif figura == 2:
    # Cálculo para Triângulo
    lado1 = float(input("Digite o tamanho do primeiro lado do triângulo: "))
    lado2 = float(input("Digite o tamanho do segundo lado do triângulo: "))
    lado3 = float(input("Digite o tamanho do terceiro lado do triângulo: "))

    # Cálculos do perímetro e semi-perímetro
    perimetro = lado1 + lado2 + lado3
    semi_perimetro = perimetro / 2
    # Cálculo da área usando a fórmula de Heron
    area = math.sqrt(semi_perimetro * (semi_perimetro - lado1) * (semi_perimetro - lado2) * (semi_perimetro - lado3))

    # Exibição dos resultados
    print(f"Área do triângulo: {area:.2f}")
    print(f"Perímetro do triângulo: {perimetro:.2f}")

elif figura == 3:
    # Cálculo para Retângulo
    lado1 = float(input("Digite o tamanho do primeiro lado do retângulo: "))
    lado2 = float(input("Digite o tamanho do segundo lado do retângulo: "))

    # Cálculos
    area = lado1 * lado2
    perimetro = 2 * (lado1 + lado2)

    # Exibição dos resultados
    print(f"Área do retângulo: {area:.2f}")
    print(f"Perímetro do retângulo: {perimetro:.2f}")

else:
    print("Opção inválida. Por favor, escolha uma das opções disponíveis (1, 2 ou 3).")