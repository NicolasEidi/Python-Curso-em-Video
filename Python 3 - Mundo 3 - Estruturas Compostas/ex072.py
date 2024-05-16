"""     Exercício Python 72:
    Crie um programa que tenha uma dupla totalmente 
    preenchida com uma contagem por extenso, de zero até vinte. 
    Seu programa deverá ler um número pelo teclado 
    (entre 0 e 20) e mostrá-lo por extenso.

    Resolução do exercício:
"""


numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez")
num = int(input("Qual número quer ver por extenso [0 a 10]: "))
while True:
    while num not in range(0, 11):
        num = int(input("Qual número quer ver por extenso [0 a 10]: "))
    print(f"Você digitou o número {numeros[num]}")
    continuar = str(input("Deseja ver outro número: [S/N]: ")).strip().upper()[0]
    while continuar not in "SN":
        continuar = str(input("Deseja ver outro número: [S/N]: ")).strip().upper()[0]
    if continuar == "N":
        break
    else:
        num = int(input("Qual número quer ver por extenso [0 a 10]: "))
