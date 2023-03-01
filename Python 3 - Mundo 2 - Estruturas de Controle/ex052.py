"""     Exercício Python 52: 
    Faça um programa que leia um número inteiro e 
    diga se ele é ou não um número primo.

    Resolução do exercício:
"""

num = int(input('Número: '))
total = 0

for c in range(1, num + 1):
    if num % c == 0:
        total += 1

if total == 2:
    print(f'{num} é um número PRIMO')
else:
    print(f'{num} Não é um número PRIMO')

    