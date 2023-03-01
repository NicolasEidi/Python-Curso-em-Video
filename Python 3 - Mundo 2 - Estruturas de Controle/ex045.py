"""     Exercício Python 45: 
    Crie um programa que faça o computador jogar Jokenpô com você.

    Resolução do exercício:
"""

from random import choice

lista = ('pedra', 'papel', 'tesoura')
pc = choice(lista)
jogador = str(input('Escolha entre: \n[Pedra] - [Papel] - [Tesoura]: ')).lower()

if jogador not in lista:
    print('Inicie novamente e escolha entre: \nPedra, Papel ou Tesoura')

elif pc == jogador:
    print(f'Empate, o computador jogou {pc}')

elif pc == ('pedra') and jogador == ('tesoura'):
    print(f'O computador ganhou jogando {pc}')

elif pc == ('papel') and jogador == ('tesoura'):
    print(f'Você ganhou! O computador escolheu {pc}')

elif pc == ('tesoura') and jogador == ('pedra'):
    print(f'Você ganhou! O computador escolheu {pc}')

elif pc == ('papel') and jogador == ('pedra'):
    print(f'O computador ganhou jogando {pc}')

elif pc == ('pedra') and jogador == ('papel'):
    print(f'Você ganhou! O computador escolheu {pc}')

elif pc == ('tesoura') and jogador == ('papel'):
    print(f'O computador ganhou jogando {pc}')
