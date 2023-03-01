"""     Exercício Python 10: 
    Crie um programa que leia quanto dinheiro uma pessoa 
    tem na carteira e mostre quantos dólares ela pode comprar.

    Resolução do exercício:
"""

dinheiro = float(input('Quanto de dinheiro tem em reais: R$'))
dolar = dinheiro / 3.27
dolar1 = dinheiro / 5.08 #Cotação do dolar do dia 12/08/22
print('Você tem em reais: {} \nE em dolar em 2017: {:.2f} \nHoje em dia em dolar: {:.2f}' .format(dinheiro, dolar, dolar1))
