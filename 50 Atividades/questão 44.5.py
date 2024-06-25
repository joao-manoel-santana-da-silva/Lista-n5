def calcular_potencia(base, expoente):
    if expoente == 0:
        return 1  # Qualquer número elevado a 0 é 1

    resultado = 1
    multiplicador = base if expoente > 0 else 1 / base
    expoente = abs(expoente)  # Transforma o expoente negativo em positivo

    for _ in range(expoente):
        resultado *= multiplicador

    return resultado


# Exemplos de uso
base = 2
expoente_positivo = 3
expoente_negativo = -2

print(f"{base} elevado a {expoente_positivo} é igual a {calcular_potencia(base, expoente_positivo)}")
print(f"{base} elevado a {expoente_negativo} é igual a {calcular_potencia(base, expoente_negativo)}")