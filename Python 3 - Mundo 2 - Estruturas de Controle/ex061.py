"""     Exercício Python 61: 
    Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
    mostrando os 10 primeiros termos da progressão usando a estrutura while.

    Resolução do exercício:
"""

num = int(input("Número inicial da progressão aritmética: "))
razão = int(input("Razão da progressão: "))

termo = num
cont = 1

while cont <= 10:
    print(f"{termo} -> ", end = "")
    termo += razão
    cont += 1
