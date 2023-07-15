import pygame
from threading import Thread
from time import sleep

class Kumanda:
    
    def __init__(self):
        
        pygame.init()

        pygame.joystick.init()

        self.k = pygame.joystick.Joystick(0)
        self.k.init
        
        self.solX = 0
        self.sağX = 0 
        self.solY = 0
        self.sağY = 0
        self.butons = []

    def dinlemeyeBasla(self):

        Thread(target=self.__dinle__, args=()).start()
        return self

    def __dinle__(self):

        while True:
            for event in pygame.event.get():
                if event == pygame.JOYBUTTONDOWN and event.button not in self.butons:
                    self.butons.append(event.button)
                if event == pygame.JOYBUTTONUP and event.button in self.butons:
                    self.butons.remove(event.button)
                if (event.type == pygame.JOYAXISMOTION):
                    if (event.axis == 0):
                        self.solX = event.value
                    elif (event.axis == 1):
                        self.solY = event.value
                    elif (event.axis == 2):
                        self.sagX = event.value
                    elif (event.axis == 3):
                        self.sagY = event.value

    def sol(self):
        return self.solX, self.solY
    def sağ(self):
        return self.sağX, self.sağY
    def butonlar(self):
        return self.butons
    def oku(self):
        return self.sol, self.sağ, self.butonlar








