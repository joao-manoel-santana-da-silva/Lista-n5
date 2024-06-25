# Escreva uma função que verifique se os parênteses em uma string estão equilibrados (considerando
# também colchetes e chaves).

texto= input('qual palavra você quer?:')
com_parenteses= False

for i in texto:
    if i == '(' or i == ')':
        com_parenteses= True


if com_parenteses:
    print('Seu codigo tem parentes')
else:
    print('Seu codigo não tem parrenteses')