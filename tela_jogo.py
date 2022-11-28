import pygame
import time
import random
from Snake_Nake import LARGURA, ALTURA

def game_screen1(janela):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    FPS = 30
    background = pygame.image.load('tela_principal1_ok.png').convert_alpha()
    game = True
    LARGURA = 600
    ALTURA = 400

    # Assets
    font = pygame.font.SysFont('Comics', 48)
    meteor_img = pygame.image.load('assets/img/meteorBrown_med1.png').convert_alpha()
    meteor_img = pygame.transform.scale(meteor_img, (20, 15))
    fruta_img = pygame.image.load('assets/img/laserRed16.png').convert_alpha()
    fruta_img = pygame.transform.scale(fruta_img, (20, 15))

    # velocidade cobra
    cobra_speed_x = 0
    cobra_speed_y = 0

    # Posição cobra
    cobra_x = (ALTURA/2)
    cobra_y = (LARGURA/2)
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
        # Atualização da posição da nave
            self.rect.x += self.speedx
            self.rect.y += self.speedy

            #Não permitir sair da tela
            if self.rect.right > LARGURA:
                self.rect.right = LARGURA
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.top > ALTURA:
                self.rect.top = ALTURA
            if self.rect.bottom < 0:
                self.rect.bottom = 0

    class Fruta(pygame.sprite.Sprite):
        def __init__(self, img):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(0, LARGURA)
            self.rect.y = random.randint(0, ALTURA)


    all_sprites = pygame.sprite.Group()
    all_frutas = pygame.sprite.Group()
    cobra = Ship(meteor_img)
    fruta = Fruta(fruta_img)
    all_sprites.add(fruta)
    all_sprites.add(cobra)
    all_frutas.add(fruta)

    while game:
        clock.tick(FPS)     


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    cobra.speedy = 0
                    cobra.speedx = +4
                if event.key == pygame.K_LEFT:
                    cobra.speedy = 0
                    cobra.speedx = -4
                if event.key == pygame.K_DOWN:
                    cobra.speedy = +4 
                    cobra.speedx = 0
                if event.key == pygame.K_UP:
                    cobra.speedy = -4
                    cobra.speedx = 0
                    
            if event.type == pygame.QUIT:
                game = False
                time.sleep(2)

                
        # Atualizando a posição das sprite
        all_sprites.update()
        hits = pygame.sprite.spritecollide(cobra, all_frutas, True)
        if hits != []:
            print('joao')
        for meteor in hits: # As chaves são os elementos da cobra que colidiram com alguma fruta
        # A fruta é comida e precisa ser recriada
            m = Fruta(fruta_img)
            all_sprites.add(m)
            all_frutas.add(m)

        janela.fill((8, 91, 7))
        cor = (255, 255, 0)
        
        all_sprites.draw(janela)

        pygame.display.update()

    return 2