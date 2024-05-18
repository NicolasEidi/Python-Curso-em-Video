import sys
from moeda import *

sys.path.append('./ex108')

preco = float(input("Digite o preço: "))
print(f"A metade de {moeda(preco)} é {metade(preco, True)}")
print(f"O dobro de {moeda(preco)} é {dobro(preco, True)}")
print(f"A diferença de 10% de {moeda(preco)} é {diminuir(preco, 10, True)}")
print(f"O aumento de 10% de {moeda(preco)} é {aumentar(preco, 10, True)}")