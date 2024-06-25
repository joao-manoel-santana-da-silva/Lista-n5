def binario_para_decimal(binario):
    decimal = 0
    # Inverte a string binária para facilitar a conversão
    binario = binario[::-1]

    # Itera sobre cada dígito binário e calcula o valor decimal correspondente
    for i in range(len(binario)):
        if binario[i] == '1':
            decimal += 2 ** i  # Multiplica por 2 elevado à posição do dígito '1'

    return decimal


# Exemplo de uso
numero_binario = input("Digite um número binário: ")
decimal = binario_para_decimal(numero_binario)
print(f"O número binário {numero_binario} é equivalente a {decimal} em decimal.")