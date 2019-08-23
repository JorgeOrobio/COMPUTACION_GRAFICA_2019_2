import pygame as pg
pg.init()
pantalla=pg.display.set_mode([600,300])

fin = False
NEGRO = [0,0,0]
BLANCO = [255,255,255]
ORIGEN = [300,150]
NEGRO=[0,0,0]
AZUL=[0,0,255]
reloj=pg.time.Clock()
ls_puntos=[]
index = 1
while not fin:
    event=pg.event.get()
    for e in event:
        if e.type == pg.QUIT:
            fin = True
        if e.type == pg.MOUSEBUTTONDOWN:
            ls_puntos.append(e.pos)
            if len(ls_puntos) >= 2:
                pg.draw.line(pantalla,BLANCO,ls_puntos[index-1],ls_puntos[index])
                index+=1
                pg.display.flip()
            if index > 2:
                print("DEBERIA MOVERSE")
                while e.type != pg.MOUSEBUTTONDOWN:
                    print("ENTRO WHILE")
                    p= (pg.mouse.get_pos())
                    pantalla.fill(NEGRO)
                    pg.draw.line(pantalla,BLANCO,ls_puntos[index],p)
                    pg.display.flip()
                    reloj.tick(20)
