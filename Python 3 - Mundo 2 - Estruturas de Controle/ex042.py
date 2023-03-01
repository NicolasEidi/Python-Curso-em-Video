"""     Exercício Python 42: 
    Refaça o DESAFIO 35 dos triângulos, 
    acrescentando o recurso de mostrar que tipo de triângulo será formado:
    – EQUILÁTERO: todos os lados iguais
    – ISÓSCELES: dois lados iguais, um diferente
    – ESCALENO: todos os lados diferentes

    Resolução do exercício:
"""

l1 = int(input('Lado 1: '))
l2 = int(input('Lado 2: '))
l3 = int(input('Lado 3: '))

if (l1 + l2) > l3 and (l2 + l3) > l1 and (l1 + l3) > l2:
    print('Esse triângulo é possível de ser formado')
    if l1 == l2 and l1 == l3:
        print('Equilátero, possui todos os lados iguais')
    elif l1 == l2 or l1 == l3 or l3 == l2:
        print('Isósceles, possui 2 lados iguais')
    else:
        print('Escaleno, não possui lados iguais')
else:
    print('Não é possível formar um triângulo')
