"""     Exercício Python 27: 
    Faça um programa que leia o nome completo de uma pessoa, 
    mostrando em seguida o primeiro e o último nome separadamente.

    Resolução do exercício:
"""

nome = str(input('Digite seu nome completo: ')).lower().strip().split()

print('Primeiro nome: {}'.format(nome[0].capitalize()))
print('Último nome: {}'.format(nome[-1].capitalize()))
