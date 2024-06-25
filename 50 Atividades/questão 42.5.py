# Strings para verificar a subsequência
string_principal = "abcdefg"
subsequencia = "aceg"

# Inicialização de índices para percorrer as strings
indice_subsequencia = 0

# Percorre a string principal
for char in string_principal:
    # Verifica se o caractere atual da string principal é igual ao caractere da subsequência
    if indice_subsequencia < len(subsequencia) and char == subsequencia[indice_subsequencia]:
        indice_subsequencia += 1  # Move para o próximo caractere da subsequência

# Se o índice da subsequência é igual ao seu comprimento, então é uma subsequência
if indice_subsequencia == len(subsequencia):
    print(f"A string '{subsequencia}' é uma subsequência de '{string_principal}'")
else:
    print(f"A string '{subsequencia}' não é uma subsequência de '{string_principal}'")