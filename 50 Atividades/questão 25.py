# ) Faça uma função para verificar se um ano é bissexto ou não. Utilize a seguinte regra:
# Um ano bissexto é divisível por 4, mas não por 100, ou então se é divisível por 400.
# Exemplo: 1988 é bissexto pois é divisível por 4 e não é por 100; 2000 é bissexto porque é divisível
# por 400.
# A função deve retornar True caso o ano seja bissexto, e False caso contrário.

ano_bissexto = int (input('Digite a sua data:'))
if (ano_bissexto % 4==0 and ano_bissexto % 100!=0) or (ano_bissexto % 400==0):
    print('Seu ano é bissexto!')
else:
    print('Seu ano não é bissexto')