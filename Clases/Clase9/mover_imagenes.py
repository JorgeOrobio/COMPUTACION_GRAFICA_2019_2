import pygame as pg
from libreria import*

if __name__ == '__main__':
    pg.init()
    pantalla = pg.display.set_mode((ancho,alto))
    img = pg.image.load('descarga.jpeg')
    fondo = pg.image.load('fondo1.png')
    info= img.get_rect()
    print(info)
    x=100
    y=100
    velx=0
    vely=0
    reloj=pg.time.Clock()
    fin = False
    while not fin:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                fin = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    vely= -5
                    velx=0
                if event.key == pg.K_DOWN:
                    vely= 5
                    velx=0
                if event.key == pg.K_RIGHT:
                    velx= 5
                    vely=0
                if event.key == pg.K_LEFT:  #273 4 5 6
                    velx= -5
                    vely=0
                if event.key == pg.K_SPACE:
                    velx=0
                    vely=0

        # print(y)
        if x>(ancho-info[2]):
            x= ancho-info[2]
            velx =0
        elif x<0:
            x=0
            velx=0
        else:
            x+=velx
        if y>(alto-info[3]):
            y=alto-info[3]
            vely=0
        elif y<0 :
            y=0
            vely=0
        else:
            y+=vely
        pantalla.fill(negro)
        pantalla.blit(fondo,[0,0])
        pantalla.blit(img,[x,y])
        pg.display.flip()
        # x+=2
        reloj.tick(60)
