from random import *
import pygame
class chasseur():
    def __init__(self,abscisse,ordonnee,placementAbscisse,placementOrdonnee):
        self.level = 0
        self.PV = 10 + 5*self.level
        self.maxPV = self.PV
        self.dommage = 3 + 1*self.level
        self.fleche = 5
        self.pseudo = "chasseur"
        self.type = "chasseur"
        self.image = pygame.image.load("animation/images/chasseur-removebg-preview.png")
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.auto = (abscisse*10/100)/self.width
        self.resize = pygame.transform.scale(self.image,(abscisse*10/100, self.height*self.auto))
        self.rect = self.image.get_rect()
        self.rect.x = abscisse*placementAbscisse/100
        self.rect.y = ordonnee*placementOrdonnee/100
    def attaque(self,ennemi):
        if self.fleche > 0:
            ennemi.PV -= randint(0,self.dommage)
            self.fleche -= 1
        else:
            ennemi.PV -= randint(0,1)
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
