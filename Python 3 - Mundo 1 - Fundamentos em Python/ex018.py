"""     Exercício Python 18: 
    Faça um programa que leia um ângulo qualquer 
    e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

    Resolução do exercício:
"""

import math

ang = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(ang))
co = math.cos(math.radians(ang))
ta = math.tan(math.radians(ang))
print('O ângulo de {} tem o SENO de: {:.2f} \nO ângulo de {} tem o COSSENO de: {:.2f} \nO ângulo de {} tem a TANGENTE de: {:.2f}'.format(ang, seno, ang, co, ang, ta))
