from random import *
import pygame
class mage():
    def __init__(self,abscisse,ordonnee,placementAbscisse,placementOrdonnee):
        self.level = 0
        self.PV = 10 + 5*self.level
        self.dommage = 4 + 2 * self.level
        self.AOE = 2 + 1*self.level
        self.pseudo = "mage"
        self.type = "mage"
        self.image = pygame.image.load("animation/images/mage-removebg-preview.png")
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.auto = (abscisse*10/100)/self.width
        self.resize = pygame.transform.scale(self.image,(abscisse*10/100, self.height*self.auto))
        self.rect = self.image.get_rect()
        self.rect.x = abscisse*placementAbscisse/100
        self.rect.y = ordonnee*placementOrdonnee/100
    def attaque(self,ennemis, monoCible):
        for i in ennemis:
            if i == monoCible:
                i.PV -= randint(0,self.dommage)
            else:
                i.PV -= randint(0, self.AOE)
    def estEnVie(self):
        if self.PV>0:
            return True
        else:
            return False