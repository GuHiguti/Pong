import pygame
from pygame.locals import *
import PySimpleGUI as sg
import random
import v3_POO_Pong as game

class Screens():
    def __init__(self): 
        layout = [
            [sg.Text('Pontuação final: ')],
            [sg.Slider(range=(3,10),default_value=5,orientation='h', size=(30,20), key='Max_round')],
            [sg.Text('Velocidade da bola: ')],
            [sg.Slider(range=(1,4),default_value=2,orientation='h', size=(30,20), key='Vel_bola')],
            [sg.Text('Velocidade da barra: ')],
            [sg.Slider(range=(1,4),default_value=2,orientation='h', size=(30,20), key='Vel_barra')],
            [sg.Button('INICIAR')]
        ]
        #Janela
        self.janela = sg.Window('PONG MENU').layout(layout)
    def Iniciar(self):   
        global P_max,v_bola,v_barra       
        self.button, self.values = self.janela.read()
        try:
            if self.values!=None:
                P_max = self.values['Max_round']
                v_bola = 8 + self.values['Vel_bola']*2
                v_barra = 2 + self.values['Vel_barra']*4
                self.janela.close()
        except:
            exit()

while True:
    tela = Screens()
    tela.Iniciar()
    jogo = game.Pong(P_max,v_bola,v_barra)
    jogo.tela()
    del jogo