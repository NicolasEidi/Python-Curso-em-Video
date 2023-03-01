"""     Exercício Python 17: 
    Faça um programa que leia o comprimento do cateto oposto 
    e do cateto adjacente de um triângulo retângulo. 
    Calcule e mostre o comprimento da hipotenusa.

    Resolução do exercício:
"""

from math import hypot 

co = float(input('Digite um valor para cateto oposto: '))
ca = float(input('Digite um valor para o cateto adjacente: '))
hip = hypot(co, ca) #a²+b²=c²
print('O valor de hipotenusa será: {:.2f}'.format(hip))
