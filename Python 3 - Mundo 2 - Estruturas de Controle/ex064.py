"""     Exercício Python 64: 
    Crie um programa que leia vários números inteiros pelo teclado. 
    O programa só vai parar quando o usuário digitar o valor 999, 
    que é a condição de parada. No final, mostre quantos números foram 
    digitados e qual foi a soma entre eles (desconsiderando o flag).

    Resolução do exercício:
"""

num = int(input("Digite um valor: "))
cont = soma = num = 0

while num != 999:
    soma += num
    cont += 1
    num = int(input("Digite um valor: "))

print(f"Você digitou {cont} números e a soma deles é {soma}")
