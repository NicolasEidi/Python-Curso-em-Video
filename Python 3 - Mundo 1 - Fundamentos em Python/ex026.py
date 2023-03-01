"""     Exercício Python 26: 
    Faça um programa que leia uma frase pelo teclado e 
    mostre quantas vezes aparece a letra “A”, 
    em que posição ela aparece a primeira vez e 
    em que posição ela aparece a última vez.

    Resolução do exercício:
"""


frase =  str(input('Frase: ')).lower().strip()

print('Quantas vezes aparece a letra (a): {}'.format(frase.count('a')))
print('Primeira aparição da letra (a): {}'.format(frase.find('a')+1))
print('A última aparição da letra (a): {}'.format(frase.rfind('a')+1))
