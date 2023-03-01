"""     Exercício Python 60: 
    Faça um programa que leia um número qualquer e mostre o seu fatorial. 
    Exemplo:
    5! = 5 x 4 x 3 x 2 x 1 = 120

    Resolução do exercício:
"""

num = int(input("Qual número você quer fatorar: "))

c = num
f = 1

print(f"Calculando {num}! = ", end = "")

while c > 0:
    print(f"{c}", end = "")
    print(" x " if c > 1 else " = ", end = "")
    f *= c
    c -= 1

print(f)
