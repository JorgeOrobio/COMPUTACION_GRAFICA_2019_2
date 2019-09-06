##TRANSFORMACION LINEAL DEL PLANO CARTESIANO AL PLANO DEL COMPUTADOR, POSICIONES DEFINIDAS

import pygame as pg
ANCHO = 600
ALTO = 300
fin = False
NEGRO = [0,0,0]
AZUL = [0,0,255]
BLANCO = [255,255,255]
ORIGEN = [300,150]
# while not fin:
#     event=pg.event.get()
#     pantalla.fill(NEGRO)
#     pg.draw.line(pantalla,AZUL,[ANCHO/2,0],[ANCHO/2,ALTO]) #eje Y
#     pg.draw.line(pantalla,AZUL,[0,ALTO/2],[ANCHO,ALTO/2])#eje X
#     pg.display.flip()
#     for e in event:
#         if e.type == pg.QUIT:
#             fin = True

#
# while not fin:
#     event=pg.event.get()
#     pantalla.fill(NEGRO)
#     pg.draw.line(pantalla,AZUL,[ANCHO/2,0],[ANCHO/2,ALTO]) #eje Y
#     pg.draw.line(pantalla,AZUL,[0,ALTO/2],[ANCHO,ALTO/2])#eje X
#     pg.draw.line(pantalla,BLANCO,ORIGEN,[340,90])
#     pg.display.flip()
#     for e in event:
#         if e.type == pg.QUIT:
#             fin = True
def transformacion_cartesiano_pantalla(x_cor,y_cor):
    x_t=x_cor+ORIGEN[0]
    y_t = ORIGEN[1]- y_cor
    return x_t,y_t

def dibujar_plano(pantalla):
    pg.draw.line(pantalla,AZUL,[ANCHO/2,0],[ANCHO/2,ALTO]) #eje Y
    pg.draw.line(pantalla,AZUL,[0,ALTO/2],[ANCHO,ALTO/2])#eje X

def dibujar_linea1(pantalla,posicion):
    x,y = transformacion_cartesiano_pantalla(posicion[0],posicion[1])
    pg.draw.line(pantalla,BLANCO,ORIGEN,[x,y])

if __name__ == '__main__':
    pg.init()
    pantalla=pg.display.set_mode([ANCHO,ALTO])
    while not fin:
        event=pg.event.get()
        pantalla.fill(NEGRO)
        dibujar_plano(pantalla)
        dibujar_linea1(pantalla,[60,80])
        dibujar_linea1(pantalla,[-20,-80])
        dibujar_linea1(pantalla,[100,30])
        pg.display.flip()
        for e in event:
            if e.type == pg.QUIT:
                fin = True
