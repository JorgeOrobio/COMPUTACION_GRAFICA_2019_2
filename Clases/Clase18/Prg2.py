import pygame as pg
from libreria import*
import random
import configparser as cp

class Cuadro(pg.sprite.Sprite):
    """clase cuadro"""
    def __init__(self,pos):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.Surface([40,40])
        self.image.fill(verde)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.click=False
        self.velx=0
    def update(self):
        self.rect.x += self.velx
        if self.click:
            self.rect.center = pg.mouse.get_pos()

class Region(pg.sprite.Sprite):
    """clase Region"""
    def __init__(self,pos):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.Surface([100,100])
        self.image.fill(blanco)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.click=False
    # def update(self):
    #     if self.click:
    #         self.rect.center = pg.mouse.get_pos()

if __name__ == '__main__':

    # PANTALLA
    pg.init()
    pantalla = pg.display.set_mode([ancho,alto])
    reloj= pg.time.Clock()
    # CREACION DE GRUPOOS
    jugadores = pg.sprite.Group()
    objetos=pg.sprite.Group()
    regiones = pg.sprite.Group()
    # CUADRO
    r=Region([100,100])
    regiones.add(r)
    pg.display.flip()
    fin = False
    while not fin:
        event=pg.event.get()
        for e in event:
            if e.type == pg.QUIT:
                fin = True
            if e.type == pg.MOUSEBUTTONDOWN:
                if r.rect.collidepoint(e.pos):
                    for r in regiones:
                        if r.rect.collidepoint(e.pos):
                            c=Cuadro(e.pos)
                            c.click=True
                            objetos.add(c)
                    # obj.click = True
            if e.type == pg.MOUSEBUTTONUP:
                for o in objetos:
                    if o.click:
                        o.click=False
                        o.velx=10
                    # obj.click=False
                    pass
        objetos.update()
        pantalla.fill(negro)
        objetos.draw(pantalla)
        regiones.draw(pantalla)
        pg.display.flip()
        reloj.tick(35)
