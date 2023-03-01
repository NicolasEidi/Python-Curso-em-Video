"""     Exercício Python 11: 
    Faça um programa que leia a largura e a altura de uma parede em metros, 
    calcule a sua área e a quantidade de tinta necessária para pintá-la, 
    sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

    Resolução do exercício:
"""

h = int(input('Altura em metros: '))
l = int(input('Largura em metros: '))
A = h * l
tinta = A / 2
print('A área é: {}m2 \nPara pintar essa parede vai precisar de {} litros de tinta'.format(A, tinta))
