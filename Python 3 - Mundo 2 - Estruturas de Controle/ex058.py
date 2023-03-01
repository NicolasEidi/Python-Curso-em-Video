"""     Exercício Python 58: 
    Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em 
    um número entre 0 e 10. Só que agora o jogador vai tentar 
    adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

    Resolução do exercício:
"""

from random import randint

print("\nAdvinhe o valor do computador entre 0 e 10\n")

pc = randint (0, 10)
acertou = False
chutes = 0 

while not acertou:
    num = int(input("Digite um valor: "))
    chutes += 1
    if num == pc:
        acertou = True
    else:
        if num > pc:
            print("Menos...")
        else:
            print("Mais...")

print(f"Você acertou o valor com o total de {chutes} chutes")
