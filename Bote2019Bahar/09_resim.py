import math
import pygame

width, height = 640, 480
saat = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((width, height))

devam = True
img0 = pygame.image.load("./images/pengu1.png")
img0.convert()
rect = img0.get_rect()
merkez = width // 2, height // 2
pygame.draw.rect(img0, pygame.color.Color("tomato"), rect, 2)
rect.center = merkez
aci = 0
img = img0
olcek = 1
while devam:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            devam = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if event.mod & pygame.KMOD_SHIFT:
                    aci += 10
                else:
                    aci -= 10
                img = pygame.transform.rotozoom(img0, aci, olcek)
            elif event.key == pygame.K_o:
                if event.mod & pygame.KMOD_SHIFT:
                    olcek /= 1.1
                else:
                    olcek *= 1.1
                img = pygame.transform.rotozoom(img0, aci, olcek)
            elif event.key == pygame.K_b:
                img = img0
                olcek = 1
                aci = 0
            elif event.key == pygame.K_q:
                img = pygame.transform.flip(img, True, False)
            elif event.key == pygame.K_w:
                img = pygame.transform.flip(img, False, True)
            elif event.key == pygame.K_2:
                img = pygame.transform.scale2x(img)
            elif event.key == pygame.K_1:
                img = pygame.transform.laplacian(img)

            rect = img.get_rect()
            rect.center = merkez

        elif event.type == pygame.MOUSEMOTION:
            imlec = event.pos
            x = imlec[0] - merkez[0]
            y = imlec[1] - merkez[1]
            uzaklik = math.sqrt(x**2 + y**2)

            aci = math.degrees(-math.atan2(y,x))
            olcek = abs(6*uzaklik / width)
            img = pygame.transform.rotozoom(img0, aci, olcek)
            rect = img.get_rect()
            rect.center = merkez

    screen.fill(pygame.color.Color("azure3"))
    screen.blit(img, rect)

    pygame.display.update()
    saat.tick(60)

pygame.quit()
