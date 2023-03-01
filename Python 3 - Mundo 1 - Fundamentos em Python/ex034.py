"""     Exercício Python 34: 
    Escreva um programa que pergunte o salário de um funcionário e 
    calcule o valor do seu aumento. Para salários superiores a R$1250,00, 
    calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

    Resolução do exercício:
"""

salario = int(input('Salário: '))

if salario > 1250:
    aumento = salario * 0.10
    print(f'O salário de R${salario:.2f} teve um aumento de R${aumento:.2f}, ficando com R${salario+aumento:.2f}')
else:
    aumento = salario * 0.15
    print(f'O salário de R${salario:.2f} teve um aumento de R${aumento:.2f}, ficando com R${salario+aumento:.2f}')
