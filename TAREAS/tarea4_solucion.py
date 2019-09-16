import pygame as pg
from libreria import*


if __name__ == '__main__':
    pg.init
    pantalla = pg.display.set_mode([ancho,alto])
    fin = False
    lineas=[]
    linea=[]
    lineas_pantalla=[]
    lineas_cartesiano=[]
    while not fin:
        for event in pg.event.get():
            if event.type ==pg.QUIT:
                fin = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if len(linea) < 2:
                        linea.append(event.pos)
                    else:
                        lineas.append(linea)
                        linea=[]
                if event.button == 2:
                    # print(lineas)
                    for p in lineas:
                        Puntos_A_Cartesiano(p)
                        lineas_cartesiano.append(p)
                    lineasN=Conjunto_Por_MenosUno(lineas_cartesiano)
                    for e in lineasN:
                        Puntos_A_Pantalla(e)
                        lineas_pantalla.append(e)
                    for i in lineas_pantalla:
                        Recta(i,pantalla,0,1)

        Plano_Cartesiano(pantalla)
        for e in lineas:
            pg.draw.line(pantalla,blanco,e[0],e[1])
        pg.display.flip()
