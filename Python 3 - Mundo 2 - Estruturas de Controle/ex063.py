"""     Exercício Python 63: 
    Escreva um programa que leia um número N inteiro qualquer e 
    mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
    Exemplo:
    0 – 1 – 1 – 2 – 3 – 5 – 8

    Resolução do exercício:
"""

n = int(input("Número de termos da Sequência de Fibonacc: "))

t1 = 0 
t2 = 1
cont = 3

print("===---" * 10)
print("Sequência de Fibonacci")
print("===---" * 10)

print(f"{t1} -> {t2}", end = "")

while cont <= n:
    t3 = t1 + t2
    print(f" -> {t3}", end = "")
    cont += 1
    t1 = t2
    t2 = t3
