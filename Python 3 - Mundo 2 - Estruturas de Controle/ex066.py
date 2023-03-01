"""     Exercício Python 66: 
    Crie um programa que leia números inteiros pelo teclado. 
    O programa só vai parar quando o usuário digitar o valor 999, 
    que é a condição de parada. No final, mostre quantos números 
    foram digitados e qual foi a soma entre elas (desconsiderando o flag).

    Resolução do exercício:
"""

soma = cont = 0

while True:
    num = int(input("Digite um valor: "))
    if num == 999:
        break
    soma += num
    cont += 1

print(f"Você digitou {cont} números, a soma desses números é {soma}")
