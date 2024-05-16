"""     Exercício Python 86:
    Crie um programa que declare uma matriz de dimensão 3×3 
    e preencha com valores lidos pelo teclado. No final, 
    mostre a matriz na tela, com a formatação correta.

    Resolução do exercício:
"""

matriz = [[], [], []], [[], [], []], [[], [], []]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (input(f"Digite um valor para [{l}, {c}]: "))
for l in range(0, 3):
    for c in range(0, 3):
        print(f"({matriz[l][c]:^5}) ", end="")
    print()
