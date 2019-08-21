import pygame as pg
pg.init()
ANCHO = 600
ALTO = 300
pantalla=pg.display.set_mode([ANCHO,ALTO])
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


while not fin:
    event=pg.event.get()
    pantalla.fill(NEGRO)
    pg.draw.line(pantalla,AZUL,[ANCHO/2,0],[ANCHO/2,ALTO]) #eje Y
    pg.draw.line(pantalla,AZUL,[0,ALTO/2],[ANCHO,ALTO/2])#eje X
    pg.draw.line(pantalla,BLANCO,ORIGEN,[280,230])
    pg.display.flip()
    for e in event:
        if e.type == pg.QUIT:
            fin = True
