import pygame
from pygame.locals import *

class Metin:
    def __init__(self,yaz, poz):
        self.text = yaz
        self.pos = poz
        self.fontname = None
        self.fontsize = 72
        self.fontcolor = Color("brown")
        self.set_font()
        self.render()

    def set_font(self):
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def ciz(self):
        Uygulama.screen.blit(self.img, self.rect)

class Uygulama:
    def __init__(self):
        pygame.init()
        flags = RESIZABLE
        Uygulama.screen = pygame.display.set_mode((640,480), flags)
        Uygulama.yazi = Metin('En buyuk BOTE', poz=(50,50))
        Uygulama.devam = True

    def run(self):
        while Uygulama.devam:
            for event in pygame.event.get():
                if event.type == QUIT:
                    Uygulama.devam = False

            Uygulama.screen.fill(color.Color("bisque1"))
            Uygulama.yazi.ciz()
            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':
    Uygulama().run()
