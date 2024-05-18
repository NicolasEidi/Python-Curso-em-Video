import sys
from moeda import *

sys.path.append('./ex108')

preco = float(input("Digite o preço: "))
print(f"A metade de {moeda(preco)} é {moeda(metade(preco))}")
print(f"O dobro de {moeda(preco)} é {moeda(dobro(preco))}")
print(f"A diferença de 10% de {moeda(preco)} é {moeda(diminuir(preco, 10))}")
print(f"O aumento de 10% de {moeda(preco)} é {moeda(aumentar(preco, 10))}")