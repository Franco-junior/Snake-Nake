import pygame
import time
import random

LARGURA = 600
ALTURA = 400
FPS = 30
def game_screen1(janela):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    background = pygame.image.load('fundo-de-textura-grunge-verde_1409-1374.jpg').convert_alpha()
    game = True

    # Assets
    font = pygame.font.SysFont(None, 48)
    cobrinha = pygame.image.load('cobrinha.png').convert_alpha()
    cobrinha = pygame.transform.scale(cobrinha, (30,15))
    cobra_cima = pygame.image.load('cobra_cima.png').convert_alpha()
    cobra_cima = pygame.transform.scale(cobra_cima, (15, 30))
    cobra_esquerda = pygame.image.load('cobra_esquerda.png').convert_alpha()
    cobra_esquerda = pygame.transform.scale(cobra_esquerda, (30, 15))
    cobra_baixo = pygame.image.load('cobra_baix.png').convert_alpha()
    cobra_baixo = pygame.transform.scale(cobra_baixo, (15, 30))
    meteor_img = pygame.image.load('assets/img/meteorBrown_med1.png').convert_alpha()
    meteor_img = pygame.transform.scale(meteor_img, (20, 15))
    fruta_img = pygame.image.load('comida.png').convert_alpha()
    fruta_img = pygame.transform.scale(fruta_img, (20, 15))
    
    #Função para aumentar a cobra
    
    '''def aumenta_cobra(lista_cobra):
        for i in range(len(lista_cobra)):
            X = lista_cobra[i][0]
            Y = lista_cobra[i][1]
            pygame.draw.rect(janela, (0,255,0), (X, Y, 20, 20))'''

    # velocidade cobra
    cobra_speed_x = 0
    cobra_speed_y = 0

    # Posição cobra
    
    cobra_x = (ALTURA/2)
    cobra_y = (LARGURA/2)
    lista_cobra = [cobra_x, cobra_y]
    cobra = 6
    
    score = 0
    # Estrutura

    class Ship(pygame.sprite.Sprite):

        def __init__(self, img):
            
            pygame.sprite.Sprite.__init__(self)
            
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.centerx = 300
            self.rect.bottom = 200
            self.speedx = 0
            self.speedy = 0
            self.x_anterior = self.rect.x
            self.y_anterior = self.rect.y

        def update(self):
        # Atualização da posição da cobra
            self.x_anterior = self.rect.x
            self.y_anterior = self.rect.y
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            

            #Não permitir sair da tela
            if self.rect.right > LARGURA:
                self.rect.right = LARGURA
                pygame.quit()
            if self.rect.left < 0:
                self.rect.left = 0
                pygame.quit()
            if self.rect.top > ALTURA - 15:
                self.rect.top = ALTURA - 15
                pygame.quit()
            if self.rect.bottom < 15:
                self.rect.bottom = 15
                pygame.quit()

    class Fruta(pygame.sprite.Sprite):
        def __init__(self, img):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(0, LARGURA-30)
            self.rect.y = random.randint(0, ALTURA-30)

    class Corpo(pygame.sprite.Sprite):

        def __init__(self, img, corpo):
            
            pygame.sprite.Sprite.__init__(self)
            
            self.image = img
            self.rect = self.image.get_rect()
            self.speedx = corpo.speedx
            self.speedy = corpo.speedy
            self.corpo = corpo
            if self.speedx > 0:
                self.rect.x = corpo.rect.x - 30
                self.rect.y = corpo.rect.y
            elif self.speedx < 0:
                self.rect.x = corpo.rect.x + 30
                self.rect.y = corpo.rect.y
            elif self.speedy > 0:
                self.rect.x = corpo.rect.x
                self.rect.y = corpo.rect.y - 15
            elif self.speedy < 0:
                self.rect.x = corpo.rect.x
                self.rect.y = corpo.rect.y + 15
            self.x_anterior = self.rect.x
            self.y_anterior = self.rect.y

        def update(self):
        # Atualização da posição da cobra
            self.x_anterior = self.rect.x
            self.y_anterior = self.rect.y
            self.rect.x = self.corpo.x_anterior 
            self.rect.y = self.corpo.y_anterior 

    all_sprites = pygame.sprite.Group()
    all_frutas = pygame.sprite.Group()
    all_corpo = pygame.sprite.Group()
    cobra = Ship(cobrinha)
    #corpo = Corpo(cobrinha, lista_cobra[0], lista_cobra[1])
    ultimo_pedaco = cobra
    fruta = Fruta(fruta_img)
    all_sprites.add(fruta)
    all_sprites.add(cobra)
    all_frutas.add(fruta)

    

    while game:
        clock.tick(FPS)     


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if cobra.speedx == -10:
                        pass
                    else:
                        cobra.speedx = +10
                        cobra.speedy = 0
                if event.key == pygame.K_LEFT:
                    if cobra.speedx == 10:
                        pass
                    else:
                        cobra.speedx = -10
                        cobra.speedy = 0
                if event.key == pygame.K_DOWN:
                    if cobra.speedy == -10:
                        pass
                    else:
                        cobra.speedx = 0
                        cobra.speedy = 10
                if event.key == pygame.K_UP:
                    if cobra.speedy == 10:
                        pass
                    else:
                        cobra.speedx = 0
                        cobra.speedy = -10
                    
            if event.type == pygame.QUIT:
                game = False
                time.sleep(2)
        

                
        # Atualizando a posição das sprite
        lista_cobra = [cobra.rect.x, cobra.rect.y]
        all_sprites.update()
        hits = pygame.sprite.spritecollide(cobra, all_frutas, True)
        if hits != []:
            lista_cobra[0] = cobra.rect.x
            lista_cobra[1] = cobra.rect.y
            pygame.mixer.music.load('apple_bite.ogg')
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(0)
            score += 100

            
        for k in hits: # As chaves são os elementos da cobra que colidiram com alguma fruta
        # A fruta é comida e precisa ser recriada
            m = Fruta(fruta_img)
            alo = Corpo(cobrinha, ultimo_pedaco)
            ultimo_pedaco = alo
            all_sprites.add(alo)
            all_sprites.add(m)
            all_frutas.add(m)
            all_corpo.add(alo)

        #hits1 = pygame.sprite.spritecollide(cobra, all_corpo, True)
        #if len(hits1) > 1:
            #game = False


        # Aumentando a cobra
        '''lista_cabeca = []
        lista_cabeca.append(cobra_x)
        lista_cabeca.append(cobra_y)
        lista_cobra.append(lista_cabeca)
        aumenta_cobra(lista_cobra)'''

        janela.fill((8, 91, 7))
        janela.blit(background, (0, 0))
        background = pygame.transform.scale(background, (600, 400))
        #texto do score
        texto_score = font.render('SCORE: {0}'.format(score), True, (255, 255, 255))
        score_rect = texto_score.get_rect()
        score_rect.midtop = (LARGURA / 2,  10)
        janela.blit(texto_score, score_rect)
        cor = (255, 255, 0)
        
        all_sprites.draw(janela)

        pygame.display.update()

    return 2