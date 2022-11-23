# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import time
from tela_inicial import init_screen
from tela_jogo import game_screen1



pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
LARGURA = 600
ALTURA = 400
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Snake Nake')

state = 1
while state != 2:
    if state == 1:
        state = init_screen(janela)
    elif state == 3:
        state = game_screen1(janela)
    else:
        state = 2
        
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

