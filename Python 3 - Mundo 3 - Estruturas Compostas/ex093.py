"""     Exercício Python 93:
    Crie um programa que gerencie o aproveitamento de um jogador
    de futebol. O programa vai ler o nome do jogador e quantas 
    partidas ele jogou. Depois vai ler a quantidade de gols 
    feitos em cada partida. No final, tudo isso será guardado 
    em um dicionário, incluindo o total de gols feitos durante 
    o campeonato.

    Resolução do exercício:
"""

jogador = {}
partidas = []
jogador['Nome'] = str(input("Nome do jogador: ")).capitalize()
jogador['Partidas'] = int(input("Quantidade de partidas: "))
for c in range(0, jogador['Partidas']):
    gol = int(input(f"Quantidade de gols na {c+1}º partida: "))
    partidas.append(gol)    
jogador['Gols'] = partidas[:]
jogador['Total de Gols'] = sum(partidas)
print("===---" * 10)
for k, v in jogador.items():
    print(f"{k} tem valor: {v}")
print("===---" * 10)
print(f"O jogador {jogador['Nome']} tem o total de {jogador['Partidas']} partidas")

for c in range(0, jogador['Partidas']):
    print(f"    Na {c+1}º partida fez um total de {jogador['Gols'][c]} gols")
print(f"Foi um total de {jogador['Total de Gols']} gols")
