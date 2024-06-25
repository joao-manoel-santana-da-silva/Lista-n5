# Crie uma função que expanda abreviações em um texto baseado em um dicionário de abreviações.
# Crie uma Matriz de abreviações, contendo a abreviação e a palavra completa (sem abreviações).
# Quando o texto for inserido, apresente o texto sem as abreviações originais.

def expandir_abreviacoes(texto, dicionario_abreviacoes):
    palavras = texto.split()
    texto_expandido = []

    for palavra in palavras:
        if palavra in dicionario_abreviacoes:
            texto_expandido.append(dicionario_abreviacoes[palavra])
        else:
            texto_expandido.append(palavra)

    return ' '.join(texto_expandido)

# Exemplo de uso da função
def main():
    # Dicionário de abreviações
    dicionario_abreviacoes = {
        'vc': 'você',
        'tb': 'também',
        'q': 'que',
        'p': 'para',
        'td': 'tudo',
        'blz': 'beleza'
    }

    # Texto de exemplo com abreviações
    texto = "Oi, td bem? Qd vamos nos encontrar? Blz, te vejo lá!"

    # Expandir as abreviações no texto
    texto_expandido = expandir_abreviacoes(texto, dicionario_abreviacoes)

    # Imprimir o texto expandido
    print("Texto Original:")
    print(texto)
    print("\nTexto Expandido:")
    print(texto_expandido)

if __name__ == "__main__":
    main()