import pygame as pg
from libreria import*
import random
import configparser as cp

def matriz_sprites(imagen,anc,alt,height,high):
    pass
    x,y = 0,0
    matriz=[]
    lista=[]
    for j in range(0,anc,height):
        for i in range(0,alt,high):
            imag=imagen.subsurface(j,i,height,high)
            lista.append(imag)
        matriz.append(lista)
        lista=[]
    return matriz

class Jugador(pg.sprite.Sprite):
    """clase jugador animal"""
    def __init__(self,matriz):
        pg.sprite.Sprite.__init__(self)
        self.dir=0
        self.col=3
        self.matriz=matriz
        self.image = self.matriz[self.col][self.dir]
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y=100
        self.velx=0
        self.vely=0
        self.vuelo=False

    def update(self):
        self.image = self.matriz[self.col][self.dir]
        if j.vuelo:
            pass
            if self.velx != 0 or self.vely !=0:
                if self.col >=8:
                    self.col=6
                else:
                    self.col+=1
        else:
            if self.velx != 0 or self.vely !=0:
                if self.col >=5:
                    self.col=3
                else:
                    self.col+=1

        self.rect.x += self.velx
        self.rect.y += self.vely

    def position(self):
        pass
        return [self.rect.x,self.rect.y]

if __name__ == '__main__':

    # PANTALLA
    pg.init()
    pantalla = pg.display.set_mode([ancho,alto])
    archivo='/home/jorge/Escritorio/CGrafica/Sprites/Proyecto1/Personaje/animal/animals.png'
    fondo = pg.image.load(archivo) #CAMBIAR LA IMAGEN A SU RESPECTIVO SITIO DEPENDIENDO DEL PC
    matriz=[]
    reloj= pg.time.Clock()
    matriz=matriz_sprites(fondo,384,256,32,32)

    jugadores = pg.sprite.Group()
    j=Jugador(matriz)
    jugadores.add(j)
    # pantalla.blit(fondo,[0,0])
    # print(matriz)
    pantalla.blit(matriz[0][0],[0,0])
    pg.display.flip()

    con=7
    fin = False
    while not fin:
        event=pg.event.get()
        for e in event:
            if e.type == pg.QUIT:
                fin = True
            #MOVIMIENTO DIRECCIONADO
            if e.type==pg.KEYDOWN:
                if e.key == pg.K_RIGHT:
                    if j.vuelo:
                        j.velx=8
                        j.vely=0
                        j.dir=2
                    else:
                        j.velx=5
                        j.vely=0
                        j.dir=2

                if e.key == pg.K_LEFT:
                    if j.vuelo:
                        j.velx=-8
                        j.vely=0
                        j.dir=1
                    else:
                        j.velx=-5
                        j.vely=0
                        j.dir=1
                if e.key == pg.K_DOWN:
                    if j.vuelo:
                        j.vely=8
                        j.velx=0
                        j.dir=0
                    else:
                        j.vely=5
                        j.velx=0
                        j.dir=0
                if e.key == pg.K_UP:
                    if j.vuelo:
                        j.vely=-8
                        j.velx=0
                        j.dir=3
                    else:
                        j.vely=-5
                        j.velx=0
                        j.dir=3
                if e.key == pg.K_SPACE:
                    j.vuelo= not(j.vuelo)
            if e.type == pg.KEYUP:
                j.vely=0
                j.velx=0

        pantalla.fill(negro)
        jugadores.draw(pantalla)
        jugadores.update()
        pg.display.flip()
        reloj.tick(10)
