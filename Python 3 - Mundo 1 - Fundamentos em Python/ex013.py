"""     Exercício Python 13: 
    Faça um algoritmo que leia o salário de um funcionário 
    e mostre seu novo salário, com 15% de aumento.

    Resolução do exercício:
"""

salario = int(input('Salário: R$'))
porcent = int(input('Aumento em porcentos: '))
porcent1 = porcent / 100
salarioaument = salario * porcent1
salarioaument1 = salario + salarioaument
print('Salário atual: R${:.2f} \nPorcentagem de aumento: {}% \nQuanto de aumento vai ter: R${:.2f} \nSalário novo: R${:.2f}'.format(salario, porcent, salarioaument, salarioaument1))
