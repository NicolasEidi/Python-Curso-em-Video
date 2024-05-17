"""     Exercício Python 102:

    Crie um programa que tenha uma função fatorial() 
    que receba dois parâmetros: o primeiro que indique 
    o número a calcular e outro chamado show, 
    que será um valor lógico (opcional) indicando se 
    será mostrado ou não na tela o processo de cálculo do fatorial.

    Resolução do exercício:
"""

def fatorial(num, show=False):
    """Calcula Fatorial de um numero
    
    Keyword arguments: 
    num: Numero a ser calculado o fatorial
    show: (opcional) Mostrar ou nao o calculo
    Return: Retorna o fatorial 
    """
    
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(" x ", end='')
                
            else:
                print(" = ", end='')
        f *= c
    return f

print(fatorial(5, show=True))
help(fatorial)