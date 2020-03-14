import pygame

width, height= 640,480
fps= pygame.time.Clock()

pygame.init()
screen=pygame.display.set_mode((width,height))

basla=[0,0]
boyut=[0,0]
ciziyor=False
devam =True

tamliste=[]
while devam:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            devam=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            basla= event.pos
            boyut=(0,0)
            ciziyor=True
        elif event.type==pygame.MOUSEMOTION:
            if ciziyor:
                son=event.pos
                boyut=(son[0]- basla[0],son[1] - basla[1])

        elif event.type== pygame.MOUSEBUTTONUP:

            son=event.pos
            boyut=(son[0] - basla[0], son[1] -basla[1])
            ciziyor= False
            tamliste.append(pygame.Rect(basla, boyut))



    screen.fill((20,22,25))
    pygame.draw.rect(screen,(255,255,0),(basla,boyut),2)
    for d  in tamliste:
        pygame.draw.rect(screen,(200,25,160),d,2)
    pygame.display.update()
    fps.tick(60)

pygame.quit()