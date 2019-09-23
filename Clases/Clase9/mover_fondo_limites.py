import pygame as pg
from libreria import*

if __name__ == '__main__':
    pg.init()
    pantalla = pg.display.set_mode((ancho,alto))
    img = pg.image.load('descarga.jpeg')
    fondo = pg.image.load('fondo1.png')
    info= fondo.get_rect()
    print(info)
    fondox=-100
    fondoy=-100
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
                    vely= 5
                    velx=0
                if event.key == pg.K_DOWN:
                    vely= -5
                    velx=0
                if event.key == pg.K_RIGHT:
                    velx= -5
                    vely=0
                if event.key == pg.K_LEFT:  #273 4 5 6
                    velx= 5
                    vely=0
                if event.key == pg.K_SPACE:
                    velx=0
                    vely=0

        # print(y)
        # print(fondoy)
        if fondox<((info[2]-ancho)*-1):
            fondox=(info[2]-ancho)*-1
            print(fondox)
            velx =0
        elif fondox>0:
            fondox=0
            velx=0
        else:
            fondox+=velx
        if fondoy<((info[3]-alto)*-1):
            fondoy=(info[3]-alto)*-1
            vely=0
        elif fondoy>0 :
            fondoy=0
            vely=0
        else:
            fondoy+=vely
        pantalla.fill(negro)
        pantalla.blit(fondo,[fondox,fondoy])
        pg.display.flip()
        reloj.tick(30)
