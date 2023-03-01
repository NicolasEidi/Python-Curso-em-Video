"""     Exercício Python 44:
    Elabore um programa que calcule o valor a ser pago 
    por um produto, considerando o seu preço normal e condição de pagamento:
    – à vista dinheiro/cheque: 10% de desconto
    – à vista no cartão: 5% de desconto
    – em até 2x no cartão: preço formal 
    – 3x ou mais no cartão: 20% de juros

    Resolução do exercício:
"""

produto = int(input('Valor do produto: '))
print('Formas de pagamento: ')
pagamento = int(input('(1) A vista no dinheiro, 10% de desconto\n(2) A vista no cartão, 5% de desconto\n(3) Duas vezes no cartão, preço normal\n(4) 3x ou mais no cartão, 20% de juros\nEscolha: '))

if pagamento not in range(1, 5) :
    print('Digite outro valor de forma de pagamento')

elif pagamento == 1:
    desconto = produto - (produto * 0.10)
    print(f'A vista no dinheiro você ira pagar R${desconto:.2f}')

elif pagamento == 2:
    desconto = produto - (produto * 0.05)
    print(f'A vista no cartão você ira pagar R${desconto:.2f}')

elif pagamento == 3:
    parcela = produto / 2
    print(f'Em 2x no cartão você ira pagar R${produto:.2f} no total, cada parcela ira custar R${parcela:.2f}')

elif pagamento == 4:
    juros = produto + (produto * 0.20)
    parcelas = int(input('Quantas parcelas? '))
    total =juros / parcelas
    print(f'Em {parcelas}x no cartão você ira pagar R${juros:.2f}, cada parcela ira custar R${total:.2f}')
