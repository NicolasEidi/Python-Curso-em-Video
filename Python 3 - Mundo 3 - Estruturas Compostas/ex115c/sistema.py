from lib.interface import *
from lib.arquivo import *
from time import sleep

arquivo = "ex115c/arquivo.txt"

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Sair'])
    if resposta == 1:
        #Opcao de listar o conteudo de um arquivo 
        lerArquivo(arquivo)

    elif resposta == 2:
        #Opcao para cadastrar uma nova pessoa
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: ")).strip().capitalize()
        idade = leiaInt("Idade: ")
        cadastrar(arquivo, nome, idade)
    
    elif resposta == 3:
        cabecalho("Saindo... ")
        break

    else:
        cabecalho("\033[31mERRO: por favor, digite um numero inteiro valido\033[m")
    sleep(1)