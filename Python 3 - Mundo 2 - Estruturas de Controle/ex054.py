"""     Exercício Python 54:
    Crie um programa que leia o ano de nascimento de 
    sete pessoas. No final, mostre quantas pessoas ainda 
    não atingiram a maioridade e quantas já são maiores.

    Resolução do exercício:
"""

from datetime import date

ano = date.today().year
cont = 0
cont2 = 0

for i in range(1, 8):
    nascimento = int(input(f'{i}º data de nascimento: '))
    if (ano - nascimento) < 21:
        cont += 1
    else:
        cont2 += 1
    
print(f'{cont} é o número de pessoas que são menores de idade\nE {cont2} são maiores de idade')
