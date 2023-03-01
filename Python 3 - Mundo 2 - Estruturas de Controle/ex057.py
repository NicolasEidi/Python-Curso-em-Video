"""     Exercício Python 57: 
    Faça um programa que leia o sexo de uma pessoa, 
    mas só aceite os valores "M" ou "F". 
    Caso esteja errado, peça a digitação novamente até ter um valor correto.

    Resolução do exercício:
"""

sexo = str(input("Digite seu sexo: [F/M]: ")).strip().upper()[0]

while sexo not in "FM":
    sexo = str(input("Digite seu sexo novamente [F/M]: ")).strip().upper()[0]

print(f"Seu sexo é {sexo}")
