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

if __name__ == '__main__':

    # PANTALLA
    pg.init()
    pantalla = pg.display.set_mode([ancho,alto])
    archivo='/home/jorge/Escritorio/CGrafica/Sprites/Proyecto1/Personaje/animal/animals.png'
    fondo = pg.image.load(archivo) #CAMBIAR LA IMAGEN A SU RESPECTIVO SITIO DEPENDIENDO DEL PC
    matriz=[]
    reloj= pg.time.Clock()
    matriz=matriz_sprites(fondo,384,256,32,32)
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
        pantalla.fill(negro)
        pantalla.blit(matriz[con][0],[0,0])
        pg.display.flip()
        reloj.tick(10)
        if con >=9:
            con=7
        else:
            con+=1
