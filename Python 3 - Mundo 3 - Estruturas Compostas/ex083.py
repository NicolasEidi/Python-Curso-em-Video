"""     Exercício Python 83:
    Crie um programa onde o usuário digite uma expressão qualquer
    que use parênteses. Seu aplicativo deverá analisar se a 
    expressão passada está com os parênteses abertos e fechados 
    na ordem correta.

    Resolução do exercício:
"""

express = input("Digite uma expressão matemática: ")
total = []
for caract in express:
    if caract == "(":
        total.append("(")
    elif caract == ")":
        if len(total) > 0:
            total.pop()
        else:
            total.append(")")
if len(total) == 0:
    print("Essa expressão é válida")
else:
    print("Essa expressão é ínvalida")
