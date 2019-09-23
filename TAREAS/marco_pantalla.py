import pygame as pg
from libreria import*


if __name__ == '__main__':
    pg.init
    pantalla = pg.display.set_mode([ancho,alto])
    fin = False
    lineas=[[[10,30],[20,30]],[[20,30],[20,10]],[[20,10],[30,10]]]
    velx=0
    vely=0
    while not fin:
        for event in pg.event.get():
            if event.type ==pg.QUIT:
                fin = True
        marco_pantalla(pantalla,lineas,velx,vely)

        pg.display.flip()
