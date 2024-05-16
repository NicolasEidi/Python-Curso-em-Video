"""     Exercício Python 82:
    Crie um programa que vai ler vários números e 
    colocar em uma lista. Depois disso, 
    crie duas listas extras que vão conter apenas os valores 
    pares e os valores ímpares digitados, respectivamente. 
    Ao final, mostre o conteúdo das três listas geradas.

    Resolução do exercício:
"""

lista = []
par = []
impar = []
while True:
    lista.append(int(input("Digite um valor: ")))
    continuar = str(input("Deseja continuar: [S/N] ")).strip().upper()[0]
    while continuar not in "SN":
        continuar = str(input("Deseja continuar: [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
for c, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f"\nA lista completa é {lista}")
print(f"A lista dos números pares é {par}")
print(f"A lista dos números impares é {impar}")
