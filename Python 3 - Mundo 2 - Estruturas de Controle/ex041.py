"""     Exercício Python 41: 
    A Confederação Nacional de Natação precisa 
    de um programa que leia o ano de nascimento de 
    um atleta e mostre sua categoria, de acordo com a idade:
    – Até 9 anos: MIRIM
    – Até 14 anos: INFANTIL
    – Até 19 anos: JÚNIOR
    – Até 25 anos: SÊNIOR
    – Acima de 25 anos: MASTER

    Resolução do exercício:
"""

from datetime import date

nasc = int(input('Ano em que nasceu: '))
atual = date.today().year

data = atual - nasc
print(f'O atleta tem {data} anos')
if data <= 9:
    print('Mirim')
elif data <= 14:
    print('Infantil')
elif data <= 19:
    print('Júnior')
elif data <= 25:
    print('Sênior')
else:
    print('Master')
