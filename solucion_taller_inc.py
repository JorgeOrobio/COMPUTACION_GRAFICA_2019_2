import pygame as pg
ANCHO = 600
ALTO = 300
fin = False
NEGRO = [0,0,0]
ROJO = [255,0,0]
AZUL = [0,0,255]
BLANCO = [255,255,255]
ORIGEN = [ANCHO/2,ALTO/2]

def dibujar_triangulo(pantalla, ls_puntos, index ,):
    if len(ls_puntos) >= 2 and len(ls_puntos) <= 3:
        pg.draw.line(pantalla,BLANCO,ls_puntos[index-1],ls_puntos[index])
        index+=1
    if len(ls_puntos) > 3:
        pg.draw.line(pantalla,BLANCO,ls_puntos[index-1],ls_puntos[0])
    pg.display.flip()
    return  index

##LAS TUPLAS NO SE PUEDEN CAMBIAR!!!
def escalar_triangulo(pantalla,ls_puntos, escalado ):
    ls_escalada=[]
    for p in ls_puntos:
        px= int(p[0] * escalado[0])
        py= int(p[1] * escalado[1])
        ls_escalada.append([px,py])
    dibujar(pantalla,ls_escalada)

def dibujar(pantalla,ls_puntos):
    index = len(ls_puntos) -1
    for e in ls_puntos:
        pg.draw.line(pantalla,AZUL,ls_puntos[index-1],ls_puntos[index])
        index-=1

if __name__ == '__main__':
    pg.init
    pantalla = pg.display.set_mode([ANCHO,ALTO])
    pg.display.flip()
    ls_puntos=[]
    ls_puntosEscalada=[]
    fin = False
    escalado=[2,2]
    escalado2=[0.5,0.5]
    index= 1
    while not fin:
        for event in pg.event.get():
            if event.type ==pg.QUIT:
                fin = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if len(ls_puntos) <= 3:
                    ls_puntos.append(event.pos)
                    index = dibujar_triangulo(pantalla,ls_puntos,index)
                    escalar_triangulo(pantalla,ls_puntos,escalado2)
                    escalar_triangulo(pantalla,ls_puntos,escalado)
                print (len(ls_puntos))
                print (ls_puntos[-1])
