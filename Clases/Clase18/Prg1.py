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
    def __init__(self,matriz,limite):
        pg.sprite.Sprite.__init__(self)
        self.limite=limite
        self.accion=1
        self.col=0
        self.matriz=matriz
        self.image = self.matriz[self.col][self.accion]
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y=100
        self.velx=0
        self.vely=0

    def update(self):
        self.image = self.matriz[self.col][self.accion]
        if self.velx != 0 or self.vely !=0 or self.accion != 1:
            if self.col >=self.limite[self.accion]:
                self.col=0
            else:
                self.col+=1
        self.rect.x += self.velx
        self.rect.y += self.vely

    def position(self):
        pass
        return [self.rect.x,self.rect.y]

class Bloque(pg.sprite.Sprite):
    """clase bloque"""
    def __init__(self,pos,cl=blanco):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([50,100])
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.error=10

    def update(self):
        if self.velx >=0:
            self.rect.x += self.velx
            self.velx -=1

    def EnLimite(self,pos_jugador):
        cumple=False
        liminf=self.rect.bottom - self.error
        limsup=self.rect.bottom + self.error
        if  liminf < pos_jugador <limsup :
            cumple=True
        else:
            cumple=False
        return cumple

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
    def update(self):
        if self.click:
            self.rect.center = pg.mouse.get_pos()


if __name__ == '__main__':

    # PANTALLA
    pg.init()
    pantalla = pg.display.set_mode([ancho,alto])
    archivo='/home/jorge/Escritorio/CGrafica/Sprites/Street_Figther/ken.png'
    fondo = pg.image.load(archivo) #CAMBIAR LA IMAGEN A SU RESPECTIVO SITIO DEPENDIENDO DEL PC
    matriz=[]
    reloj= pg.time.Clock()
    # RECORTE DEL TIPO (ANCHO_IMAGEN,ALTO_IMAGEN,ANCHO_SPRITE,ALTO_SPRITE)
    matriz=matriz_sprites(fondo,490,800,70,80)
    # CANTIDAD DE SPRITES DE LA IMAGEN POR FILA
    limite=[3,3,2,4,1,3,4,4,6,0]
    # CREACION DE GRUPOOS
    jugadores = pg.sprite.Group()
    bloques=pg.sprite.Group()
    cuadros = pg.sprite.Group()
    # CUADRO
    obj=Cuadro([100,100])
    cuadros.add(obj)
    pg.display.flip()
    fin = False
    while not fin:
        event=pg.event.get()
        for e in event:
            if e.type == pg.QUIT:
                fin = True
            if e.type == pg.MOUSEBUTTONDOWN:
                if obj.rect.collidepoint(e.pos):
                    obj.click = True
            if e.type == pg.MOUSEBUTTONUP:
                    obj.click=False

        cuadros.update()
        pantalla.fill(negro)
        cuadros.draw(pantalla)
        pg.display.flip()
        reloj.tick(20)
