# Escreva um algoritmo que verifique se um e-mail é válido quanto a sua forma. Exemplo:
# jean@zahn.com é um e-mail válido, mas jean@zahn e jeanzahn.com não são e-mails válidos

email= input('qual deu email?:')
if email.count('@')== 1 and email.count('.')>= 1:
    print(email, 'seu email foi autorizado' )
else:
    print('seu email não foi autorizado')