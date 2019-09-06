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
dibujo = 1
while not fin:
    event=pg.event.get()
    for e in event:
        if e.type == pg.QUIT:
            fin = True
        if e.type == pg.MOUSEBUTTONDOWN:
            ls_puntos.append(e.pos)
            if len(ls_puntos) >= 2:
                pantalla.fill(NEGRO)
                dibujo = index
                for dibujo in  len(ls_puntos):
                    pg.draw.line(pantalla,BLANCO,ls_puntos[dibujo-1],ls_puntos[dibujo])
                p= (pg.mouse.get_pos())
                print(p)
                pg.draw.line(pantalla,AZUL,ls_puntos[index],p)
                pg.display.flip()
                reloj.tick(20)
                index+=1
            # if index > 2:
            #     print("DEBERIA MOVERSE")
            #     while e.type != pg.MOUSEBUTTONDOWN:
            #         print("ENTRO WHILE")
            #         p= (pg.mouse.get_pos())
            #         pantalla.fill(NEGRO)
            #         reloj.tick(20)
            #         pg.display.flip()
            #         pg.draw.line(pantalla,BLANCO,ls_puntos[index],p)
