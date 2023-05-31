from random import *

import pygame

class troll(pygame.sprite.Sprite):
    def __init__(self,abscisse,ordonnee,placementAbscisse,placementOrdonnee,pseudo):
        super().__init__()
        self.PV = 5
        self.maxPV = self.PV
        self.dommage = 4
        self.attaqueChasseur = 2
        self.pseudo = pseudo
        self.type="ennemi"
        self.image = pygame.image.load("animation/images/trollv2-removebg-preview.png")
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.auto = (abscisse*10/100)/self.width
        self.resize = pygame.transform.scale(self.image,(abscisse*10/100, self.height*self.auto))
        self.rect = self.image.get_rect()
        self.rect.x = abscisse*placementAbscisse/100
        self.rect.y = ordonnee*placementOrdonnee/100
        
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
    
