def eh_primo(num):
    if num <= 1:
        return False  # Números menores ou iguais a 1 não são primos

    # Verifica divisibilidade por todos os números de 2 até a raiz quadrada do número
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False  # Se for divisível por algum número, não é primo

    return True  # Se não for divisível por nenhum número, é primo


def lista_primos(n):
    primos = []
    num = 2  # Começa verificando a partir do número 2

    while len(primos) < n:
        if eh_primo(num):
            primos.append(num)
        num += 1

    return primos


# Exemplo de uso
n = 10
primeiros_primos = lista_primos(n)
print(f"Os primeiros {n} números primos são: {primeiros_primos}")