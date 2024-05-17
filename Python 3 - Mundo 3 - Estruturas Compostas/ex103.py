"""     Exercício Python 103:

    Faça um programa que tenha uma função chamada ficha(), 
    que receba dois parâmetros opcionais: o nome de um jogador 
    e quantos gols ele marcou. 
    O programa deverá ser capaz de mostrar a ficha do jogador, 
    mesmo que algum dado não tenha sido informado corretamente.

    Resolução do exercício:
"""

def ficha(jogador='<Desconhecido>', gol=0):
    print(f"O jogador {jogador} fez {gol} gols no campeonato")

nome = str(input("Nome do jogador: "))
gols = str(input("Numero de gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)