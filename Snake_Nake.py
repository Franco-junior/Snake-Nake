# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import time
from tela_inicial import init_screen
from tela_jogo import game_screen1


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('som do jogo.mp3')
pygame.mixer.music.set_volume(4)
pygame.mixer.music.play(-1)

# ----- Gera tela principal
LARGURA = 600
ALTURA = 400
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Snake Nake')

state = 1
while state != 2:
    if state == 1:
        state = init_screen(janela)
    if state == 3:
        state = game_screen1(janela)
    else:
        state = 2
        
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

