#HACER QUE LA ULTIMA LINEA SIGA EL MOUSE HASTA QUE LE DE CLICK

import pygame as pg
ANCHO = 600
ALTO = 300
fin = False
NEGRO = [0,0,0]
AZUL = [0,0,255]
BLANCO = [255,255,255]
ORIGEN = [300,150]

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
            if event.type == pg.MOUSEBUTTONDOWN:
                ls_puntos.append(event.pos)
                if len(ls_puntos) >= 2:
                    pg.draw.line(pantalla,BLANCO,ls_puntos[index-1],ls_puntos[index])
                    index+=1

                pg.display.flip()
                print ls_puntos
                print len(ls_puntos)
                print ls_puntos[-1]
