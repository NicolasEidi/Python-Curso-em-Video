"""     Exercício Python 50: 
    Desenvolva um programa que leia seis números inteiros e 
    mostre a soma apenas daqueles que forem pares. 
    Se o valor digitado for ímpar, desconsidere-o.

    Resolução do exercício:
"""

soma = 0
cont  = 0

for c in range(1, 7):
    a = int(input(f'Digite {c}º valor: '))
    if a % 2 == 0:
        soma += a
        cont += 1
print(f'Você informou {cont} números pares e a soma é {soma}')
