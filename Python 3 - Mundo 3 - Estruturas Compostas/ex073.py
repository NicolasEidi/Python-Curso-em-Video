"""     Exercício Python 73:
    Crie uma tupla preenchida com os 20 primeiros 
    colocados da Tabela do Campeonato Brasileiro de Futebol, 
    na ordem de colocação. Depois mostre:
    a) Os 5 primeiros times.
    b) Os últimos 4 colocados.
    c) Times em ordem alfabética.
    d) Em que posição está o time da Chapecoense.

    Resolução do exercício:
"""

times = ("Palmeiras", "Athletico-PR", "Atlético-MG", "Corinthians", "Internacional", "Fluminense", "São Paulo", "Flamengo", "Botafogo", "Santos")
print("===---" * 10)
print(f"Os 5 primeiros colocados da tabela são: {times[0:5]}")
print(f"Os 4 ultimos  colocados da tabela são: {times[-4:]} ")
print(f"Os times em ordem alfabética {sorted(times)}")
pos = str(input("Qual time você quer saber a posição: ")).strip().capitalize()
while pos not in times:
    pos = str(input("Qual time você quer saber a posição: ")).strip().capitalize()
print(f"O {pos} está em {times.index(pos)+1}º posição")
print("===---" * 10)