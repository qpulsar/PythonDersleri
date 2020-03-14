import pygame

pygame.init()
ekran = pygame.display.set_mode((300, 300))

bitti = False
r = (255, 0, 0)
b = (0, 0, 255)
renk = True
c = r
x = 50
y = 50
saat = pygame.time.Clock()

while not bitti:
    ekran.fill((0, 0, 0))
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            bitti = True
        if olay.type == pygame.KEYDOWN and olay.key == pygame.K_SPACE:
            renk = not renk
    tus = pygame.key.get_pressed()
    if tus[pygame.K_LEFT]:
        x -= 5
    if tus[pygame.K_RIGHT]:
        x += 5
    if tus[pygame.K_UP]:
        y += -5
    if tus[pygame.K_DOWN]:
        y += 5
    if renk:
        c = r
    else:
        c = b
    pygame.draw.rect(ekran, c, pygame.Rect(x, y, 75, 75))
    pygame.display.flip()
    saat.tick(60)
