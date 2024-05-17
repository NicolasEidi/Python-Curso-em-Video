"""     Exercício Python 104:

    Crie um programa que tenha a função leiaInt(), 
    que vai funcionar de forma semelhante 
    a função input() do Python, só que fazendo a validação 
    para aceitar apenas um valor numérico. 
    Ex: n = leiaInt(‘Digite um n: ‘)

    Resolução do exercício:
"""
def leiaInt(mensagem):
    ok = False
    valor = 0

    while True:
        n = str(input(mensagem))
        if n.isnumeric():
            valor = int(n)
            ok = True

        else:
            print("\033[0;31mERRO Digite um valor inteiro valido. \033[m")
        
        if ok:
            break
    return valor

n = leiaInt("Digite um numero")
print(f"Voce digitou o numero {n}")
