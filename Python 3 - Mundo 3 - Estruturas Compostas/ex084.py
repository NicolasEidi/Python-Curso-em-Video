"""     Exercício Python 84:
    Faça um programa que leia nome e peso de várias pessoas,
    guardando tudo em uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas.
    B) Uma listagem com as pessoas mais pesadas.
    C) Uma listagem com as pessoas mais leves.

    Resolução do exercício:
"""

total = []
pessoa = []
maior = menor = 0
while True:
    pessoa.append(str(input("Nome: ")))
    pessoa.append(int(input("Peso: ")))
    if len(total) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        elif pessoa[1] < menor:
            menor = pessoa[1]
    total.append(pessoa[:])
    pessoa.clear()
    continuar = str(input("Deseja continuar: [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break

print(f"Foram cadastradas {len(total)} pessoas")
print(f"O maior peso foi de {maior}Kg do(da) ", end="")
for p in total:
    if p[1] == maior:
        print(f"{p[0]} ", end="")
print()
print(f"O menor peso foi de {menor}Kg do(da) ", end="")
for p in total:
    if p[1] == menor:
        print(f"{p[0]} ", end="")
