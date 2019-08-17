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
r=100
g=0
x=100
y=100
color_actual=[r,g,0]
reloj=pg.time.Clock()
while not fin:
    event=pg.event.get()
    for e in event:
        if e.type == pg.QUIT:
            fin = True
        if e.type == pg.MOUSEBUTTONDOWN:
            p=e.pos
            x=p[0]
            y=p[1]
            if e.button == 4:
                r+=5
                color_actual=[r,0,0]
                if r>255 and g<255:
                    r=255
                    g+=5
                    color_actual=[r,g,0]
                    print(color_actual)
                if g = 255:
                    pass
    pantalla.fill(NEGRO)
    pg.draw.line(pantalla,color_actual,[300,150],[x,y])
    pg.display.flip()
    reloj.tick(20)
