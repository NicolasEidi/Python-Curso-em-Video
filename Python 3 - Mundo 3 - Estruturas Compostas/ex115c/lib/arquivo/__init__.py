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
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f"{dado[0]:<30}{dado[1]:>3} anos")

    finally:
        a.close()

def cadastrar(arquivo, nome='Desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')

    except:
        print("Houve um ERRO na abertura do arquivo")

    else:
        try:
            a.write(f"{nome};{idade}\n")
        
        except:
            print("Houve um EROO na hora de escrever os dados")

        else:
            print(f"Novo registro de {nome} adicionado")
            a.close()