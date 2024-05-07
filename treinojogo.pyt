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
x_cobra= int(largura/2)
y_cobra = int(altura/2)
relogio = pygame.time.Clock()


x_maca = randint(40,600)
y_maca = randint(50,430)

velocidade_x = 4
velocidade_y = 4
x_controle = 0
y_controle = 0

pontos = 0
fonte =pygame.font.SysFont('Comic Sans', 40, True, True)

tela = pygame.display.set_mode((largura, altura))


pygame.display.set_caption('CrazyRacing: Less Wanted')


lista_cobra = []
comprimento_inicial = 5

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
     #XeY = [x,y]
     #XeY[0] = x
     #XeY[1] = y  
        pygame.draw.rect(tela, (0,255,0), (XeY[0],XeY[1],20,20))
while True: 
    
    relogio.tick(60)
    tela.fill((255,255,255))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem,True,(0,0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if x_controle != velocidade_x:
                    pass
            else:
                    x_controle = -velocidade_x
                    y_controle = 0 
                   
            if event.key == K_RIGHT:
                if x_controle != -velocidade_x:
                    pass
            else:
                    x_controle = velocidade_x
                    y_controle = 0
                
            if event.key == K_UP:
                if y_controle != -velocidade_y:
                    pass
            else:
                    x_controle = 0
                    y_controle = velocidade_y  
                  
            if event.key == K_DOWN:
                if y_controle != velocidade_y:
                    pass
            else:
                    x_controle = 0 
                    y_controle = -velocidade_y
        
       
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
       
    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20))
     
    if cobra.colliderect(maca):
        x_maca = randint(40,600)
        y_maca = randint(50,430)
        pontos = pontos + 1
        barulho_colisao.play()
        comprimento_inicial = comprimento_inicial + 1
        
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    
    
    lista_cobra.append(lista_cabeca)
    
    if len(lista_cobra) > comprimento_inicial:
     del lista_cobra[0]
    aumenta_cobra(lista_cobra)
        
    tela.blit(texto_formatado, (400, 40))
    
    pygame.display.update()
