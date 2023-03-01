"""     Exercício Python 39: 
    Faça um programa que leia o ano de nascimento de 
    um jovem e informe, de acordo com a sua idade, 
    se ele ainda vai se alistar ao serviço militar, 
    se é a hora exata de se alistar ou se já passou do 
    tempo do alistamento. Seu programa também deverá mostrar 
    o tempo que falta ou que passou do prazo.

    Resolução do exercício:
"""

from datetime import date

ano = int(input('Ano de nascimento: '))
ano_atual = date.today().year
dif = ano_atual - ano

if dif == 18:
    print('Está na hora de se alistar')
elif dif < 18:
    print('Falta {} anos para você se alistar'.format(18 - dif))
elif dif > 18:
    print('Você deveria ter se alistado à {} anos atrás'.format(dif - 18))
