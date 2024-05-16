"""     Exercício Python 78:
    Faça um programa que leia 5 valores numéricos 
    e guarde-os em uma lista. No final, mostre qual foi 
    o maior e o menor valor digitado e as suas respectivas 
    posições na lista.

    Resolução do exercício:
"""

valores = []
maior = menor = 0
for c in range(0, 5):
    valores.append(input(f"Digite o {c}º valor: "))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        elif valores[c] < menor:
            menor = valores[c]

print(f"O maior valor digitado é {maior} e ele apareceu nas posições ", end="")
for i, v in enumerate(valores):
    if v == maior:
        print(f"{i} ", end=",")
print()
print(f"O menor valor digitado é {menor} e ele apreceu nas posições ", end="")
for i, v in enumerate(valores):
    if v == menor:
        print(f"{i} ", end="")
