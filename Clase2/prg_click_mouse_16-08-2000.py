import pygame as pg
#
# print ('\n\n hola bebe, se que contigo no sirve la labia \n')
# a=12
# b=2.5
# c=a+b
# print (c)

pg.init()
pantalla=pg.display.set_mode([600,300])

# fin = False
# while not fin:
#    a= a+1
#    if a>1000:
#        fin = True
fin = False
NEGRO=[0,0,0]
AZUL=[0,0,255]
p=[200,200]
reloj=pg.time.Clock()
while not fin:
    event=pg.event.get()
    for e in event:
        if e.type == pg.QUIT:
            fin = True
        if e.type == pg.MOUSEBUTTONDOWN:
            print(e.pos, e.button)
            p=e.pos

    pantalla.fill(NEGRO)
    pg.draw.line(pantalla,AZUL,[300,150],p)
    pg.display.flip()
    reloj.tick(20)
