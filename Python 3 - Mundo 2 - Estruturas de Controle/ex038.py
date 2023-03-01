"""     Exercício Python 38: 
    Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
    – O primeiro valor é maior
    – O segundo valor é maior
    – Não existe valor maior, os dois são iguais.

    Resolução do exercício:
"""

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))

if num1 > num2:
    print('O primeiro valor é maior')

elif num1 < num2:
    print('O segundo valor é maior')

else:
    print('Não existe valor maior, os dois são iguais.')
