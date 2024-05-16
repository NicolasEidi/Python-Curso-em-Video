"""     Exercício Python 75:
    Desenvolva um programa que leia quatro valores 
    pelo teclado e guarde-os em uma tupla. No final, mostre:
    A) Quantas vezes apareceu o valor 9.
    B) Em que posição foi digitado o primeiro valor 3.
    C) Quais foram os números pares.

    Resolução do exercício:
"""

numeros =  (int(input("Primeiro valor: ")),
            int(input("Segundo valor: ")),
            int(input("Terceiro valor: ")),
            int(input("Quarto valor: ")))

print(f"O número 9 aparece {numeros.count(9)}x")
if 3 in numeros:
    print(f"O número 3 apareceu {numeros.index(3)+1}º posição")
elif 3 not in numeros:
    print(f"O número 3 não apareceu em nenhuma posição")
print("Os valores pares são: ")
for c in numeros:
    if c % 2 == 0:
        print(c, end=" ")
