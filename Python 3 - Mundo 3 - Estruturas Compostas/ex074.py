"""     Exercício Python 74:
    Crie um programa que vai gerar cinco números aleatórios 
    e colocar em uma tupla. Depois disso, 
    mostre a listagem de números gerados e também indique 
    o menor e o maior valor que estão na tupla.

    Resolução do exercício:
"""

from random import randint
while True:
    numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
    print("Os valores sorteados são: ", end="")
    for n in numeros:
        print(f"{n} ", end="")
    print(f"\nO maior valor é {max(numeros)}")
    print(f"O menor valor é {min(numeros)}")
    continuar = str(input("Deseja ver outro número: [S/N]: ")).strip().upper()[0]
    while continuar not in "SN":
        continuar = str(input("Deseja ver outro número: [S/N]: ")).strip().upper()[0]
    if continuar == "N":
        break
    else:
        numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
