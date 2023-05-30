from trollClass import troll
import pygame
from PIL import *
from guerisseurHeros import guerisseur
from guerrierHeros import guerrier
from mageHeros import mage
from chasseurHeros import chasseur
from dragonClass import dragon
from combat import *
from tourJoueur import *
pygame.init()


ecran = pygame.display.set_mode()

x, y = ecran.get_size()





background = pygame.image.load("animation/images/BG.jpg")
background = pygame.transform.scale(background, (x,y))

continuer = True
numeroDeVagues = 1

compteur = 0

def game(numeroDeVagues):
    while numeroDeVagues !=5:
        #initialisation des heros
        monChasseur = chasseur(x,y,20,52)
        monGuerrier = guerrier(x,y,20,35)
        monGuerisseur = guerisseur(x,y,20,3)
        monMage = mage(x,y,20,70)
        combattants = {"chasseur": monChasseur, "guerrier": monGuerrier, "guerisseur": monGuerisseur, "mage" : monMage} #mettre les différents heros dans un dictionnaire
        listeCombattants = list(combattants.values()) #créer une liste avec les combattants en vie
        vaguesEnnemi = vagues(numeroDeVagues,x,y)
        combat(vaguesEnnemi,compteur, continuer, listeCombattants)
        if listeCombattants == []:
            break
        else:
            numeroDeVagues += 1
            for i in listeCombattants:
                i.level += 1
        

    
def combat(vaguesEnnemi,compteur, continuer, listeCombattants):
    while continuer:
        
        ecran.blit(background, (0,0))
        for i in vaguesEnnemi:
            ecran.blit(i.resize,i.rect)
        for j in listeCombattants:
            ecran.blit(j.resize,j.rect)
            
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                try:
                    clicked_sprites = [s for s in vaguesEnnemi if s.rect.collidepoint(pos)]
                    for i in vaguesEnnemi:
                        if clicked_sprites[0].pseudo == i.pseudo:  
                            tourHeros(choixPersonnage(compteur,listeCombattants),listeCombattants, vaguesEnnemi,i)
                    if vaguesEnnemi == [] or listeCombattants == []:
                        continuer = False
                except:
                    pass
                
game(numeroDeVagues)

        
pygame.quit()