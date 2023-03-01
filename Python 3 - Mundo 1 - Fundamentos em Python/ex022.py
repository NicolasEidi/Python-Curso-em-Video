"""     Exercício Python 22: 
    Crie um programa que leia o nome completo de uma pessoa e mostre:
    – O nome com todas as letras maiúsculas e minúsculas.
    – Quantas letras ao todo (sem considerar espaços).
    – Quantas letras tem o primeiro nome.

    Resolução do exercício:
"""

nome = str(input('Nome: ')).strip()

print('Nome em maiúsculo: {}'.format(nome.upper()))
print('Nome em minúsculo: {}'.format(nome.lower()))
print('Total de letras do nome: {}'.format(len(nome) - nome.count(' ')))
print('Seu nome tem {} letras'.format(nome.find(' ')))
