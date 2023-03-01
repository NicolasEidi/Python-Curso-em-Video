"""     Exercício Python 32: 
    Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

    Resolução do exercício:
"""

from datetime import date

ano = int(input('Ano para verificar se é bissexto: Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
    print(f'{ano} É um ano bissexto') 
else:
    print(f'{ano} Não é um ano bissexto')
