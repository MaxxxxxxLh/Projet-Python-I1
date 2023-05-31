from random import *
import pygame
class guerisseur():
    def __init__(self, abscisse, ordonnee,placementAbscisse,placementOrdonnee):
        self.level = 0
        self.PV = 10 + 5*self.level
        self.maxPV = self.PV
        self.dommage = 1 + 1*self.level
        self.heal = 2 + 1 *self.level
        self.pseudo = "guerrisseur"
        self.type = "guerrisseur"
        self.image = pygame.image.load("animation/images/guerisseuse-removebg-preview.png")
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.auto = (abscisse*10/100)/self.width
        self.resize = pygame.transform.scale(self.image,(abscisse*10/100, self.height*self.auto))
        self.rect = self.image.get_rect()
        self.rect.x = abscisse*placementAbscisse/100
        self.rect.y = ordonnee*placementOrdonnee/100
    def attaque(self,ennemi):
        ennemi.PV -= randint(0,self.dommage)
    def soin(self,allie):
        allie.PV += self.heal
        if allie.PV> allie.maxPV:
            allie.PV = allie.maxPV
    def estEnVie(self):
        if self.PV>0:
            return True
        else:
            return False
