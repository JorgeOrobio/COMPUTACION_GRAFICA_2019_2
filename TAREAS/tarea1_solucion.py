import pygame as pg
pg.init()
pantalla=pg.display.set_mode([600,300])
fin = False
NEGRO=[0,0,0]
AZUL=[0,0,255]
flag=1
posicion1=[0,0]
posicion2=[0,0]
while not fin:

    event=pg.event.get()
    for e in event:
        if e.type == pg.QUIT:
            fin = True
        if e.type == pg.MOUSEBUTTONDOWN:
            if e.button == 1:
                posicion1=e.pos
                flag+=1
                if flag == 2:
                    posicion2=e.pos
                    flag=0
    print(flag)
    pantalla.fill(NEGRO)
    pg.draw.line(pantalla,AZUL,posicion1,posicion2)
    pg.display.flip()
