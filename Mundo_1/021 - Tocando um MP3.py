# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
from pathlib import Path

import pygame

musica = Path(__file__).with_name('musica.mp3')
if not musica.is_file():
    raise FileNotFoundError(
        f'Arquivo de áudio não encontrado: {musica}. '
        'Coloque um arquivo chamado musica.mp3 nesta pasta.'
    )

pygame.init()
pygame.mixer.music.load(str(musica))
pygame.mixer.music.play()
pygame.event.wait()