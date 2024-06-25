def expandir_intervalos(string_intervalos):
    # Dividir a string em intervalos individuais
    intervalos = string_intervalos.split(',')
    numeros_expandidos = []

    for intervalo in intervalos:
        if '-' in intervalo:
            # Se for um intervalo como "1-3"
            inicio, fim = map(int, intervalo.split('-'))
            numeros_expandidos.extend(range(inicio, fim + 1))
        else:
            # Se for um número único como "5"
            numeros_expandidos.append(int(intervalo))

    return numeros_expandidos


# Exemplo de uso
string_exemplo = "1-3,5,7-9"
resultado = expandir_intervalos(string_exemplo)
print(resultado)  # Saída esperada: [1, 2, 3, 5, 7, 8, 9]