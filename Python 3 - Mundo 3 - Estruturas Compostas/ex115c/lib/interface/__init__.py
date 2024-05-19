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



def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f"\033[31m{c}\033[m - \033[34m{item}\033[m")
        c += 1
    
    print(linha())
    opc = leiaInt("\033[32mSua Opcao: \033[m")

    return opc