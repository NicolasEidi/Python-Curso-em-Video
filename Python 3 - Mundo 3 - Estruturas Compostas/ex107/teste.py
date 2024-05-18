import sys
from moeda import metade, dobro, diminuir, aumentar

sys.path.append('./ex108')

preco = float(input("Digite o preço: "))
print(f"A metade de {preco} é {metade(preco)}")
print(f"O dobro de {preco} é {dobro(preco)}")
print(f"A diferença de 10% de {preco} é {diminuir(preco, 10)}")
print(f"O aumento de 10% de {preco} é {aumentar(preco, 10)}")