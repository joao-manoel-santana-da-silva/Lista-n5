# teste que eu pedi para o chat gpt para me ajudar a enteder como verificar um numero primo

numero = int(input("Digite um número inteiro positivo maior que 1: "))

if numero <= 1:
    print("Número inválido. Digite um número inteiro positivo maior que 1.")
else:
    eh_primo = True  # Assume que o número é primo inicialmente

    # Verifica divisibilidade por todos os números de 2 até número - 1
    for i in range(2, numero):
        if numero % i == 0:
            eh_primo = False  # Se for divisível por algum número, não é primo
            break  # Não é necessário verificar mais

    if eh_primo:
        print(f"{numero} é primo")
    else:
        print(f"{numero} não é primo")