"""     Exercício Python 51: 
    Desenvolva um programa que leia o primeiro 
    termo e a razão de uma PA. No final, 
    mostre os 10 primeiros termos dessa progressão.

    Resolução do exercício:
"""

num = int(input('Numero do primeiro termo: '))
razao = int(input('Valor da progressão aritmética: '))
decimo = num + (10 - 1) * razao

for c in range(num, decimo + razao, razao):
    print(c, end = ', ')

print('ACABOU!')
