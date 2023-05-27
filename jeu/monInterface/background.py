from monScenario.trollClass import troll
import pygame

pygame.init()

ecran = pygame.display.set_mode((1080, 720))
image = pygame.image.load("animation/images/troll.jpg")
background = pygame.image.load("animation/images/foretJeu (1).jpg")

continuer = True

while continuer:
    
    ecran.blit(background, (0,0))
    
    ecran.blit(troll.image, troll.rect)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
            pygame.quit()

pygame.quit()