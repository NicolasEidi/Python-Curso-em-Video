"""     Exercício Python 79:
    Crie um programa onde o usuário possa digitar vários valores 
    numéricos e cadastre-os em uma lista. Caso o número já exista 
    lá dentro, ele não será adicionado. No final, 
    serão exibidos todos os valores únicos digitados, 
    em ordem crescente.

    Resolução do exercício:
"""

num = []
while True:
    numero = int(input("Digite um valor: "))
    if numero not in num:
        num.append(numero)
        print("Valor adicionado...")
    else:
        print("Valor duplicado, não será considerado")
    continuar = str(input("Deseja continuar: [S/N] ")).strip().upper()[0]
    while continuar not in "SN":
        continuar = str(input("Deseja continuar: [S/N] ")).strip().upper()[0]
    
    if continuar == "N":
        break
print("===---" * 10)
print(f"A lista dos valores digitados são {sorted(num)}")
