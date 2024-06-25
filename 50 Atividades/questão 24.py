# ) Faça uma função que informe o status do aluno a partir da sua média de acordo com a tabela a seguir:
# Nota acima de 6 → “Aprovado”
# Nota entre 4 e 6 → “Verificação Suplementar”
# Nota abaixo de 4 → “Reprovado”

nota = int(input('qual a nota do aluno?:' '(1 até 10)'))

if nota >= 6:
    print('o aluno está aprovado!')

elif nota >=5:
    print('O aluno está de recuperação!')

else:
    print('O aluno não passou!')