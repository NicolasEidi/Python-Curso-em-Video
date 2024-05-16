"""     Exercício Python 94:
    Crie um programa que leia nome, sexo e idade de várias 
    pessoas, guardando os dados de cada pessoa em um dicionário 
    e todos os dicionários em uma lista. No final, mostre: 
    A) Quantas pessoas foram cadastradas 
    B) A média de idade 
    C) Uma lista com as mulheres 
    D) Uma lista de pessoas com idade acima da média

    Resolução do exercício:
"""

lista = []
pessoa = {}
total_idade = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input("Digite seu nome: ")).capitalize()
    while True:
        pessoa['Sexo'] = str(input("Seu sexo [M/F]: ")).strip().upper()[0]
        if pessoa['Sexo'] in "MF":
            break
        print("Por favor digite apenas M ou F")
    pessoa['Idade'] = int(input("Sua idade: "))
    total_idade += pessoa['Idade']
    lista.append(pessoa.copy())
    while True:
        continuar = str(input("Deseja cadastrar mais alguém: [S/N]: ")).strip().upper()[0]
        if continuar in "SN":
            break
        print("Digite apenas S ou N")
    if continuar == "N":
        break
media = total_idade / len(lista)
print("===---" * 10)
print(f"A) Foram cadastradas {len(lista)} pessoas")
print(f"B) A média de idade do grupo é {media}")
print(f"C) Todas as mulheres cadastradas são: ", end="")
for p in lista:
    if p['Sexo'] in "Ff":
        print(f"{p['Nome']} ", end="")
print()
print("D) A lista das pessoas que estão acima da média é: ", end="")
for p in lista:
    if p['Idade'] >= media:
        print("    ", end="")
        for k, v in p.items():
            print(f"{k} = {v}, ", end="")
        print()
print("Fim")
