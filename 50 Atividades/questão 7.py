#Faça um programa que leia o nome do usuário e mostre o nome de traz para frente, utilizando somente
#letras maiúsculas.
#Exemplo:
#Nome = Swainstainger
#Resultado gerado pelo programa:
#REGNIATSNIAWS

frase=input('diga seu nome:')

frase= frase.upper()
print(frase[::-1])