"""     Exercício Python 35: 
    Desenvolva um programa que leia o comprimento de três retas 
    e diga ao usuário se elas podem ou não formar um triângulo.

    Resolução do exercício:
"""

l1 = int(input('Lado 1: '))
l2 = int(input('Lado 2: '))
l3 = int(input('Lado 3: '))

if (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1:
    print('É possível formar um triângulo')
else:
    print('Não é possivel formar um triângulo')
