from trollClass import troll
import pygame
from PIL import *
from guerisseurHeros import guerisseur
from guerrierHeros import guerrier
from mageHeros import mage
from chasseurHeros import chasseur
from dragonClass import dragon

pygame.init()


ecran = pygame.display.set_mode()

x, y = ecran.get_size()

#test avec cinq trolls et les attaquants
trollUn = troll(x,y,70,75)
trollDeux = troll(x,y,70,57)
trollTrois = troll(x,y,70,39)
trollQuatre = troll(x,y,70,21)
trollCinq = troll(x,y,70,3)

dragonneau = dragon(x,y,70,39)

monGuerisseur = guerisseur(x,y,20,3)
monMage = mage(x,y,20,70)
monChasseur = chasseur(x,y,20,52)
monGuerrier = guerrier(x,y,20,35)

combattants = []

combattants.append(monGuerisseur)
combattants.append(monGuerrier)
combattants.append(monMage)
combattants.append(monChasseur)

vagueTroll = []

vagueTroll.append(dragonneau)
'''
vagueTroll.append(trollUn)
vagueTroll.append(trollDeux)
vagueTroll.append(trollTrois)
vagueTroll.append(trollQuatre)
vagueTroll.append(trollCinq)
'''
#fin des variables

background = pygame.image.load("animation/images/BG.jpg")
background = pygame.transform.scale(background, (x,y))

continuer = True

while continuer:
    
    ecran.blit(background, (0,0))
    for i in vagueTroll:
        ecran.blit(i.resize,i.rect)
    for j in combattants:
        ecran.blit(j.resize,j.rect)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
            pygame.quit()

pygame.quit()