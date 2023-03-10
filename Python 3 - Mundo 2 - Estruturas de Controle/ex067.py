"""     Exercício Python 67: 
    Faça um programa que mostre a tabuada de vários números, 
    um de cada vez, para cada valor digitado pelo usuário. 
    O programa será interrompido quando o número solicitado for negativo.

    Resolução do exercício:
"""

while True:
    num = int(input("Qual tabuada deseja ver: "))
    print("===---" * 10)
    if num < 0:
        break
    for c in range(1, 11):
        print(f"{num} x {c} = {c * num}")
    print("===---" * 10)

print("Programa encerrado...")
print("===---" * 10)
