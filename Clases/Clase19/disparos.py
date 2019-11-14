import pygame as pg
from libreria import*
import random
import configparser as cp

class Torre(pg.sprite.Sprite):
    """clase torre"""
    def __init__(self,pos,cl=azul):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.Surface([40,40])
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.click=False
    def update(self):
        if self.click:
            self.rect.center = pg.mouse.get_pos()

class Fondo(pg.sprite.Sprite):
    """docstring for Fondo."""

    def __init__(self,img,pos):
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect= self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0

    def update(self):
        if (ancho - self.rect.width >= self.rect.x):
            self.rect.x = ancho - self.rect.width - self.velx
        elif alto - self.rect.height >= self.rect.y:
            self.rect.y = alto - self.rect.height  - self.vely
        elif self.rect.x >0 :
            self.rect.x=-10
        elif self.rect.y >0:
            self.rect.y=-10
        elif self.rect.y >0 and  self.rect.x >0:
            self.rect.x=-10
            self.rect.y=-10
        self.rect.x += self.velx
        self.rect.y += self.vely
        pass


class Apuntador(pg.sprite.Sprite):
    """clase Apuntador"""
    def __init__(self,imagen,pos):
        pg.sprite.Sprite.__init__(self)
        self.image=imagen
        self.radio=75
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
    def update(self):
        self.rect.center = pg.mouse.get_pos()
if __name__ == '__main__':

    # PANTALLA
    pg.init()
    pantalla = pg.display.set_mode([ancho,alto])
    reloj= pg.time.Clock()
    # CREACION DE GRUPOOS
    Miras= pg.sprite.Group()
    fondos = pg.sprite.Group()
    # MIRA
    s_img="/home/jorge/Escritorio/CGrafica/Sprites/Clases/mira.png"
    fondo="/home/jorge/Escritorio/CGrafica/Sprites/Clases/fondo.jpg"
    # FONDO
    imgfondo=pg.image.load(fondo)
    fondopos=[0,-600]
    fondo1 = Fondo(imgfondo,fondopos)
    fondos.add(fondo1)
    # MIRA
    imagen=pg.image.load(s_img)
    pos=[200,100]
    mira=Apuntador(imagen,pos)
    pg.mouse.set_visible(False)
    Miras.add(mira)
    pg.display.flip()
    fin = False
    while not fin:
        event=pg.event.get()
        for e in event:
            if e.type == pg.QUIT:
                fin = True
        if(mira.rect.right > ancho - 50):
            fondo1.velx = -10
            fondo1.vely = 0
        elif (mira.rect.left <  50):
            fondo1.velx = 10
            fondo1.vely =0
        elif (mira.rect.top < 50):
            fondo1.vely = 10
            fondo1.velx =0
        elif( mira.rect.bottom > alto - 50):
            fondo1.vely = -10
            fondo1.velx =0
        else:
            fondo1.velx=0
            fondo1.vely=0

        Miras.update()
        fondos.update()
        fondos.draw(pantalla)
        Miras.draw(pantalla)
        pg.display.flip()
        reloj.tick(35)
