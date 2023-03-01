"""     Exercício Python 69: 
    Crie um programa que leia a idade e o sexo de várias pessoas. 
    A cada pessoa cadastrada, o programa deverá perguntar se o 
    usuário quer ou não continuar. 
    No final, mostre:
    A) quantas pessoas tem mais de 18 anos.
    B) quantos homens foram cadastrados.
    C) quantas mulheres tem menos de 20 anos.

    Resolução do exercício:
"""

contadorHomem = contadorIdade = contadorMulher = 0

while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F]")).strip().upper()[0]

    if idade >= 18:
        contadorIdade += 1
    if sexo == "M":
        contadorHomem += 1
    if sexo == "F" and idade < 20:
        contadorMulher += 1

    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Deseja cadastrar mais uma pessoa? [S/N] ")).strip().upper()[0]

    if continuar == "N":
        break

print(f"Foi registrado {contadorIdade} pessoa(s) com mais de 18 anos\nFoi registrado {contadorHomem} homen(s) no total\nE {contadorMulher} mulhere(s) com menos de 20 anos")
