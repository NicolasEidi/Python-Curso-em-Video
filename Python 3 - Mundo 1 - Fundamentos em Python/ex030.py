"""     Exercício Python 30: 
    Crie um programa que leia um número inteiro e
    mostre na tela se ele é PAR ou ÍMPAR.

    Resolução do exercício:
"""

print('Veficação se numero é par ou ímpar\n')

num = int(input('Digite um valor: '))
impar = num % 2
if impar != 0:
    print('{} É um número ímpar'.format(num))
else:
    print('{} É um número par'.format(num))
