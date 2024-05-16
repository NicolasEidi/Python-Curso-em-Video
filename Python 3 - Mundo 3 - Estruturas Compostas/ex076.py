"""     Exercício Python 76:
    Crie um programa que tenha uma tupla única 
    com nomes de produtos e seus respectivos preços, 
    na sequência. No final, mostre uma listagem de preços, 
    organizando os dados em forma tabular.

    Resolução do exercício:
"""

produtos = ("Leite", 4, "Feijão", 10, "Sabão", 3.50, "Maçã", 2, "Banana", 2.50, "Arroz", 20, "Chá", 5)

print("===---" * 7)
print(f"{'LISTA DE COMPRAS':^40}")
print("===---" * 7)

for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f"{produtos[item]:.<30}.", end="")
    else:
        print(f"R${produtos[item]:>7.2f}")
        
print("===---" * 7)
