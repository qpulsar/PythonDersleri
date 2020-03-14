import pygame

width, height = 640, 480
saat = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((width, height))

devam = True
hareket = False
img = pygame.image.load('./images/pengu1.png')
img.convert()
rect = img.get_rect()
print(rect)
while devam:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            devam = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                hareket = True
        elif event.type == pygame.MOUSEBUTTONUP:
            hareket = False
        elif event.type == pygame.MOUSEMOTION:
            if hareket:
                rect.move_ip(event.rel)


    screen.fill(pygame.color.Color("azure3"))
    screen.blit(img, rect)
    pygame.draw.rect(screen, pygame.color.Color("red"), rect, 1)
    pygame.display.update()
    saat.tick(60)

pygame.quit()
