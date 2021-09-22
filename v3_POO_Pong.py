import pygame
import random
import time
from pygame.locals import *

class Pong:
    def __init__(self,P_max,V_bola,V_barra,Bot):
        pygame.init()
        self.largura = 1000
        self.altura_tela = 620
        self.altura_sup = 100
        self.altura_inf = 600
        self.y_init = 295
        self.y1 = self.y_init
        self.y2 = self.y_init
        self.x1 = 30
        self.x2 = 950
        self.xb = 500
        self.yb = 320
        self.j1 = 0
        self.j2 = 0
        self.B0 = 0
        self.P_max = P_max
        self.v_bola = V_bola
        self.vx_bola = int(self.v_bola*random.randint(6,8)/10)
        self.vy_bola = V_bola - self.vx_bola
        self.v_barra = V_barra
        self.fonte = pygame.font.SysFont('arial',30,bold=True,italic=True)#fonte de texto
        self.fonteG = pygame.font.SysFont('arial',50,bold=True,italic=True)#fonte de texto
        self.larg_barra = 20
        self.alt_barra = 70
        self.b_radius = 10
        self.colide1 = time.time()
        self.bot = Bot
        self.bot_down = False
        self.bot_up = False

    def mov_bola(self):
        if self.yb-10>self.altura_sup and self.yb+10<self.altura_inf:
            self.xb += self.vx_bola
            self.yb += self.vy_bola
        else:
            self.vy_bola = (-1)*self.vy_bola
            self.xb += self.vx_bola
            self.yb += self.vy_bola

    def reset(self):
        self.y1 = self.y_init
        self.y2 = self.y_init
        self.x1 = 30
        self.x2 = 950
        self.xb = 500
        self.yb = 320
        self.B0 = 0
        self.vx_bola = int(self.v_bola*random.randint(6,8)/10)
        self.vy_bola = self.v_bola - self.vx_bola
        self.v_barra = self.v_barra
        self.bot_down = False
        self.bot_up = False

    def formas(self):
        self.limite_cima = pygame.draw.line(self.scr,(255,255,255),(0,self.altura_sup-5),(self.largura,self.altura_sup-5))
        self.limite_baixo = pygame.draw.line(self.scr,(255,255,255),(0,self.altura_inf+5),(self.largura,self.altura_inf+5))
        self.limite_centro = pygame.draw.line(self.scr,(255,255,255),(self.largura/2,self.altura_sup-5),(self.largura/2,self.altura_inf+5))
        self.barra1 = pygame.draw.rect(self.scr,(0,255,0),(self.x1,self.y1,self.larg_barra,self.alt_barra))
        self.barra2 = pygame.draw.rect(self.scr,(255,0,0),(self.x2,self.y2,self.larg_barra,self.alt_barra))
        self.bola = pygame.draw.circle(self.scr,(255,255,255),(self.xb,self.yb),self.b_radius)

        self.mensagem1 = f'Jogador 1: {self.j1}'
        self.mensagem2 = f'Jogador 2: {self.j2}'
        self.texto1 = self.fonte.render(self.mensagem1, True, (255,255,255))
        self.texto2 = self.fonte.render(self.mensagem2, True, (255,255,255))
        self.scr.blit(self.texto1, ((self.largura/2)-80, 10))
        self.scr.blit(self.texto2, ((self.largura/2)-80, 40))
    
    def bot_move(self):
        if self.bot:
            self.bot_down = False
            self.bot_up = False
            _y = (self.vy_bola*(self.x2-self.xb+10))/self.vx_bola
            _H = (self.altura_inf-self.altura_sup)
            _n = int((self.yb+_y)/_H)
            y_futuro = self.yb+_y-_n*_H
            if _n%2==1:
                y_futuro = _H - y_futuro + self.altura_sup
            if y_futuro>self.y2+15+self.alt_barra/2:
                self.bot_down = True
            elif y_futuro<self.y2-15+self.alt_barra/2:
                self.bot_up = True


    def tela(self):
        self.scr = pygame.display.set_mode((self.largura, self.altura_tela))
        pygame.display.set_caption("PONG GAME") #Nome da tela
        self.relogio = pygame.time.Clock()

        while True:
            self.relogio.tick(30) #frames per second
            self.scr.fill((10,10,10)) #clear screen
            self.mensagem1 = f'Jogador 1: {self.j1}'
            self.mensagem2 = f'Jogador 2: {self.j2}'
            self.texto1 = self.fonte.render(self.mensagem1, True, (255,255,255))
            self.texto2 = self.fonte.render(self.mensagem2, True, (255,255,255))

            #Events loop
            try:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.display.quit()
                        pygame.quit()
                        #exit()
                    if event.type == KEYDOWN:
                        if pygame.key.get_pressed()[K_r]:
                            self.reset()
                            self.j1=0
                            self.j2=0

                self.bot_move()

                if pygame.key.get_pressed()[K_w]:
                    if self.y1>self.altura_sup:
                        self.y1-=self.v_barra
                if pygame.key.get_pressed()[K_s]:
                    if self.y1+self.alt_barra<self.altura_inf:
                        self.y1+=self.v_barra
                if pygame.key.get_pressed()[K_UP] or self.bot_up:
                    if self.y2>self.altura_sup:
                        self.y2-=self.v_barra
                if pygame.key.get_pressed()[K_DOWN] or self.bot_down:
                    if self.y2+self.alt_barra<self.altura_inf:
                        self.y2+=self.v_barra

            except:
                pygame.display.quit()
                pygame.quit()
                break

            if self.B0==0:
                self.vx_bola = self.vx_bola*random.choice([-1,1])
                self.vy_bola = self.vy_bola*random.choice([-1,1])
                self.formas()
                pygame.time.delay(500)
                self.B0=1

            if self.xb+self.b_radius<0:
                self.j2+=1
                self.reset()
            elif self.xb-self.b_radius>=self.largura:
                self.j1+=1
                self.reset()
            if self.j1>=self.P_max or self.j2>=self.P_max:
                if self.j1>self.j2:
                    Vencedor='Jogador 1 venceu!'
                    mensagemVence = f'{Vencedor}'
                    textoV = self.fonteG.render(mensagemVence, True, (0,255,0))
                if self.j2>self.j1:
                    Vencedor='Jogador 2 venceu!'
                    mensagemVence = f'{Vencedor}'
                    textoV = self.fonteG.render(mensagemVence, True, (255,0,0))
                self.scr.blit(textoV, (300, 500))
                self.reset()
                pygame.display.flip() 
                pygame.time.delay(2000)
                self.j1 = 0
                self.j2 = 0

            self.formas()

            if self.bola.colliderect(self.barra1) or self.bola.colliderect(self.barra2):
                self.colide2 = time.time()
                if self.colide2 - self.colide1 > 0.5:
                    if self.vx_bola<20:
                        self.vx_bola = self.vx_bola*(-1.05)
                    _t = 0
                elif _t==0:
                    self.vy_bola = (-1.7)*self.vy_bola
                    self.vx_bola = self.vx_bola*(0.8)
                        
                    _t = 1
                self.colide1 = self.colide2

            self.mov_bola()

            self.scr.blit(self.texto1, ((self.largura/2)-80, 10))
            self.scr.blit(self.texto2, ((self.largura/2)-80, 40))

            pygame.display.flip()


#jogo = Pong(3,10,10)
#jogo.tela()