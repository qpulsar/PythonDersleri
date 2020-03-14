import pygame

width, height = 640, 480
saat = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((width, height))

devam = True
font = pygame.font.SysFont(None, 48)
font1 = pygame.font.SysFont('comicsansms', 72)
fontlar = pygame.font.get_fonts()
print(fontlar)
img1 = font.render("Deneme", True, pygame.color.Color("yellow"))
img2 = font1.render("cambriacambriamath", True, pygame.color.Color("red"))
while devam:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            devam = False

    screen.blit(img1, (50,30))
    screen.blit(img2, (100,130))
    pygame.display.update()
    saat.tick(60)

pygame.quit()
