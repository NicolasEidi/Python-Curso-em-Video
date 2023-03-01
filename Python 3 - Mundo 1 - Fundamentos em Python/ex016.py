"""     Exercício Python 16: 
    Crie um programa que leia um número Real qualquer 
    pelo teclado e mostre na tela a sua porção Inteira.

    Resolução do exercício:
"""

from math import trunc

num = float(input('Digite um número: '))
print('O número quebrado é {} e ele inteiro seria {}'.format(num, trunc(num)))
