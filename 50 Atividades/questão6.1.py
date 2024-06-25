def sao_anagramas(str1, str2):
    # Remover espaços em branco
    str1_sem_espacos = str1.replace(" ", "")
    str2_sem_espacos = str2.replace(" ", "")

    # Converter para minúsculas
    str1_minusculas = str1_sem_espacos.lower()
    str2_minusculas = str2_sem_espacos.lower()

    # Verificar se têm o mesmo tamanho após a remoção de espaços e conversão para minúsculas
    if len(str1_minusculas) != len(str2_minusculas):
        return False

    # Verificar se contêm os mesmos caracteres (ignorando a ordem)
    for char in str1_minusculas:
        if char not in str2_minusculas:
            return False

    return True


# Exemplo de uso:
str1 = "Iracema"
str2 = "America"

if sao_anagramas(str1, str2):
    print(f'"{str1}" e "{str2}" são anagramas.')
else:
    print(f'"{str1}" e "{str2}" não são anagramas.')