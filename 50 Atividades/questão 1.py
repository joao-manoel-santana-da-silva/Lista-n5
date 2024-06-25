# Escreva um programa que lê uma frase e uma String antiga e uma String nova. O programa deve imprimir uma String contendo a frase original, mas com a última ocorrência da String antiga substituída pela String nova.

frase= "dois pratos de trigo para dois tigres"
a= "dois"
b= "tres"

a=a[::-1]
b=b[::-1]

frase=frase[::-1]

frase=frase.replace(a,b,1)
print(frase[::-1])