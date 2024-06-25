# Faça um programa que leia o nome do usuário e o imprima na vertical, em forma de escada, usando
# apenas letras maiúsculas.
# Exemplo:
# Nome =Vanessa
# Resultado gerado pelo programa:
# V
# VA
# VAN
# VANE
# VANES
# VANESS
# VANESSA

nome = input('Qual o seu nome? ')

for i in range(1, len(nome)+1):
    pedaço_do_nome=  nome[:i]
    print(pedaço_do_nome)