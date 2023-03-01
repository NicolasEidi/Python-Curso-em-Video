"""     Exercício Python 31: 
    Desenvolva um programa que pergunte a distância de uma viagem em Km. 
    Calcule o preço da passagem, cobrando R$0,50 por Km para viagens 
    de até 200Km e R$0,45 parta viagens mais longas.

    Resolução do exercício:
"""

distancia = int(input('Distância de uma viagem: '))

if distancia <= 200:
    custo = distancia * 0.50
    print('O custo da viagem será de R${:.2f}'.format(custo))
else:
    custo = distancia * 0.45
    print('O custo da viagem será de R${:.2f}'.format(custo))
