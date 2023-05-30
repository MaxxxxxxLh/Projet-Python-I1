from random import *
import pygame
class dragon():
    def __init__(self,abscisse,ordonnee,placementAbscisse,placementOrdonnee,pseudo):
        self.PV = 15
        self.maxPV = self.PV
        self.dommage = randint(0,6)
        self.AOE = randint(0,2)
        self.pseudo = pseudo
        self.type = "dragon"
        self.image = pygame.image.load("animation/images/dragon-removebg-preview.png")
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.auto = (abscisse*30/100)/self.width
        self.resize = pygame.transform.scale(self.image,(abscisse*30/100, self.height*self.auto))
        self.rect = self.image.get_rect()
        self.rect.x = abscisse*placementAbscisse/100
        self.rect.y = ordonnee*placementOrdonnee/100
    def attaque(self, ennemis, attaquant):
        for i in ennemis:
            if i == attaquant:
                attaquant.PV -= randint(0,self.dommage)
            else:
                i.PV -= randint(0,self.AOE)
    def estEnVie(self):
        if self.PV>0:
            return True
        else:
            return False
    def barreHP(self,background):
        barreCouleur = (71,209,71)
        barreCouleurFond = (230,0,0)
        positionBarre = [self.rect.x, self.rect.y, (self.PV/self.maxPV)*self.rect.width, self.rect.height*5/100]
        positionBarreFond = [self.rect.x, self.rect.y, self.rect.width, self.rect.height*5/100]
        pygame.draw.rect(background,barreCouleurFond,positionBarreFond)
        pygame.draw.rect(background,barreCouleur,positionBarre)