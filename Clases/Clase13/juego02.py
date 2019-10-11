
import pygame as pg
from libreria import*
import random

def matriz_sprites(imagen):
    pass
    x,y = 0,0
    matriz=[]
    lista=[]
    for j in range(0,1024,32):
        for i in range(0,384,32):
            imag=imagen.subsurface(j,i,32,32)
            lista.append(imag)
        matriz.append(lista)
        lista=[]
    return matriz

if __name__ == '__main__':

    # PANTALLA
    pg.init()
    pantalla = pg.display.set_mode([ancho,alto])
    fondo = pg.image.load("/home/jorge/Escritorio/CGrafica/Sprites/Proyecto1/Fondo/terrenogen.png")
    matriz=[]
    reloj= pg.time.Clock()
    matriz=matriz_sprites(fondo)
    for i in matriz:
        for j in i:
            pantalla.blit(j,[0,0])
            pg.display.flip()
            reloj.tick(1)
    # pantalla.blit(matriz[0][4],[0,0])
    # pg.display.flip()
    # reloj.tick(1)

    fin = False
    # CICLO PRINCIPAL
    while not fin:
        for event in pg.event.get():
            #EVENTOS
            if event.type ==pg.QUIT:
                fin = True
