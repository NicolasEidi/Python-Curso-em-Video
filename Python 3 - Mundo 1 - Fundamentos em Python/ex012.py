"""     Exercício Python 12: 
    Faça um algoritmo que leia o preço de um produto 
    e mostre seu novo preço, com 5% de desconto.

    Resolução do exercício:
"""

p = float(input('Preço de um produto: R$'))
porcent = float(input('Quantos porcento de desconto: '))
porcent1 = porcent / 100
desconto = p * porcent1
novo_p = p - desconto
print('Valor do produto R${:.2f} \nValor do desconto R${:.2f} \nValor do produto com desconto R${:.2f}' .format(p, desconto, novo_p))
