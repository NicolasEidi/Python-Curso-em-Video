"""     Exercício Python 100:

    Faça um programa que tenha uma lista chamada números 
    e duas funções chamadas sorteia() e somaPar(). 
    A primeira função vai sortear 5 números e vai colocá-los 
    dentro da lista e a segunda função vai mostrar a soma 
    entre todos os valores pares sorteados pela função anterior.

    Resolução do exercício:
"""
from random import randint

numeros = []

def sorteia(quantidade):
    for i in range(0, quantidade):  
        numeros.append(randint(0, 10))


def somaPar(numeros):
    par = 0
    for i in numeros:
        if i % 2 == 0:
            par = par + i

    print(f"A soma dos numeros pares é {par}")

sorteia(4)
print(f"Lista com os valores sorteados {numeros}")
somaPar(numeros)
