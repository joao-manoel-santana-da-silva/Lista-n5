#  Escreva uma função que converta um número romano para um número inteiro.

numero_romano = input("Digite o seu número em romano (em maiúsculas): ")


valores_romanos = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }


numero_inteiro = 0


for i in range(len(numero_romano)):
    if i > 0 and valores_romanos[numero_romano[i]] > valores_romanos[numero_romano[i - 1]]:

        numero_inteiro += valores_romanos[numero_romano[i]] - 2 * valores_romanos[numero_romano[i - 1]]
    else:

        numero_inteiro += valores_romanos[numero_romano[i]]

# Exibe o número inteiro correspondente ao número romano
print(f"O número inteiro correspondente ao número romano {numero_romano} é: {numero_inteiro}")