"""     Exercício Python 21: 
    Faça um programa em Python que abra e 
    reproduza o áudio de um arquivo MP3.

    Resolução do exercício:
"""

import pygame

pygame.init()
pygame.mixer.music.load(r'ex21.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
