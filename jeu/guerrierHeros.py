from random import *
import pygame
class guerrier():
    def __init__(self,abscisse,ordonnee,placementAbscisse,placementOrdonnee):
        self.PV = 10
        self.dommage = 5
        self.pseudo = "guerrier"
        self.type = "guerrier"
        self.image = pygame.image.load("animation/images/guerrier-removebg-preview.png")
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.auto = (abscisse*10/100)/self.width
        self.resize = pygame.transform.scale(self.image,(abscisse*10/100, self.height*self.auto))
        self.rect = self.image.get_rect()
        self.rect.x = abscisse*placementAbscisse/100
        self.rect.y = ordonnee*placementOrdonnee/100
    def attaque(self,ennemi):
        ennemi.PV -= randint(0,self.dommage)
    def estEnVie(self):
        if self.PV>0:
            return True
        else:
            return False
