"""     Exercício Python 96: 
    Faça um programa que tenha uma função chamada área(),
    que receba as dimensões de um terreno retangular (largura e comprimento)
    e mostre a área do terreno.

    Resolução:
"""

def area(altura, largura):
    total = altura * largura
    print("-" * 30)
    print(f"{'Área do Terreno':^30}")
    print("-" * 30)
    print(f"A área de um terreno de {altura}m x {largura}m é: {total}m2")


area(int(input("Altura: ")), int(input("Largura: ")))
