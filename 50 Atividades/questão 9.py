# Faça um programa que leia o nome do usuário e o imprima na vertical, em forma de escada invertida,
# usando apenas letras maiúsculas.
# Exemplo:
# Nome =Vanessa
# Resultado gerado pelo programa:
# VANESSA
# VANESS
# VANES
# VANE
# VAN
# VA
# V

nome = input('Qual o seu nome? ')

for i in range(len(nome), 0, -1):
    pedaço_do_nome= nome[:i]
    print(pedaço_do_nome)