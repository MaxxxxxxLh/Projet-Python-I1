import pygame

pygame.init()

ecran = pygame.display.set_mode((600, 600))
image = pygame.image.load("troll.jpg").convert_alpha()

continuer = True

while continuer:
    ecran.blit(image, (0, 50))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
    pygame.display.flip()

pygame.quit()