"""     Exercício Python 105:

    Faça um programa que tenha uma função notas() 
    que pode receber várias notas de alunos e vai 
    retornar um dicionário com as seguintes informações:

    – Quantidade de notas                                                                                                                                                  
    – A maior nota                                                                                                                                                                
    – A menor nota                                                                                                                                                              
    – A média da turma                                                                                                                                                      
    – A situação (opcional)
    Resolução do exercício:
"""

def notas(*notas, situacao=False):
    """Analise notas de alunos
    
    Keyword arguments:
    notas: Uma ou mais notas dos alunos
    situacao: (opcional) indica se deve ou nao adicionar a situacao
    Return: dicionario com varias informacoes sobre a situacao da turma
    """
    
    r = dict()
    r['total'] = len(notas)
    r['maior'] = max(notas)
    r['menor'] = min(notas)
    r['media'] = sum(notas)/len(notas)

    if situacao:
        if r['media'] >= 7:
            r['situacao'] = 'Boa'

        elif r['media'] >=5: 
            r['situacao'] = 'Razoavel' 
        
        else:
            r['situacao'] = 'Ruim' 
    return r
resposta = notas(5.5, 2.5, 1.5, situacao=True)
print(resposta)
help(notas)