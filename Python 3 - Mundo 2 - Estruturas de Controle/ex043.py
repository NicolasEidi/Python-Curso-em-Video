"""     Exercício Python 43: 
    Desenvolva uma lógica que leia o peso e 
    a altura de uma pessoa, calcule seu Índice 
    de Massa Corporal (IMC) e mostre seu status, 
    de acordo com a tabela abaixo:
    – IMC abaixo de 18,5: Abaixo do Peso
    – Entre 18,5 e 25: Peso Ideal
    – 25 até 30: Sobrepeso
    – 30 até 40: Obesidade
    – Acima de 40: Obesidade Mórbida

    Resolução do exercício:
"""

peso = float(input('Digite o seu peso (Kg): '))
altura = float(input('Digite a sua altura (m): '))
imc = peso / ((altura)**2)

if imc <= 18.5:
    print(f'Você está abaixo do peso, seu imc é {imc:.2f}')
elif imc <= 25:
    print(f'Você está no peso ideal, seu imc é {imc:.2f}')
elif imc <= 30:
    print(f'Você está com sobrepeso, seu imc é {imc:.2f}')
elif imc <= 40:
    print(f'Você está com obesidade, seu imc é {imc:.2f}')
else:
    print(f'você está com obesidade mórbida, seu imc é {imc:.2f}')
