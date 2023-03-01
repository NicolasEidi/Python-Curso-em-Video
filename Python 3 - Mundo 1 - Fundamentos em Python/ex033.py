"""     Exercício Python 33: 
    Faça um programa que leia três números e 
    mostre qual é o maior e qual é o menor.

    Resolução do exercício:
"""

print('O maior e o menor\n')

num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))

if num1 > num2 and num1 > num3:
    print(f'{num1} é maior número')
elif num2 > num1 and num2 > num3:
    print(f'{num2} é maior número')
else:
    print(f'{num3} é o maior número')

if num1 < num2 and num1 < num3:
    print(f'{num1} é o menor número')
elif num2 < num1 and num2 < num3:
    print(f'{num2} é o menor número')
else:
    print(f'{num3} é o menor número') 
