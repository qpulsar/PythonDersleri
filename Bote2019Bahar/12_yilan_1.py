import pygame
import random

w = 500
h = 500
satir = 20
# sutun = 20
beyaz = (255, 255, 255)
yesil = (0, 255, 0)
kirmizi = (255, 0, 0)

devam = True


class elma(object):
    global screen, w, h, satir
    gen = w // satir

    def __init__(self):
        self.at()

    def at(self):
        self.x = random.randrange(0, satir)
        self.y = random.randrange(0, satir)
        # todo: çalışma kontrolü yapılacak
        self.pos = [self.x, self.y]

    def ciz(self):
        pygame.draw.circle(screen, kirmizi, (self.x * self.gen + self.gen // 2,
                                             self.y * self.gen + self.gen // 2),
                                             10)


class kup(object):
    global screen, w, h, satir

    def __init__(self, pos, yonx=1, yony=0, renk=yesil, kafa=False):
        self.pos = list(pos)
        self.yonx = yonx
        self.yony = yony
        self.renk = renk
        self.kafa = kafa

    def ciz(self):
        gen = w // satir
        x, y = self.pos
        pygame.draw.rect(screen, self.renk, (x * gen + 1, y * gen + 1, gen - 1, gen - 1))
        if self.kafa == True:
            merkez = gen // 2
            r = 3
            m1 = (x * gen + merkez - r, y * gen + 10)
            m2 = (x * gen + merkez + r, y * gen + 10)
            pygame.draw.circle(screen, beyaz, m1, r)
            pygame.draw.circle(screen, beyaz, m2, r)


class yilan(object):
    govde = []

    def __init__(self, position):
        self.position = list(position)
        self.yonx = 0
        self.yony = 1
        self.govde.append(kup(position, kafa=True))
        self.govde.append(kup((position[0], position[1] - 1)))
        self.govde.append(kup((position[0], position[1] - 2)))

    def move(self, tus):
        if tus == pygame.K_RIGHT:
            self.yonx = 1
            self.yony = 0
        elif tus == pygame.K_LEFT:
            self.yonx = -1
            self.yony = 0
        elif tus == pygame.K_UP:
            self.yonx = 0
            self.yony = -1
        elif tus == pygame.K_DOWN:
            self.yonx = 0
            self.yony = 1

        for k in range(len(self.govde) - 1, 0, -1):
            self.govde[k].pos[0] = self.govde[k - 1].pos[0]
            self.govde[k].pos[1] = self.govde[k - 1].pos[1]

        self.govde[0].pos[0] += self.yonx
        self.govde[0].pos[1] += self.yony

        for k in self.govde:
            k.ciz()

    def uza(self):
        kuyruk = kup(self.govde[1].pos)
        self.govde.append(kuyruk)


def grid():
    global screen, w, h, satir, FONTS
    genislik = w // satir
    x, y = 0, 0
    for i in range(satir):
        x += genislik
        y += genislik
        pygame.draw.line(screen, beyaz, (0, y), (w, y))
        pygame.draw.line(screen, beyaz, (x, 0), (x, h))

    x = 1
    for i in range(satir):
        r = FONTS["SMALL"].render(str(i), True, beyaz)
        screen.blit(r, (x, 1, 10, 10))
        screen.blit(r, (1, x, 10, 10))
        x += genislik

def yem_kontrol(yilan, yem):
    if yilan.govde[0].pos == yem.pos:
        yem.at()
        yilan.uza()

def main():
    global devam, screen, FONTS

    pygame.init()
    FONTS = {"BIG": pygame.font.SysFont("helvetica", 100, True),
             "SMALL": pygame.font.SysFont("helvetica", 10, True)}
    screen = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()

    kobra = yilan([10, 10])
    yem = elma()
    while devam:
        screen.fill((0, 0, 0))
        grid()
        tus = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                devam = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    devam = False
                else:
                    tus = event.key
        yem_kontrol(kobra, yem)
        kobra.move(tus)
        yem.ciz()
        pygame.display.update()
        clock.tick(5)

    pygame.quit()


if __name__ == '__main__':
    main()
