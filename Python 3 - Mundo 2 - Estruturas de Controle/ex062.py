"""     Exercício Python 62: 
    Melhore o DESAFIO 61, perguntando para o usuário se ele 
    quer mostrar mais alguns termos. O programa encerrará 
    quando ele disser que quer mostrar 0 termos.

    Resolução do exercício:
"""

num = int(input("Primeiro termo: "))
razão = int(input("Razão: "))

termo = num
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo} -> ", end = "")
        termo += razão
        cont += 1
    mais = int(input("Mais quantos termos você quer ver: "))

print(f"O total de termos nessa PA foi de {total}")
