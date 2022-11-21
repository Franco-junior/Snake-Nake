import pygame
import time

pygame.init()

LARGURA = 600
ALTURA = 400
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Snake Nake')
background = pygame.image.load('tela_principal1.png').convert()
game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            time.sleep(2)
    janela.fill((255, 255, 255))
    janela.blit(background, (0, 0))
    background = pygame.transform.scale(background, (120, 84.94))

    pygame.display.update()

pygame.quit()