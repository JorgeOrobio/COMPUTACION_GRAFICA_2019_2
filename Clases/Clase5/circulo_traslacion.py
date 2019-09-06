import pygame as pg
ANCHO = 600
ALTO = 300
fin = False
NEGRO = [0,0,0]
ROJO = [255,0,0]
AZUL = [0,0,255]
BLANCO = [255,255,255]
ORIGEN = [ANCHO/2,ALTO/2]

def diujar_circulo(pantalla, ls_puntos,index):
        pg.draw.circle(pantalla,BLANCO,ls_puntos[index],10)

##LAS TUPLAS NO SE PUEDEN CAMBIAR!!!
def trasladar_triangulo(pantalla,ls_puntos, escalado ):
    ls_escalada=[]
    ls_centrada=centrar_puntos(ls_puntos)
    for p in ls_centrada:
        px= int(p[0] + escalado[0])
        py= int(p[1] + escalado[1])
        ls_escalada.append([px,py])
    dibujar_centro(pantalla,ls_escalada)

def centrar_puntos(ls_puntos):
    ls=[]
    for p in ls_puntos:
        px= p[0] - ORIGEN[0]
        py= ORIGEN[1] - p[1]
        ls.append([px,py])
    return ls

def dibujar(pantalla,ls_puntos):
    index = len(ls_puntos) -1
    for e in ls_puntos:
        pg.draw.circle(pantalla,AZUL,ls_puntos[index],10)
        index-=1
def transformar_puntos(ls_puntos):
    ls_transformada=[]
    for p in ls_puntos:
        px=p[0]+ORIGEN[0]
        py= ORIGEN[1]-p[1]
        ls_transformada.append([px,py])
    return ls_transformada


def dibujar_centro(pantalla,ls_puntos):
    ls_puntos = transformar_puntos(ls_puntos)
    index = len(ls_puntos) -1
    for e in ls_puntos:
        pg.draw.circle(pantalla,AZUL,ls_puntos[index],10)
        index-=1

def dibujar_plano(pantalla):
        pg.draw.line(pantalla,ROJO,[ANCHO/2,0],[ANCHO/2,ALTO]) #eje Y
        pg.draw.line(pantalla,ROJO,[0,ALTO/2],[ANCHO,ALTO/2])#eje X

if __name__ == '__main__':
    pg.init
    pantalla = pg.display.set_mode([ANCHO,ALTO])
    pg.display.flip()
    ls_puntos=[]
    ls_puntosEscalada=[]
    fin = False
    index=0
    trasladado=[10,10]
    trasladado2=[-10,-10]
    while not fin:
        for event in pg.event.get():
            if event.type ==pg.QUIT:
                fin = True
            if event.type == pg.MOUSEBUTTONDOWN:
                dibujar_plano(pantalla)
                if len(ls_puntos) <= 1:
                    ls_puntos.append(event.pos)
                    diujar_circulo(pantalla,ls_puntos,index)
                    trasladar_triangulo(pantalla,ls_puntos,trasladado2)
                    trasladar_triangulo(pantalla,ls_puntos,trasladado)
