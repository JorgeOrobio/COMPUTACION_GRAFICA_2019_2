import pygame
from libreria import *
import random

class Jugador(pygame.sprite.Sprite):
    """jugadores"""

    def __init__(self,pto):
        pygame.sprite.Sprite.__init__(self)
        self.col=3
        self.image=pygame.Surface([40,60])
        self.image.fill(blanco)
        self.rect=self.image.get_rect()
        self.rect.x=pto[0]
        self.rect.y=pto[1]
        self.velx=5
        self.vely=0
        self.q=0
        self.col=0

    def update(self):

        self.rect.x+=self.velx
        self.rect.y+=self.velx
        if self.q == 0 and self.col == 1:
            self.q=1
            self.col=1
        if self.q==0 and self.col == 0:
            self.q=0
            self.col=0
            self.velx=5
            self.vely=0
        if self.q == 1 and self.col == 1:
            self.velx=0
            selfvely=5
            self.q=0
            self.col=0

class Bloque(pygame.sprite.Sprite):
    def __init__(self,pto):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([40,60])
        self.image.fill(blanco)
        self.rect=self.image.get_rect()
        self.rect.x=pto[0]
        self.rect.y=pto[1]
        self.velx=0
        self.desp=20


class Mina(pygame.sprite.Sprite):
    def __init__(self,pto):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([30,30])
        self.image.fill(azul)
        self.rect=self.image.get_rect()
        self.rect.x=pto[0]
        self.rect.y=pto[1]
        self.velx=5
        self.desp=0
        self.radius = 100

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.desp



class Ventaja (pygame.sprite.Sprite):
    def __init__(self,pto,cl=azul):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([30,30])
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x=pto[0]
        self.rect.y=pto[1]
        self.velx=5
        self.desp=0


def Enlimite(self,valor):
    cumple=False
    liminf=self.rect.bottom - self.desp
    limsup=self.rect.bottom + self.desp
    if (liminf < valor) and (valor < limsup):
        cumple=True

    return cumple

if __name__ == '__main__':

    pygame.init()
    pantalla=pygame.display.set_mode([600,400])
    jugadores=pygame.sprite.Group()
    bloques=pygame.sprite.Group()
    minas=pygame.sprite.Group()
    ventajas=pygame.sprite.Group()
    j=Jugador([100,100])
    jugadores.add(j)


    b=Bloque([250,140])
    bloques.add(b)

    m=Mina([340,170])
    minas.add(m)

    # v=Ventaja([500,300])
    # ventajas.add(v)

    moneda =0
    posible=90

    #pantalla.blit(m[0][0],[10,10])
    pygame.display.flip()
    fin=False
    reloj=pygame.time.Clock()



    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                j.velx=5
                j.final(event.pos)

        colision = pygame.sprite.spritecollide(j,bloques,False)
        for e in colision:
            j.col = 1

        for m in minas:
            if pygame.sprite.collide_circle(m,j):
                m.image.fill(verde)
                moneda=random.randrange(100)

        if moneda > posible:
            v=Ventaja([0,0])
            ventajas.add(v)

        pantalla.fill(negro)

        #pantalla.blit(m[cont][0],[10,10])
        jugadores.draw(pantalla)
        jugadores.update()
        bloques.draw(pantalla)
        minas.draw(pantalla)
        ventajas.draw(pantalla)
        pygame.display.flip()
        reloj.tick(30)
