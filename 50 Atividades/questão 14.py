# Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente
# 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço
# separador.
# Exemplo:
# Telefone: 461-0133
# Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
# Telefone corrigido sem formatação: 34610133
# Telefone corrigido com formatação: 3461-0133

telefone= input('telefone:')
if len(telefone)== 7:
    telefone_corrigido= '3'+telefone
    print('seu telefone tem somente 7 digitos. Vou acrescentar o digito três na frente.')
    print(f'telefone corrigido sem formatação:{telefone_corrigido}')