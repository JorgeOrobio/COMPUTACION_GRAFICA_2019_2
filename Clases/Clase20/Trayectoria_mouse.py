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
    def update(self):
        self.image = self.matriz[self.col][self.dir]
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


class Jugador_Dir(pg.sprite.Sprite):
    """clase jugador animal"""
    def __init__(self,matriz,puntoi,puntof):
        pg.sprite.Sprite.__init__(self)
        self.dir=0
        self.col=3
        self.matriz=matriz
        self.image = self.matriz[self.col][self.dir]
        self.rect=self.image.get_rect()
        self.puntof= puntof
        self.rect.x=puntoi[0]
        self.rect.y=puntoi[1]
        self.velx= 0
        self.m=((puntof[1]-puntoi[1])/(puntof[0]-puntoi[0]))
        self.b= self.rect.y - (self.m*self.rect.x)

    def recalY(self,m,b,x):
        y = m*x + b
        return(int(y))

    def update(self):
        self.image = self.matriz[self.col][self.dir]
        if self.velx != 0:
            if self.col >=5:
                self.col=3
            else:
                self.col+=1
        if self.rect.x < self.puntof[0]:
            self.rect.x += self.velx
            self.rect.y = self.recalY(self.m,self.b,self.rect.x)
        else:
            self.velx =0

    def repos(self,position):
        self.m = ((position[1]-self.rect.y)/(position[0]-self.rect.x))
        self.b= self.rect.y - (self.m*self.rect.x)
        self.puntof = position
        # self.rect.x
        # self.rect.y

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
    puntoi=[100,100]
    puntof=[200,200]
    j=Jugador_Dir(matriz,puntoi,puntof)
    jugadores.add(j)
    # pantalla.blit(fondo,[0,0])
    # print(matriz)
    # pantalla.blit(matriz[0][0],[0,0])
    pg.display.flip()
    # con=7
    fin = False
    while not fin:
        event=pg.event.get()
        for e in event:
            if e.type == pg.QUIT:
                fin = True
            #MOVIMIENTO DIRECCIONADO
            if e.type==pg.MOUSEBUTTONDOWN:
                j.velx=5
                j.repos(e.pos)
        pantalla.fill(negro)
        jugadores.draw(pantalla)
        jugadores.update()
        pg.display.flip()
        reloj.tick(10)
