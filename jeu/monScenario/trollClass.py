from random import *
import pygame
import sys

class troll(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.PV = 5
        self.dommage = 4
        self.attaqueChasseur = 2
        self.pseudo = "troll"
        self.image = pygame.image.load("animation/images/troll.jpg")
        self.rect = self.image.get_rect()
    def attaque(self,ennemi):
        if ennemi.type == "chasseur":
            ennemi.PV -= randint(0,self.attaqueChasseur)
        else:
            ennemi.PV -= randint(0,self.dommage)
    def estEnVie(self):
        if self.PV>0:
            return True
        else:
            return False