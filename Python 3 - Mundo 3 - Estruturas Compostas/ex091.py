"""     Exercício Python 91:
    Crie um programa onde 4 jogadores joguem um dado e 
    tenham resultados aleatórios. Guarde esses resultados 
    em um dicionário em Python. No final, coloque esse dicionário
    em ordem, sabendo que o vencedor tirou o maior número no dado.

    Resolução do exercício:
"""

from random import randint
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
print("==--" * 13)
print(f"{' ' * 16}{'Valores Sorteados':^10}{' ' * 16}")
print("==--" * 13)
for k, v in jogadores.items():
    print(f"O {k} sorteou {v} no dado")

print(f"{'---=== '*3}{'RANKING':^10}{' ===---'*3}")
ranking = []
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f"Em {i+1}º lugar ficou {v[0]} em sorteando {v[1]}")
print("==--" * 13)
