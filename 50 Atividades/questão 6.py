#Um anagrama é uma palavra que é feita a partir da transposição das letras de outra palavra ou frase.
#Por exemplo, "Iracema" é um anagrama para "America". Escreva um programa que decida se uma
#String é um anagrama de outra String, ignorando os espaços em branco. O programa deve considerar
#maiúsculas e minúsculas como sendo caracteres iguais, ou seja, "a" = "A".

def sao_anagramas(str1, str2):

    str1_sem_espacos = str1.replace('', '')
    str2_sem_espacos = str2.replace('', '')

    str1_minusculas = str1_sem_espacos.lower()
    str2_minusculas = str2_sem_espacos.lower()
    if len(str1_minusculas) != len(str2_minusculas):
      return False

    for char in str1_minusculas:
       if char not in str2_minusculas:
         return False

    return True


str1= 'Asriel'
str2= 'Ralsei'
if sao_anagramas(str1, str2):
    print(f'"{str1}" e "{str2}" são anagramas.')
else:
    print(f'"{str1}" e "{str2}" não são anagramas.')