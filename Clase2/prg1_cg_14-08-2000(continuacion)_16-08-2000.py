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
y1=0
y2=100
y3=200
reloj=pg.time.Clock()
while not fin:
    event=pg.event.get()
    pantalla.fill([0,0,0])
    pg.draw.line(pantalla,[0,255,0],[0,y1],[100,y2])
    pg.draw.line(pantalla,[0,255,0],[100,y2],[200,y1])
    pg.draw.line(pantalla,[0,255,0],[200,y1],[200,y3])
    pg.draw.line(pantalla,[0,255,0],[0,y1],[200,y1])
    pg.draw.line(pantalla,[0,255,0],[0,y3],[0,y1])
    pg.draw.line(pantalla,[0,255,0],[200,y3],[0,y3])
    pg.display.flip()
    for e in event:
        if e.type == pg.QUIT:
            fin = True
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_UP:
                y1-=10
                y2-=10
                y3-=10
            if e.key == pg.K_DOWN:
                y1+=10
                y2+=10
                y3+=10
    reloj.tick(20)
