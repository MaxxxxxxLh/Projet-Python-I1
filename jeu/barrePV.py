import pygame
def barreHP(a,background,x,y):
    barreCouleur = (71,209,71)
    barreCouleurFond = (230,0,0)
        
    positionBarre = [a.rect.x, a.rect.y, (a.PV/a.maxPV)*x*10/100,y*1/100 ]
    positionBarreFond = [a.rect.x, a.rect.y, x*10/100, y*1/100]
    pygame.draw.rect(background,barreCouleurFond,positionBarreFond)
    pygame.draw.rect(background,barreCouleur,positionBarre)