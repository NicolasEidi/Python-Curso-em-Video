"""     Exercício Python 98:
    Faça um programa que tenha uma função chamada contador(),
    que receba três parâmetros: início, fim e passo. 
    Seu programa tem que realizar três contagens através da função criada:
    a) de 1 até 10, de 1 em 1                                                                                                                                              
    b) de 10 até 0, de 2 em 2                                                                                                                                            
    c) uma contagem personalizada

    Resolução do exercício:
"""
from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1

    if passo == 0:
        passo = 1

    print("=-" * 20)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    sleep(2)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f"{cont} ", end='', flush=True)
            sleep(0.5)
            cont += passo
        print("Fim!")

    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont} ", end='', flush=True)
            sleep(0.5)
            cont -= passo
        print("Fim!")
    

#contador(1, 10, 1)
#contador(10, 0, 2)
print("=-" * 20)
print("Insira o numero para o inicio, fim e passo")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)