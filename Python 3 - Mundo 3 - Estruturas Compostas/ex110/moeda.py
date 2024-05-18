def aumentar(preco=0, taxa=0, format=False):
    res = preco + (preco * taxa/100)
    return res if format is False else moeda(res)

def diminuir(preco=0, taxa=0, format=False):
    res = preco - (preco * taxa/100)
    return res if format is False else moeda(res)

def dobro(preco=0, format=False):
    res = preco * 2
    return res if format is False else moeda(res)


def metade(preco=0, format=False):
    res = preco / 2
    return res if format is False else moeda(res)

def moeda(preco=0, moeda='R$'):
    return f"{moeda}{preco:.2f}".replace('.',',')

def resumo(preco=0, taxa_aumento=10, taxa_reducao=5):
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("=" * 30)
    print(f"Preco analisado {moeda(preco)}\n")
    print(f"A metade do preco \t{metade(preco, True)}")
    print(f"O dobro do preco \t{dobro(preco, True)}")
    print(f"A diferença de {taxa_aumento}% \t{diminuir(preco, taxa_aumento, True)}")
    print(f"O aumento de {taxa_reducao}% \t{aumentar(preco, taxa_reducao, True)}")