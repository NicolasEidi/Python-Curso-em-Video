"""     Exercício Python 5: 
    Faça um programa que leia um número Inteiro e 
    mostre na tela o seu sucessor e seu antecessor.

    Resolução do exercício:
"""

numero = int(input('Digite um número: '))
print('Sucessor de {} é {} e seu antecessor é {}'.format(numero, (numero+1), (numero-1)))
