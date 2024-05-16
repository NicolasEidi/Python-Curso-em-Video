"""     Exercício Python 80:
    Crie um programa onde o usuário possa digitar cinco valores
    numéricos e cadastre-os em uma lista, já na posição correta 
    de inserção (sem usar o sort()). No final, mostre a lista 
    ordenada na tela.

    Resolução do exercício:
"""

valores = []
for c in range(0, 5):
    num = int(input("Digite um valor: "))
    if c == 0 or num > valores[-1]:
        valores.append(num)
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                break
            pos += 1
print(valores)
# 99 5 66 4 12