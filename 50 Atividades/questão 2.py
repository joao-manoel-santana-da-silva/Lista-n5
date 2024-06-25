#Faça um programa que lê uma String que representa uma cadeia de DNA e gera a cadeia complementar.

a = 'ATTACGGC'
b = ''
for i in range(len(a)):
    if a[i] == 'A':
        b += 'T'
    elif a[i] == 'T':
        b += 'A'
    elif a[i] == 'C':
        b += 'G'
    elif a[i] == 'G':
        b += 'C'
print(b)