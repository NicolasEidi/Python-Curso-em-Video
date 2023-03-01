"""     Exercício Python 24: 
    Crie um programa que leia o nome de uma cidade 
    diga se ela começa ou não com o nome “SANTO”.

    Resolução do exercício:
"""

cidade = str(input('Cidade: ')).strip()

print(cidade[:5].lower() == 'santo')
