"""     Exercício Python 37: 
    Escreva um programa em Python que leia um número 
    inteiro qualquer e peça para o usuário escolher 
    qual será a base de conversão: 1 para binário, 
    2 para octal e 3 para hexadecimal.

    Resolução do exercício:
"""

num = int(input('Número a ser convertido: '))
opc = int(input('Deseja converter para binário(1), octal(2), hex(3): '))

if opc == 1:
   print('o valor de {} em binário é {}'.format(num, bin(num)))

elif opc == 2:
    print('o valor de {} em octal é {}'.format(num, oct(num)))

elif opc == 3:
    print('o valor de {} em hexdecimal é {}'.format(num, hex(num)))

else:
    print('Escolha um valor entre 1 e 3 para as opções de conversão')
