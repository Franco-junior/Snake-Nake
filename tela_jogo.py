import pygame
import time
import random

LARGURA = 600
ALTURA = 400
FPS = 30
def game_screen1(janela):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    background = pygame.image.load('tela_principal1_ok.png').convert_alpha()
    game = True

    # Assets
    font = pygame.font.SysFont('Comics', 48)
    meteor_img = pygame.image.load('assets/img/meteorBrown_med1.png').convert_alpha()
    meteor_img = pygame.transform.scale(meteor_img, (20, 15))
    fruta_img = pygame.image.load('assets/img/laserRed16.png').convert_alpha()
    fruta_img = pygame.transform.scale(fruta_img, (20, 15))
    
    #Função para aumentar a cobra
    
    #def aumenta_cobra(lista_cobra):
        #for XeY in lista_cobra:
            #XeY = [x, y]
            #XeY[0] = x
            #XeY[1] = y

            #pygame.draw.rect(janela, (0,255,0), (XeY[0], XeY[1], 20, 20))

    # velocidade cobra
    #cobra_speed_x = 0
    #cobra_speed_y = 0

    # Posição cobra
    
    cobra_x = (ALTURA/2)
    cobra_y = (LARGURA/2)
    lista_cobra = [cobra_x, cobra_y]
    cobra = 6
    
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

        def update(self):
        # Atualização da posição da cobra
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

        def __init__(self, img):
            
            pygame.sprite.Sprite.__init__(self)
            
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.centerx = lista_cobra[0]
            self.rect.bottom = lista_cobra[1]
            self.speedx = cobra.speedx
            self.speedy = cobra.speedy

        def update(self):
        # Atualização da posição da cobra
            self.rect.x += cobra.speedx
            self.rect.y += cobra.speedy

    all_sprites = pygame.sprite.Group()
    all_frutas = pygame.sprite.Group()
    all_corpo = pygame.sprite.Group()
    cobra = Ship(meteor_img)
    corpo = Corpo(meteor_img)
    fruta = Fruta(fruta_img)
    all_sprites.add(fruta)
    all_sprites.add(cobra)
    all_frutas.add(fruta)

    

    while game:
        clock.tick(FPS)     


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if cobra.speedx == -4:
                        pass
                    else:
                        cobra.speedx = +4
                        cobra.speedy = 0
                if event.key == pygame.K_LEFT:
                    if cobra.speedx == 4:
                        pass
                    else:
                        cobra.speedx = -4
                        cobra.speedy = 0
                if event.key == pygame.K_DOWN:
                    if cobra.speedy == -4:
                        pass
                    else:
                        cobra.speedx = 0
                        cobra.speedy = 4
                if event.key == pygame.K_UP:
                    if cobra.speedy == 4:
                        pass
                    else:
                        cobra.speedx = 0
                        cobra.speedy = -4
                    
            if event.type == pygame.QUIT:
                game = False
                time.sleep(2)

                
        # Atualizando a posição das sprite
        lista_cobra = [corpo.rect.x, cobra.rect.y]
        all_sprites.update()
        hits = pygame.sprite.spritecollide(cobra, all_frutas, True)
        if hits != []:
            lista_cobra[0] = corpo.rect.x
            lista_cobra[1] = corpo.rect.y
            
        for k in hits: # As chaves são os elementos da cobra que colidiram com alguma fruta
        # A fruta é comida e precisa ser recriada
            m = Fruta(fruta_img)
            alo = Corpo(meteor_img)
            all_sprites.add(alo)
            all_sprites.add(m)
            all_frutas.add(m)
            all_corpo.add(alo)

        # Aumentando a cobra
        #lista_cabeca = []
        #lista_cabeca.append(cobra_x)
        #lista_cabeca.append(cobra_y)
        #lista_cobra.append(lista_cabeca)
        #aumenta_cobra(lista_cobra)

        janela.fill((8, 91, 7))
        cor = (255, 255, 0)
        
        all_sprites.draw(janela)

        pygame.display.update()

    return 2