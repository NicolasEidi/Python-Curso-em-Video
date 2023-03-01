"""     Exercício Python 29: 
    Escreva um programa que leia a velocidade de um carro. 
    Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que 
    ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

    Resolução do exercício:
"""

vel = int(input('Velocidade do carro: '))

if vel > 80:
    multa = (vel - 80) * 7
    print('Você ultrapassou 80km/h a uma velocidade de {}km/h, sua multa será de R${:.2f}'.format(vel, multa))
else:
    print('Você está na velocidade de {}km/h, não levará multa'.format(vel))
