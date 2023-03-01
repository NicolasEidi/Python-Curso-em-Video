"""     Exercício Python 59: 
    Crie um programa que leia dois valores e mostre um menu na tela:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    Seu programa deverá realizar a operação solicitada em cada caso.

    Resolução do exercício:
"""

from time import sleep

num1 = int(input("Digite o primeiro valor: "))
num2 =int(input("Digite o segundo valor: "))

total = 0
oper = 0

while oper != 5:
    oper = int(input("""
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
O que deseja fazer? """))
    print("===---" * 10)
    if oper == 1:
        total = num1 + num2
        print(f"A soma dos valores {num1} e {num2} é de {total}")

    elif oper == 2:
        total = num1 * num2
        print(f"A multiplicação dos valor {num1} e {num2} é de {total}")

    elif oper == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f"O maior número entre {num1} e {num2} é {maior}")
    
    elif oper == 4:
        mudanca = int(input("Você quer substituir o primeiro valor [1] ou o segundo valor [2]: "))
        if mudanca == 1:
            num1 = int(input("Digite um novo valor para o primeiro número: "))
            print(f"O primeiro valor agora vale: {num1}")
        else:
            num2 = int(input("Digite um novo valor para o segundo número: "))
            print(f"O segundo valor agora vale {num2}")
    elif oper == 5:
        print("Saindo...")
    print("===---" *10 )
    sleep(1)

print("Você saiu do programa")
