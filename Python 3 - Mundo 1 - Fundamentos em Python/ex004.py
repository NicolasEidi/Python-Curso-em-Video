"""     Exercício Python 4:
    Faça um programa que leia algo pelo teclado 
    e mostre na tela o seu tipo primitivo e todas
    as informações possíveis sobre ele.

    Resolução do exercício:
"""

a = input('Digite algo: ')

print('O tipo primitivo desse valor é {}'.format(type(a)))
print('Só tem espaços: ', a.isspace())
print('É númerico: ', a.isnumeric())
print('É alfabético:', a.isalpha())
print('É maiúsculo: ', a.isupper())
print('É minúsculo: ', a.islower())
print('É alfanumérico: ', a.isalnum())
print('É título: ', a.istitle())
print('É ascii', a.isascii())
