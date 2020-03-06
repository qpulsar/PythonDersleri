import pygame

width, height = 640, 480
saat = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((width, height))

devam = True

while devam:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            devam = False

    pygame.display.update()
    saat.tick(60)

pygame.quit()
