import pygame
from pygame.locals import *
from sys import exit
from random import randint
pygame.init()

pygame.mixer.music.set_volume(0.2)
musica_de_fundo = pygame.mixer.music.load('pacman_beginning.wav')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('pacman_eatfruit.wav')
barulho_colisao.set_volume(0.3)

largura = 640
altura = 480 
x = int(largura/2)
y = int(altura/2)
relogio = pygame.time.Clock()

x_verde = randint(40,600)
y_verde = randint(50,430)

pontos = 0
fonte =pygame.font.SysFont('Comic Sans', 40, True, True)

tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption('CrazyRacing: Less Wanted')

while True: 
    
    relogio.tick(30)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem,True,(255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        # if event.type == KEYDOWN:
        #      if event.key == K_a:
        #          x = x - 20
        #      if event.key == K_d:
        #          x = x + 20
        #      if event.key == K_w:
        #          y = y - 20
        #      if event.key == K_s:
        #          y = y + 20 
                         
        if pygame.key.get_pressed()[K_a]:
            x = x - 20
        if pygame.key.get_pressed()[K_d]:
            x = x + 20    
        if pygame.key.get_pressed()[K_w]:
            y = y - 20
        if pygame.key.get_pressed()[K_s]:
            y = y + 20          
       
    cobra = pygame.draw.circle(tela, (60,26,198), (x,y,40,50))
    maca = pygame.draw.circle(tela, (17,179,187), (x_verde,y_verde,40,50))
     
    if cobra.colliderect(maca):
        x_verde = randint(40,600)
        y_verde = randint(50,430)
        pontos = pontos + 1
        barulho_colisao.play()
        
    tela.blit(texto_formatado, (400, 40))
    
    pygame.display.update()
