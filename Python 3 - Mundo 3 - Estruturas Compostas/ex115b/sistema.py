from lib.interface import *
from lib.arquivo import *
from time import sleep

arquivo = "ex115b/arquivo.txt"

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Sair'])
    if resposta == 1:
        #Opcao de listar o conteudo de um arquivo 
        lerArquivo(arquivo)

    elif resposta == 2:
        cabecalho("Opcao 2")
    
    elif resposta == 3:
        cabecalho("Saindo... ")
        break

    else:
        cabecalho("\033[31mERRO: por favor, digite um numero inteiro valido\033[m")
    sleep(1)