"""     Exercício Python 81:
    Crie um programa que vai ler vários números e 
    colocar em uma lista. Depois disso, mostre:
    A) Quantos números foram digitados.
    B) A lista de valores, ordenada de forma decrescente.
    C) Se o valor 5 foi digitado e está ou não na lista.

    Resolução do exercício:
"""

lista = []
while True:
    lista.append(input("Digite um valor: "))  
    continuar = str(input("Deseja continuar: [S/N] ")).strip().upper()[0]
    while continuar not in "SN":
        continuar = str(input("Deseja continuar: [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break

lista.sort(reverse=True)
print(f"\nFoi digitado {len(lista)} números")
print(f"Essa lista em forma decrescente é {lista}")
if 5 in lista:
    print(f"O valor 5 foi digitado {lista.count(5)} vezes")
else:
    print("O valor 5 não foi digitado")