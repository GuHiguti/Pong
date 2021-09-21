import pygame
from pygame.locals import *
import random
import time
import math
from sys import exit, maxsize
from os import system

#dimensões da tela
width = 1000
height = 640
altura_sup = 100
altura_inf = 620

#configurações barras
x1_init = 30
y1_init = int(height/2)-25
x1,y1 = x1_init,y1_init
x2 = width-x1_init-20
y2 = y1_init
larg_barra = 20
alt_barra = 70
vel_barra = 10
colide1 = time.time()

#configurações bola
xb = int(width/2)
yb = int(height/2)
b_radius = 10
velx_bola = 10
vely_bola = 7
B0 = 0

#pontuação
j1 = 0
j2 = 0
Vencedor = ''
P_max = 5

def mov_bola():
    global xb,yb,velx_bola,vely_bola
    if yb+b_radius<altura_inf and yb-b_radius>altura_sup:
        xb += velx_bola
        yb += vely_bola
    else:
        vely_bola = (-1)*vely_bola
        xb += velx_bola
        yb += vely_bola

def reset():
    #configurações barras
    global x1,y1,x2,y2,xb,yb,velx_bola,vely_bola,B0
    x1,y1 = x1_init,y1_init
    x2 = width-x1_init-20
    y2 = y1_init

    #configurações bola
    xb = int(width/2)
    yb = int(height/2)
    velx_bola = 7.5
    vely_bola = 10
    B0 = 0

pygame.init()

def formas():
    global barra1,barra2,bola
    barra1 = pygame.draw.rect(scr,(0,255,0),(x1,y1,larg_barra,alt_barra))
    barra2 = pygame.draw.rect(scr,(255,0,0),(x2,y2,larg_barra,alt_barra))
    bola = pygame.draw.circle(scr,(255,255,255),(xb,yb),b_radius)

fonte = pygame.font.SysFont('arial',30,bold=True,italic=True)#fonte de texto
fonteG = pygame.font.SysFont('arial',200,bold=True,italic=True)#fonte de texto

#configurar a tela
scr = pygame.display.set_mode((width, height))
pygame.display.set_caption("PONG GAME") #Nome da tela
relogio = pygame.time.Clock()

#loop principal
while True:
    relogio.tick(30) #frames per second
    scr.fill((10,10,10)) #clear screen
    mensagem1 = f'Jogador 1: {j1}'
    mensagem2 = f'Jogador 2: {j2}'
    texto1 = fonte.render(mensagem1, True, (255,255,255))
    texto2 = fonte.render(mensagem2, True, (255,255,255))

    #Events loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if B0==0:
        formas()
        velx_bola = velx_bola*random.choice([-1,1])
        vely_bola = vely_bola*random.choice([-1,1])
        B0=1

    if pygame.key.get_pressed()[K_w]:
        if y1>altura_sup:
            y1-=vel_barra
    if pygame.key.get_pressed()[K_s]:
        if y1+alt_barra<altura_inf:
            y1+=vel_barra
    if pygame.key.get_pressed()[K_UP]:
        if y2>altura_sup:
            y2-=vel_barra
    if pygame.key.get_pressed()[K_DOWN]:
        if y2+alt_barra<altura_inf:
            y2+=vel_barra

    if xb<0:
        j2+=1
        reset()
    elif xb>=width:
        j1+=1
        reset()
    if j1>=P_max or j2>=P_max:
        if j1>j2:
            Vencedor='Jogador 1 venceu!'
            mensagemVence = f'{Vencedor}'
            textoV = fonte.render(mensagemVence, True, (0,255,0))
        if j2>j1:
            Vencedor='Jogador 2 venceu!'
            mensagemVence = f'{Vencedor}'
            textoV = fonte.render(mensagemVence, True, (255,0,0))
        scr.blit(textoV, (400, 300))

    limite_cima = pygame.draw.line(scr,(255,255,255),(0,altura_sup),(width,altura_sup))
    limite_baixo = pygame.draw.line(scr,(255,255,255),(0,altura_inf),(width,altura_inf))
    formas()

    if bola.colliderect(barra1) or bola.colliderect(barra2):
        colide2 = time.time()
        if colide2 - colide1 > 0.5:
            velx_bola = velx_bola*(-1.1)
            _t = 0
        elif _t==0:
            vely_bola = (-1.2)*vely_bola
            velx_bola = velx_bola*(0.8)
            _t = 1
        colide1 = colide2

    mov_bola()

    scr.blit(texto1, ((width/2)-80, 10))
    scr.blit(texto2, ((width/2)-80, 40))

    pygame.display.flip()   