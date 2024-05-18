import sys
from utilidades import moeda

sys.path.append('./ex111')

preco = float(input("Digite o preço: "))
moeda.resumo(preco, 50, 30)