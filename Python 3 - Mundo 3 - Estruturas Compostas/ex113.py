"""     Exercício Python 113:

    Reescreva a função leiaInt() que fizemos no desafio 104, 
    incluindo agora a possibilidade da digitação de um número de tipo inválido. 
    Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

    Resolução do exercício:
"""

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))

        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um numero inteiro valido\033[m")

        except (KeyboardInterrupt):
            print("\033[31mEntrada de dados interrrompida pelo usuario\033[m")
            return 0

        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))

        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um real inteiro valido\033[m")

        except (KeyboardInterrupt):
            print("\033[31mEntrada de dados interrrompida pelo usuario\033[m")
            return 0

        else:
            return n



numInt = leiaInt("Digite um valor int: ")
numFloat = leiaFloat("Digite um valor float: ")
print(f"O valor inteiro digitado foi {numInt}, e o valor real foi {numFloat}")
