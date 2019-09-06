import pygame as pg 
ANCHO = 600
ALTO = 300
fin = False
NEGRO = [0,0,0]
AZUL = [0,0,255]
BLANCO = [255,255,255]
ORIGEN = [ANCHO/2,ALTO/2]


if __name__ == '__main__':
    pg.init
    pantalla = pg.display.set_mode([ANCHO,ALTO])
    pg.display.flip()
    ls_puntos=[]
    fin = False
    index= 1
    while not fin:
        for event in pg.event.get():
            if event.type ==pg.QUIT:
                fin = True
