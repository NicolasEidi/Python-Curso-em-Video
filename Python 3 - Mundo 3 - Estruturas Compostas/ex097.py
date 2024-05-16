"""     Exercício Python 97:
    Faça um programa que tenha uma função chamada escreva(), 
    que receba um texto qualquer como parâmetro e mostre 
    uma mensagem com tamanho adaptável.
    Ex:escreva(‘Olá, Mundo!’) Saída:
    ~~~~~~~~~Olá, Mundo!~~~~~~~~~

    Resolução do exercício:
"""

def escreva(txt):
    tamanho = len(txt)
    print(f"=-{'-' * tamanho}-=")
    print(f"{txt:^{tamanho + 4}}")
    print(f"=-{'-' * tamanho}-=")


escreva(str(input("Digite um texto: ")))
