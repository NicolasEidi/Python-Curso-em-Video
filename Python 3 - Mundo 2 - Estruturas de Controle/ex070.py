"""     Exercício Python 70: 
    Crie um programa que leia o nome e o preço de vários produtos. 
    O programa deverá perguntar se o usuário vai continuar ou não. 
    No final, mostre:
    A) qual é o total gasto na compra.
    B) quantos produtos custam mais de R$1000.
    C) qual é o nome do produto mais barato.

    Resolução do exercício:
"""

total = tot1000 = cont = 0
nomebarato = ""

while True:
    nomeP = str(input("Nome do produto: ")) 
    preço = int(input("Preço do produto: "))
    cont += 1
    if cont == 1 or preço < barato:
        barato = preço
        nomebarato = nomeP
    if preço >= 1000:
        tot1000 += 1
    
    total += preço

    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break

print(f"Total gasto na compra R${total:.2f} reais, Tem {tot1000} produtos que custaram mais de R$1000.00 reais")
print(f"O produto mais barato é {nomebarato} custando R${barato:.2f} reais")
