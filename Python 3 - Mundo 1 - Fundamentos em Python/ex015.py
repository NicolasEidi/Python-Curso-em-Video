"""     Exercício Python 15: 
    Escreva um programa que pergunte a quantidade de Km percorridos 
    por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
    Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
    e R$0,15 por Km rodado.

    Resolução do exercício:
"""

km = float(input('Km percorridos: '))
dias = float(input('Dias percorridos: '))
custod = dias * 60
custokm = km * 0.15
print('Percorrendo {}Km, vai custar R${:.2f}'.format(km, custokm))
print('Percorrendo {} dias, vai custar R${:.2f}'.format(dias, custod))
print('Ao total vai gastar R${:.2f}'.format(custod + custokm))
