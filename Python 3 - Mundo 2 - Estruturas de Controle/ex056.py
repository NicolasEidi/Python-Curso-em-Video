"""     Exercício Python 56: 
    Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
    No final do programa, mostre: a média de idade do grupo, 
    qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

    Resolução do exercício:
"""

soma = 0
idade_velho = 0
homem_velho = ''
totalm = 0

for i in range(1, 5):
    print('===-----'*10)
    nome = str(input('Nome: ')).strip().lower()
    idade = int(input('Idade: '))
    sexo = int(input('Sexo: (1) Masculino, (0)Feminino: '))
    soma += idade
    if sexo == 1 and i == 1:
        idade_velho = idade
        homem_velho = nome
    if sexo == 1 and idade_velho < idade:
        idade_velho = idade
        homem_velho = nome
    if sexo == 0 and idade < 20:
        totalm += 1

media_idade = soma / 4

print(f'A média de idade dessas pessoas é {media_idade}')
print(f'O homem mais velho tem {idade_velho} anos, e se chama {homem_velho.capitalize()}')
print(f'Tem {totalm} mulheres menores de 20 anos')
