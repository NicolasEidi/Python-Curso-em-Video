"""     Exercício Python 36: 
    Escreva um programa para aprovar o empréstimo bancário 
    para a compra de uma casa. Pergunte o valor da casa, 
    o salário do comprador e em quantos anos ele vai pagar. 
    A prestação mensal não pode exceder 30% do salário 
    ou então o empréstimo será negado.

    Resolução do exercício:
"""

casa = int(input('Valor da casa: '))
salario = int(input('Salário: '))
pagamento = int(input('Pagar em quantos anos: '))

prestacao = casa / (pagamento * 12)

if prestacao >= (salario * 0.30):
    print('Você não tem condições de comprar essa casa') 

else:
    print('-----++' * 10)
    print(f'Você pagará a casa em {pagamento} meses\nNo valor de R${casa:.2f}\nCom prestações de R${prestacao:.2f}')
    print('-----++' * 10)
