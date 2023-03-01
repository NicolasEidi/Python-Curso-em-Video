"""     Exercício Python 6: 
    Crie um algoritmo que leia um número e 
    mostre o seu dobro, triplo e raiz quadrada.

    Resolução do exercício:
"""

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raizquad = numero **(1/2)
print('O dobro de {} é {} \nO triplo de {} é {} \nA raiz quadrada de {} é {:.2f}'.format(numero, dobro, numero, triplo, numero, raizquad))
