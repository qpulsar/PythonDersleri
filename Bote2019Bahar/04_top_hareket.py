import pygame

width, height = 640, 480
saat = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((width, height))

devam = True

top = pygame.image.load("../images/ball_1.png")
hiz = [2, 3]
cerceve = top.get_rect()
print(cerceve)

while devam:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            devam = False

    cerceve = cerceve.move(hiz)
    if cerceve.top < 0 or cerceve.bottom > height:
        hiz[1] = -hiz[1]
    if cerceve.left < 0 or cerceve.right > width:
        hiz[0] = -hiz[0]

    screen.fill(pygame.color.Color("azure2"))
    screen.blit(top, cerceve)
    pygame.display.update()
    saat.tick(60)

pygame.quit()
