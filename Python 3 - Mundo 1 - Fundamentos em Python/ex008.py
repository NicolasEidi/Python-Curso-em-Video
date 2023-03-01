"""     Exercício Python 8: 
    Escreva um programa que leia um valor em metros e 
    o exiba convertido em centímetros e milímetros.

    Resolução do exercício:
"""

metros = float(input('Digite um valor em metros: '))
cm = metros * 100
mm = cm * 10
print('Metros:',metros, '\nCentímetros', cm , '\nMilímitros', mm)
