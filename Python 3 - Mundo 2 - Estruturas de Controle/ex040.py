"""     Exercício Python 40: 
    Crie um programa que leia duas notas de um 
    aluno e calcule sua média, mostrando uma mensagem 
    no final, de acordo com a média atingida:
    – Média abaixo de 5.0: REPROVADO
    – Média entre 5.0 e 6.9: RECUPERAÇÃO
    – Média 7.0 ou superior: APROVADO

    Resolução do exercício:
"""

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

media = (nota1 + nota2) / 2

if 7 > media >= 5:
    print('Recuperação!')

elif media < 5:
    print('Reprovado!')

elif media >= 7:
    print('Aprovado!')
