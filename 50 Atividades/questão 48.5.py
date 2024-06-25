# Definindo o alfabeto como uma string
alfabeto = 'abcdefghijklmnopqrstuvwxyz'

# Solicita ao usuário que digite uma frase para verificar se é um pangrama
frase = input('Digite uma frase para verificar se é um pangrama: ')

# Converte a frase para minúsculas para garantir que seja case insensitive
frase = frase.lower()

# Variável para verificar se todas as letras do alfabeto estão presentes na frase
todas_letras_presentes = True

# Itera sobre cada letra do alfabeto
for letra in alfabeto:
    # Verifica se a letra atual do alfabeto está presente na frase
    if letra not in frase:
        todas_letras_presentes = False
        break  # Se uma letra não estiver presente, podemos parar a verificação

# Verifica o resultado
if todas_letras_presentes:
    print("A frase é um pangrama!")
else:
    print("A frase não é um pangrama.")