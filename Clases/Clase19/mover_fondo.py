import pygame
import random
from libreria_sprites import*

ancho = 600
alto = 400

class Apuntador(pygame.sprite.Sprite):

    def __init__(self,img,pto):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.radius=75
        self.rect =self.image.get_rect()
        self.rect.x = pto[0]
        self.rect.y = pto[1]


    def update(self):
        self.rect.center=pygame.mouse.get_pos()


class Fondo(pygame.sprite.Sprite):

    def __init__(self,img,pto):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.rect =self.image.get_rect()
        self.rect.x = pto[0]
        self.rect.y = pto[1]
        self.velx = 0
        self.vely = 0

    def update(self):
        self.rect.x+=self.velx



class Objetivo(pygame.sprite.Sprite):

    def __init__(self,img,pto):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.rect =self.image.get_rect()
        self.rect.x = pto[0]
        self.rect.y = pto[1]
        self.velx = 0
        self.vely = 0


    def update(self):
        self.rect.x=self.velx


if __name__ == '__main__':
    #incializar variables

    pygame.init()
    pantalla = pygame.display.set_mode([ancho,alto])
    reloj = pygame.time.Clock()
    lim=500
    lim2=100

    fin = False

    img=pygame.image.load("mira.png")
    img2=pygame.image.load("target.png")
    fondo=pygame.image.load("fondo.png")

    fondos=pygame.sprite.Group()
    f=Fondo(fondo,[0,-400])
    fondos.add(f)

    apuntadores = pygame.sprite.Group()
    a=Apuntador(img,[200,200])
    apuntadores.add(a)

    objetivos = pygame.sprite.Group()
    o=Objetivo(img2,[300,250])
    objetivos.add(o)
    pygame.mouse.set_visible(False)


    while (not fin):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

        if (a.rect.right > lim):
            f.velx=-5
            if (ancho - f.rect.width) > f.rect.x :
                f.velx=0
                f.rect.x=  ancho - f.rect.width

        elif (a.rect.left < lim2):
            f.velx=+5
            if f.rect.x > 0:
                f.rect.left=0

        elif (a.rect.top < lim2):
            f.velx=+5
            if f.rect.x >0:
                f.rect.x = 0

        else:
            f.velx=0

        for o in objetivos:
            o.velx=f.velx


        print(f.rect.x)

        apuntadores.update()
        fondos.update()
        objetivos.update()

        fondos.draw(pantalla)
        apuntadores.draw(pantalla)
        objetivos.draw(pantalla)
        pygame.display.flip()

        reloj.tick(60)
