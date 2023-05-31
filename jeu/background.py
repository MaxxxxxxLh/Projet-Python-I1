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
import time
from barrePV import *

def game():
    numeroDeVagues = 1
    
    while numeroDeVagues !=5:
       
        changementVagues(numeroDeVagues)
        


        ecran = pygame.display.set_mode()

        x, y = ecran.get_size()





        background = pygame.image.load("animation/images/BG.jpg")
        background = pygame.transform.scale(background, (x,y))

        continuer = True
        
        
        
        compteur = 0
        #initialisation des heros
        monChasseur = chasseur(x,y,20,52)
        monGuerrier = guerrier(x,y,20,35)
        monGuerisseur = guerisseur(x,y,20,15)
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
        
    if numeroDeVagues == 5:
        if listeCombattants == []:
            ecranFin(False)
        else:
            ecranFin(True)
    pygame.quit()
        

   

    
def combat(vaguesEnnemi,compteur, continuer, listeCombattants, ecran, background,listePersos,numeroDeVagues,x,y):
    gueri = False
    while continuer:
        
        ecran.blit(background, (0,0))

        
        if gueri == False and choixPersonnage(compteur, listeCombattants).type == "guerrisseur":
            action = "Soigner un allié"
        else:
            action = choixPersonnage(compteur,listeCombattants).pseudo + " attaque un ennemi"
        fontBis = pygame.font.Font(None,int(x*0.05))
        afficherAction = fontBis.render(action,True,(255,255,255))
        afficherActionWidth = afficherAction.get_width()
        afficherActionHeight = afficherAction.get_height()
        afficherAction_x = (x-afficherActionWidth)//2
        afficherAction_y = (y-afficherActionHeight*13)//2
        ecran.blit(afficherAction,(afficherAction_x,afficherAction_y))
        
        
        for i in vaguesEnnemi:
            barreHP(i,background,x,y)
            ecran.blit(i.resize,i.rect)
            
        for j in listeCombattants:
            barreHP(j,background,x,y)
            ecran.blit(j.resize,j.rect)
            


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
                                barreHP(i,background,x,y)
                        else:
                            for hero in listeCombattants:
                                if  clicked_sprites[0].pseudo == hero.pseudo:
                                    a.soin(hero)
                                    barreHP(hero,background,x,y)
                                    gueri = True
                                    pass
                    else:
                        for i in vaguesEnnemi:
                            if clicked_sprites[0].pseudo == i.pseudo:
                                tourHeros(a,listeCombattants, vaguesEnnemi,i)
                                compteur += 1
                            barreHP(i,background,x,y)
                            
                    for i in vaguesEnnemi: 
                        if not i.estEnVie():
                            vaguesEnnemi.remove(i)

                    for j in listeCombattants:
                        if not j.estEnVie():
                            listeCombattants.remove(j)

                    barreHP(a,background,x,y)
                    if vaguesEnnemi == [] or listeCombattants == []:
                        continuer = False
                except:
                    pass
                
def ecranFin(a):
    pygame.init()
    ecran = pygame.display.set_mode()

    x, y = ecran.get_size()
    if a:
        screen = pygame.image.load("animation/images/victoire.jpg")
    else:
        screen = pygame.image.load("animation/images/defaite.jpg")
    screen = pygame.transform.scale(screen,(x,y))
    continuer = True
    while continuer:
        
        ecran.blit(screen,(0,0))
        pygame.display.flip()
        time.sleep(5)
        continuer = False
    pygame.quit()


def changementVagues(numeroVagues):
    pygame.init()
    background = ecran = pygame.display.set_mode()

    x, y = ecran.get_size()

    background = pygame.image.load("animation/images/BGnoir.jpg")
    background = pygame.transform.scale(background, (x,y))

    continuer = True
    while continuer:
        ecran.blit(background,(0,0))
        font = pygame.font.Font(None,int(x*0.07))
        text = font.render("Vague n°"+str(numeroVagues),True,(255,255,255))
        textWidth = text.get_width()
        textHeight = text.get_height()
        text_x = (x-textWidth)//2
        text_y = (y-textHeight)//2
        ecran.blit(text,(text_x,text_y))
        pygame.display.flip()
        time.sleep(2)
        continuer = False
    
        
game()