"""     Exercício Python 95:
    Aprimore o desafio 93 para que ele funcione com vários 
    jogadores, incluindo um sistema de visualização de 
    detalhes do aproveitamento de cada jogador.

    Resolução do exercício:
"""

time = []
jogador = {}
partidas = []
while True: 
    jogador.clear()
    jogador['Nome'] = str(input("Nome do jogador: ")).capitalize()
    quant_partida = int(input("Quantidade de partidas: "))
    partidas.clear()
    for c in range(0, quant_partida):
        partidas.append(int(input(f"Quantidade de gols na {c+1}º partida: ")))        
    jogador['Gols'] = partidas[:]
    jogador['Total de Gols'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        continuar = str(input("Deseja adicionar mais um jogador: [S/N] ")).strip().upper()[0]
        if continuar in "SN":
            break   
        print("Digite apenas S ou N")  
    if continuar == "N":
        break
print("===---" * 10)
print("Nº    ", end="")
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()
print("===---" * 10)
for k, v  in enumerate(time):
    print(f"{k:<5} ", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
while True:
    procurar_j = int(input("Dados de qual jogador você deseja ver? [999 para sair]: "))
    if procurar_j == 999:
        break
    if procurar_j >= len(time):
        print("Você digitou um valor que não pertence a nenhum jogador")
    else:
        print(f"       --Levantamento do jogador {time[procurar_j]['Nome']}--       ")
        for i, v in enumerate(time[procurar_j]['Gols']):
            print(f"No {i+1}º jogo fez {v} gols")
    print("===---" * 10)
print("Fim do programa")
