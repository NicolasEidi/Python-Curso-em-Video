"""     Exercício Python 99:

    Exercício Python 099: Faça um programa que tenha uma função chamada maior(), 
    que receba vários parâmetros com valores inteiros. 
    Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

    Resolução do exercício:
"""

def maior(*numeros):
    cont = maior_valor = 0
    print("=-" * 20)
    print("Analisando")
    for valor in numeros:
        print(f"{valor} ", end='')
        if cont == 0:
            maior_valor = valor
        
        else:
            if valor > maior_valor:
                maior_valor = valor
        
        cont += 1
    
    print(f"\nForam informados {cont} valores. ")
    print(f"O maior valor é {maior_valor}\n")

maior(99, 2, 4, 5 , 6)
maior(0, 8, 5)
maior(4, 2, 4)