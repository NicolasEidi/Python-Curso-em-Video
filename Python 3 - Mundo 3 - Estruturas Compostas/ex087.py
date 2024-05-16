"""     Exercício Python 87:
    Aprimore o desafio anterior, mostrando no final:
    A) A soma de todos os valores pares digitados.
    B) A soma dos valores da terceira coluna.
    C) O maior valor da segunda linha.

    Resolução do exercício:
"""

matriz = [0,0,0], [0,0,0], [0,0,0]
pares = coluna3 = maior = 0
for c in range(0, 3):
    for v in range(0, 3):
        valor =  int(input(f"Digite o valor para [{c},{v}]: "))
        matriz[c][v] = (valor)
        if valor % 2 == 0:
            pares += valor
        if v == 2:
            coluna3 += valor
        if c == 1:
            if matriz[1][0] > maior:
                maior = matriz[1][0]
            if matriz[1][1] > maior:
                maior = matriz[1][1]
            if matriz[1][2] > maior:
                maior = matriz[1][2] 
for c in range(0, 3):
    for v in range(0, 3):
        print(f"({matriz[c][v]:^5}) ", end="")
    print()
print(f"A soma de todos os pares são: {pares}")
print(f"A soma dos valores da 3º coluna é: {coluna3}")
print(f"O maior valor da segunda linha é: {maior}")
