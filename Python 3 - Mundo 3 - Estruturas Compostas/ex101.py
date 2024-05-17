"""     Exercício Python 101:

    Crie um programa que tenha uma função chamada voto() 
    que vai receber como parâmetro o ano de nascimento 
    de uma pessoa, retornando um valor literal indicando 
    se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO 
    nas eleições.

    Resolução do exercício:
"""


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return f"Com {idade} anos: Não Vota"
    
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: Voto Opcional"
    
    else:
        return f"Com {idade} anos: Voto Obrigatório"
    
nascimento = int(input("Digite em que ano voce nasceu: "))
print(voto(nascimento))