import pygame
from pygame.locals import *
import PySimpleGUI as sg
import random

class Screens():
    def __init__(self):
        layout = [
            [sg.Text('Pontuação final: ')],
            [sg.Slider(range=(3,10),default_value=2,orientation='h', size=(23,20), key='Max_round')],
            [sg.Text('Velocidade da bola: ')],
            [sg.Slider(range=(1,4),default_value=8,orientation='h', size=(23,20), key='Vel_bola')],
            [sg.Text('Velocidade da barra: ')],
            [sg.Slider(range=(1,4),default_value=8,orientation='h', size=(23,20), key='Vel_barra')],
            [sg.Button('INICIAR')]
        ]
        #Janela
        self.janela = sg.Window('Gerador de senha').layout(layout)
    def Iniciar(self):   
        global P_max,v_bola,v_barra       
        self.button, self.values = self.janela.read()
        
        if self.values!=None:
            P_max = self.values['Max_round']
            v_bola = self.values['Vel_bola']
            v_barra = self.values['Vel_barra']

tela = Screens()
tela.Iniciar()
Jogo = pong()