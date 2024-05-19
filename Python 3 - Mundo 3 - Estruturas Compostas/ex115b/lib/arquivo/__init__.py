from lib.interface import *

def arquivoExiste(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()

    except FileNotFoundError:
        return False
    
    else:
        return True


def criarArquivo(arquivo):
    try:
        a = open(arquivo, 'wt+')
        a.close()

    except:
        print("Houve um ERRO na criacao do arquivo")

    else:
        print(f"Arquivo {arquivo} criado com sucesso")


def lerArquivo(arquivo):
    try:
        a = open(arquivo, 'rt')

    except:
        print("Erro ao ler o arquivo")

    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(a.read())