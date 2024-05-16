"""     Exercício Python 92:
    Crie um programa que leia nome, ano de nascimento e carteira
    de trabalho e cadastre-o (com idade) em um dicionário. 
    Se por acaso a CTPS for diferente de ZERO, o dicionário 
    receberá também o ano de contratação e o salário. 
    Calcule e acrescente, além da idade, com quantos anos a 
    pessoa vai se aposentar.

    Resolução do exercício:
"""

from datetime import date
anoatual = date.today().year
pessoa = {}
print("---" * 30)
pessoa['Nome'] = str(input("Nome: ")).capitalize()
pessoa['Nascimento'] = int(input("Ano de nascimento: "))
pessoa['CTPS'] = int(input("Carteira de trabalho: [Se não tiver digite = 0] "))
pessoa['Idade'] = anoatual - pessoa['Nascimento']
if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input("Ano de contratação: "))
    pessoa['Salario'] = float(input("Salario: "))
    pessoa['Aposentadoria'] = (pessoa['Contratação'] + 35) - pessoa['Nascimento']
print("===---" * 10)
for k, v in pessoa.items():
    print(f"{k} tem valor de: {v} ")
print("---" * 30)
