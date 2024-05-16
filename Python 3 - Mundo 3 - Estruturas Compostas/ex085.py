"""     Exercício Python 85:
    Crie um programa onde o usuário possa digitar sete valores 
    numéricos e cadastre-os em uma lista única que mantenha 
    separados os valores pares e ímpares. No final, 
    mostre os valores pares e ímpares em ordem crescente.

    Resolução do exercício:
"""

números = [[], []]
valor = 0
for i in range(1, 8):
    valor = int(input(f"Digite o {i}º valor: "))
    if valor % 2 == 0:
        números[0].append(valor)
    elif valor % 2 == 1:
        números[1].append(valor)
números[0].sort()
números[1].sort()
print(f"Os valores pares são {números[0]}")
print(f"Os valores impares são {números[1]}")
