#Faça um programa que decida se duas strings lidas do teclado são palíndromas mútuas, ou seja, se uma
#é igual à outra quando lida de traz para frente.

#Exemplo: amor e roma.

a= input('escreva a sua primeira frase')
b= input('escreva sua segunda frase')
c= b [::-1]
print(c)

if c==a:
  print('as duas palavras são palindromas')
else:
  print('as duas palavras não são palindromas')