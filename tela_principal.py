import pygame
import time

pygame.init()

LARGURA = 600
ALTURA = 400
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Snake Nake')

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
pygame.quit()