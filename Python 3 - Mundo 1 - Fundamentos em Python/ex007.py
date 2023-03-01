"""     Exercício Python 7: 
    Desenvolva um programa que leia as duas notas de um aluno, 
    calcule e mostre a sua média.

    Resolução do exercício:
"""

print('{:=^20}'.format('Boletim'))
Aluno = input('Nome do aluno: ')
m1 = float(input('Nota 1: '))
m2 = float(input('Nota 2: '))
media = (m1 + m2) / 2
print('{:=^20}' .format(Aluno))
print('Nota da matéria 1: {} \nNota da matéria 2: {} \nMédia das duas matérias: {:.1f}'.format(m1, m2, media))
