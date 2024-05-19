from lib.interface import *
from time import sleep

while True:
    resposta = menu(['Cadastrar Pessoas', 'Listar Pessoas', 'Sair'])
    if resposta == 1:
        cabecalho("Opcao 1")

    elif resposta == 2:
        cabecalho("Opcao 2")
    
    elif resposta == 3:
        cabecalho("Saindo... ")
        break

    else:
        cabecalho("\033[31mERRO: por favor, digite um numero inteiro valido\033[m")
    sleep(1)