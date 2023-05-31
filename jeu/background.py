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


def game():
    numeroDeVagues = 1
    while numeroDeVagues !=5:
        pygame.init()


        ecran = pygame.display.set_mode()

        x, y = ecran.get_size()





        background = pygame.image.load("animation/images/BG.jpg")
        background = pygame.transform.scale(background, (x,y))

        continuer = True
        
        
        
        compteur = 0
        #initialisation des heros
        monChasseur = chasseur(x,y,20,52)
        monGuerrier = guerrier(x,y,20,35)
        monGuerisseur = guerisseur(x,y,20,3)
        monMage = mage(x,y,20,70)
        combattants = {"chasseur": monChasseur, "guerrier": monGuerrier, "guerisseur": monGuerisseur, "mage" : monMage} #mettre les différents heros dans un dictionnaire
        listeCombattants = list(combattants.values()) #créer une liste avec les combattants en vie
        vaguesEnnemi = vagues(numeroDeVagues,x,y)
        listePersos = []
        for i in listeCombattants:
            listePersos.append(i)
        for j in vaguesEnnemi:
            listePersos.append(j)
        combat(vaguesEnnemi,compteur, continuer, listeCombattants,ecran,background, listePersos,numeroDeVagues,x,y)
        if listeCombattants == []:
            break
        else:
            numeroDeVagues += 1
            for i in listeCombattants:
                i.level += 1
    pygame.quit()
        

   

    
def combat(vaguesEnnemi,compteur, continuer, listeCombattants, ecran, background,listePersos,numeroDeVagues,x,y):
    gueri = False
    while continuer:
        
        ecran.blit(background, (0,0))
        
        font = pygame.font.Font(None,int(x*0.07))
        text = font.render("Vague n°"+str(numeroDeVagues),True,(255,255,255))
        textWidth = text.get_width()
        textHeight = text.get_height()
        text_x = (x-textWidth)//2
        text_y = (y-textHeight*8)//2
        ecran.blit(text,(text_x,text_y))
        
        if gueri == False and choixPersonnage(compteur, listeCombattants).type == "guerrisseur":
            action = "Soigner un allié"
        else:
            action = "Attaquer un ennemi"
        fontBis = pygame.font.Font(None,int(x*0.03))
        afficherAction = fontBis.render(action,True,(255,255,255))
        afficherActionWidth = afficherAction.get_width()
        afficherActionHeight = afficherAction.get_height()
        afficherAction_x = (x-afficherActionWidth)//2
        afficherAction_y = (y-afficherActionHeight)//2
        ecran.blit(afficherAction,(afficherAction_x,afficherAction_y))
        
        
        for i in vaguesEnnemi:
            ecran.blit(i.resize,i.rect)
            i.barreHP(background)
        for j in listeCombattants:
            ecran.blit(j.resize,j.rect)
            j.barreHP(background)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                try:
                    clicked_sprites = [s for s in listePersos if s.rect.collidepoint(pos)]
                    a = choixPersonnage(compteur,listeCombattants)
                    
                    if a.type == "guerrisseur":
                        if gueri == True:
                            for i in vaguesEnnemi:
                                if clicked_sprites[0].pseudo == i.pseudo:
                                    tourHeros(a,listeCombattants, vaguesEnnemi,i)
                                    compteur += 1
                                    gueri = False
                                i.barreHP(background)
                        else:
                            for hero in listeCombattants:
                                if  clicked_sprites[0].pseudo == hero.pseudo:
                                    a.soin(hero)
                                    hero.barreHP(background)
                                    gueri = True
                                    pass
                    else:
                        for i in vaguesEnnemi:
                            if clicked_sprites[0].pseudo == i.pseudo:
                                tourHeros(a,listeCombattants, vaguesEnnemi,i)
                                compteur += 1
                            i.barreHP(background)
                            
                    for i in vaguesEnnemi: 
                        if not i.estEnVie():
                            vaguesEnnemi.remove(i)
                    a.barreHP(background)
                    if vaguesEnnemi == [] or listeCombattants == []:
                        continuer = False
                except:
                    pass
                
game()

        
