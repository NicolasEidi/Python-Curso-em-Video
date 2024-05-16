"""     Exercício Python 90:
    Faça um programa que leia nome e média de um aluno, 
    guardando também a situação em um dicionário. No final, 
    mostre o conteúdo da estrutura na tela.

    Resolução do exercício:
"""

aluno = {}
aluno['Nome'] = str(input("Nome do aluno: ")).capitalize().strip()
aluno['Média'] = float(input(f"Média do {aluno['Nome']}: "))

if aluno['Média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

for k, i in aluno.items():
    print(f"{k} é igual a {i}")
