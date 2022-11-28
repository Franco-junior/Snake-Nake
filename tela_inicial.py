import pygame
import time

FPS = 30
def init_screen(janela):
    #define o relogio do jogo
    clock = pygame.time.Clock()
    # background e letreiros da tela inicial
    background = pygame.image.load('tela_principal1_ok.png').convert_alpha()
    game = True

    # Assets
    font = pygame.font.SysFont('Comics', 35)
    text1 = font.render('Normal', True, (0, 0, 255))
    text2 = font.render('Vs PC', True, (0, 0, 255))
    text3 = font.render('Crazy', True, (0, 0, 255))
    mode = font.render('Escolha seu modo:', True, (0, 0, 0))


    while game:
        clock.tick(FPS)
        #verifica qual botão foi clicado para início do jogo de acordo com a fase escolhida
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if botao1.collidepoint((x,y)):
                    print('camila')
                    state = 3
                    game = False
                elif botao2.collidepoint((x,y)):
                    print('joao')
                    state = 3
                    game = False
                elif botao3.collidepoint((x,y)):
                    print('matheus')
                    state = 3
                    game = False
            if event.type == pygame.QUIT:
                game = False
                state = 2
                time.sleep(2)

            janela.fill((8, 91, 7))
            cor = (255, 255, 0)
            vertices1 = [(75, 300), (175, 300), (175, 350), (75, 350)]
            vertices2 = [(250, 300), (350, 300), (350, 350), (250, 350)]
            vertices3 = [(425, 300), (525, 300), (525, 350), (425, 350)]
            botao1 = pygame.draw.polygon(janela, cor, vertices1)
            botao2 = pygame.draw.polygon(janela, cor, vertices2)
            botao3 = pygame.draw.polygon(janela, cor, vertices3)
        
            janela.blit(background, (190, 60))
            janela.blit(mode, (190, 250))
            janela.blit(text1, (82, 313))
            janela.blit(text2, (265, 314))
            janela.blit(text3, (440, 315))
            background = pygame.transform.scale(background, (200, 160))
            pygame.display.flip()

    return state
