"""     Exercício Python 88:
    Faça um programa que ajude um jogador da MEGA SENA 
    a criar palpites.O programa vai perguntar quantos 
    jogos serão gerados e vai sortear 6 números entre 1 e 60 
    para cada jogo, cadastrando tudo em uma lista composta.

    Resolução do exercício:
"""

from random import randint
qjogos = int(input("Quer gerar quantos jogos? "))
list_jog = []
jogo = []
for i in range(0, qjogos): 
    for n in range(0, 6):
        num = (randint(1, 60))
        while num in jogo:
            num = (randint(1, 60))
        jogo.append(num)
    jogo.sort()
    list_jog.append(jogo[:])
    jogo.clear()
    
for c in range(0, qjogos):
    print(f"Jogo {c+1}: {list_jog[c]}")
