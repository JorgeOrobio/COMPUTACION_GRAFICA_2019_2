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

            for i in lineas:
                Recta(i,pantalla,0,1)
            while lineas[2][1][0]<ancho-10 and lineas[0][0][1]==30:
                velx=20
                vely=0
                for e in lineas:
                    for i in e:
                        i[0]+=velx
                for i in lineas:
                    Recta(i,pantalla,0,1)
            while lineas[2][1][1]<alto-50:
                velx=0
                vely=30
                for e in lineas:
                    for i in e:
                        i[1]+=vely
                for i in lineas:
                    Recta(i,pantalla,0,1)
            while lineas[0][0][0]>10:
                velx=-20
                vely=0
                for e in lineas:
                    for i in e:
                        i[0]+=velx
                for i in lineas:
                    Recta(i,pantalla,0,1)
            while lineas[2][1][1]>40:
                velx=0
                vely=-30
                for e in lineas:
                    for i in e:
                        i[1]+=vely
                for i in lineas:
                    Recta(i,pantalla,0,1)
        pg.display.flip()
