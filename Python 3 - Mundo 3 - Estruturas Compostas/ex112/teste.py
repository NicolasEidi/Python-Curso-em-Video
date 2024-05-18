import sys
from utilidades import moeda, dados

sys.path.append('./ex111')

preco = dados.leiaDinheiro("Digite o preço: ")
moeda.resumo(preco, 50, 30)