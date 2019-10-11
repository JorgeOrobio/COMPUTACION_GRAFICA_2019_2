
# IMPLEMENTA COLISIONES 
# IMPLEMENTA UN CONTADOR DE SALUD
# IMPLEMENTA LA DETECCION PERO NO LA ELIMINACION DE LOS RIVALES

import pygame as pg
from libreria import*
import random

class Jugador(pg.sprite.Sprite):
    """clase jugador"""
    def __init__(self,pos):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([80,80])
        self.image.fill(verde)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
        pass

class Rival(pg.sprite.Sprite):
    """clase rival"""
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([80,80])
        self.image.fill(rojo)
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=0
        self.velx=0
        self.vely=0


if __name__ == '__main__':
    pg.init
    pantalla = pg.display.set_mode([ancho,alto])
    jugadores=pg.sprite.Group()
    rivales=pg.sprite.Group()
    j=Jugador([100,200])
    jugadores.add(j)
    n=10
    for i in range(n):
        r = Rival()
        r.rect.x=random.randrange(ancho-r.rect.width)
        r.rect.y=random.randrange(alto- r.rect.height)
        rivales.add(r)
    salud=1000
    reloj=pg.time.Clock()
    fin = False
    # CICLO PRINCIPAL
    while not fin:
        for event in pg.event.get():
            #EVENTOS
            if event.type ==pg.QUIT:
                fin = True
            #MOVIMIENTO DIRECCIONADO
            if event.type==pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    j.velx=5
                    j.vely=0
                if event.key == pg.K_LEFT:
                    j.velx=-5
                    j.vely=0
                if event.key == pg.K_DOWN:
                    j.vely=5
                    j.velx=0
                if event.key == pg.K_UP:
                    j.vely=-5
                    j.velx=0
                if event.key == pg.K_SPACE:
                    j.vely=0
                    j.velx=0
            if event.type==pg.KEYUP:
                j.velx=0
                j.vely=0
        # CONTROL DEL SISTEMA
        # LIMITES DE PANTALLA
        if j.rect.x > (ancho - j.rect.width):
            j.rect.x = ancho - j.rect.width
            j.velx=0
        if j.rect.x < 0:
            j.rect.x=0
            j.velx=0
        # COLISIONES
        ls = pg.sprite.spritecollide(j,rivales,False)
        for r in ls:
            salud-=1
            print(salud)
            if salud==0:
                fin=True
        # REFRESCO DE PANTALLA
        jugadores.update()
        pantalla.fill(negro)
        jugadores.draw(pantalla)
        rivales.draw(pantalla)
        pg.display.flip()
        reloj.tick(60)
