#Faça um programa que lê uma frase e retorna o número de palavras que a frase contém. Considere que
#a palavra pode começar e/ou terminar por espaços.

a= input("Digite a sua frase :")
c = 0
for i in a.split():
    c+=1
print(c)