"""     Exercício Python 19: 
    Um professor quer sortear um dos seus quatro alunos 
    para apagar o quadro. Faça um programa que ajude ele, 
    lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

    Resolução do exercício:
"""

from random import choice

a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
lista = [a1, a2, a3, a4]
print('O aluno escolhido foi: {}'.format(choice(lista)))
