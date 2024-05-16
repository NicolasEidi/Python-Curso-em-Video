"""     Exercício Python 89:
    Crie um programa que leia nome e duas notas de vários alunos
    e guarde tudo em uma lista composta. No final, mostre 
    um boletim contendo a média de cada um e permita que o 
    usuário possa mostrar as notas de cada aluno individualmente.

    Resolução do exercício:
"""

alunos = []
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("1º Nota: ")) 
    nota2 = float(input("2º Nota: "))
    média = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], média])
    continuar = str(input("Deseja adicionar mais algum aluno: [S/N]:  ")).strip().upper()[0]
    while continuar not in "SN":
        continuar = str(input("Deseja adicionar mais algum aluno: [S/N]:  ")).strip().upper()[0]
    if continuar == "N":
        break
print("===---" * 10)
print(f'{"Nº":<4}{"Nome":<12}{"Média":>10}')
print("===---" * 10)
for i, a in enumerate(alunos):
    print(f"{i:<4}{a[0]:<12}{a[2]:>10.1f}")
while True:
    print("===---" * 10)
    escolha = int(input("Deseja ver a nota de qual aluno? (Digite 999 para finalizar): "))
    if escolha == 999:
        break
    if escolha <= len(alunos) -1:
        print(f"As notas do {alunos[escolha][0]} é {alunos[escolha][1]}")
print("FIM")
