# ) Faça um programa que leia uma data de nascimento no formato dd/mm/aaaa e imprima a data com
# o mês escrito por extenso.
# Exemplo:
# Data = 20/02/1995
# Resultado gerado pelo programa:
# Você nasceu em 20 de fevereiro de 1995

from datetime import datetime

# Função para obter o nome do mês por extenso

def obter_nome_mes(numero_mes):

   meses = [

       'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',

       'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'

   ]

   return meses[numero_mes - 1]

# Função principal

def imprimir_data_com_mes_extenso():

   data_str = input("Digite a data de nascimento (dd/mm/aaaa): ")

   try:

       data = datetime.strptime(data_str, "%d/%m/%Y")

       dia = data.day

       mes = data.month

       ano = data.year

       nome_mes = obter_nome_mes(mes)

       print(f"Você nasceu em {dia} de {nome_mes} de {ano}")

   except ValueError:

       print("Data inválida. Certifique-se de digitar no formato dd/mm/aaaa.")

# Chamar a função principal

imprimir_data_com_mes_extenso()