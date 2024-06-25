# Leitura das duas strings do usuário
string1 = input("String 1: ")
string2 = input("String 2: ")

# Informação sobre o conteúdo e comprimento das strings
print(f'Tamanho de "{string1}": {len(string1)} caracteres')
print(f'Tamanho de "{string2}": {len(string2)} caracteres')

# Verifica se as strings têm o mesmo comprimento
if len(string1) == len(string2):
    print("As duas strings são de tamanhos iguais.")
else:
    print("As duas strings são de tamanhos diferentes.")

# Verifica se as strings têm o mesmo conteúdo
if string1 == string2:
    print("As duas strings possuem o mesmo conteúdo.")
else:
    print("As duas strings possuem conteúdo diferente.")