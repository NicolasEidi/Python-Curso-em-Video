"""     Exercício Python 68: 
    Faça um programa que jogue par ou ímpar com o computador. 
    O jogo só será interrompido quando o jogador perder, 
    mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

    Resolução do exercício:
"""

from random import randint

v = 0

while True:
    pc = randint(1, 10)
    jogador = int(input("Escolha um número: [1 a 10] "))
    while jogador not in range (0, 11):
        jogador = int(input("Escolha um número: [1 a 10] "))
    soma = pc + jogador
    tipo = ' '
    while tipo not in "PI":
        tipo = str(input("Escolha PAR ou ÍMPAR: [P/I] ")).strip().upper()[0]
    print("===---" * 10)
    print(f"Você escolheu {jogador} e o computador escolheu {pc}, a soma dos dois é {soma}")
    print(f"DEU PAR" if soma % 2 == 0 else "DEU ÍMPAR" )
    print("===---" * 10)
    if tipo == "P":
        if (soma % 2) == 0:
            print("Você VENCEU!")
            v += 1
        else:
            print("Você PERDEU...")
            break
    if tipo == "I":
        if (soma % 2) == 1:
            print("Você VENCEU!")
            v += 1
        else:
            print("Você PERDEU...")
            break

print("===---" * 10)
print(f"Você tem {v} vitória(s)")
