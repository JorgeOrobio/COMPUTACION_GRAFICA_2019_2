import pygame as pg
from libreria import*
import random
import configparser as cp


if __name__ == '__main__':

    # PANTALLA
    pg.init()
    pantalla = pg.display.set_mode([ancho,alto])
    archivo='/home/jorge/Escritorio/CGrafica/Sprites/Proyecto1/Personaje/nave.png'
    perso = pg.image.load(archivo) #CAMBIAR LA IMAGEN A SU RESPECTIVO SITIO DEPENDIENDO DEL PC
    infoperso=perso.get_rect()
    rotperson=pg.transform.rotate(perso,90)
    inforotperso=rotperson.get_rect()
    print(infoperso.midtop)
    print(inforotperso.midtop)
    reloj= pg.time.Clock()
    fin = False
    while not fin:
        event=pg.event.get()
        for e in event:
            if e.type == pg.QUIT:
                fin = True


        pantalla.fill(negro)
        pantalla.blit(perso,[100,100])
        pantalla.blit(rotperson,[200,200])
        pg.display.flip()
        reloj.tick(10)
