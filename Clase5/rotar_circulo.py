import pygame as pg
import math
ANCHO = 600
ALTO = 300
fin = False
NEGRO = [0,0,0]
ROJO = [255,0,0]
AZUL = [0,0,255]
BLANCO = [255,255,255]
ORIGEN = [ANCHO/2,ALTO/2]

def dibujar_circulo(pantalla, ls_puntos):
        pg.draw.circle(pantalla,BLANCO,ls_puntos,1)

def dibujar_circulo_2(pantalla, ls_puntos):
        pg.draw.circle(pantalla,ROJO,ls_puntos,1)

##LAS TUPLAS NO SE PUEDEN CAMBIAR!!!
def rotar_circulo(pantalla,ls_puntos):
    ls_centrada=centrar_puntos(ls_puntos)
    px= int(ls_centrada[0] + escalado[0])
    py= int(ls_centrada[1] + escalado[1])
    ls_escalada=[px,py]
    dibujar_centro(pantalla,ls_escalada)

def centrar_puntos(ls_puntos):
    px= ls_puntos[0] - ORIGEN[0]
    py= ORIGEN[1] - ls_puntos[1]
    ls=[px,py]
    return ls

def dibujar(pantalla,ls_puntos):
    pg.draw.circle(pantalla,AZUL,ls_puntos,1)

def transformar_puntos(ls_puntos):
    px= ls_puntos[0]+ORIGEN[0]
    py= ORIGEN[1]-ls_puntos[1]
    ls_transformada=[px,py]
    return ls_transformada

def dibujar_centro(pantalla,ls_puntos):
    ls_puntos = transformar_puntos(ls_puntos)
    pg.draw.circle(pantalla,AZUL,ls_puntos,1)
    return ls_puntos

def rotar_punto_antihorario(pantalla,punto,grados):
    centrada=centrar_puntos(punto)
    xr= int (centrada[0]*math.cos(math.radians(grados)) - centrada[1]*math.sin(math.radians(grados)))
    yr= int (centrada[0]*math.sin(math.radians(grados)) + centrada[1]*math.cos(math.radians(grados)))
    pto_rotado=[xr,yr]
    dev=dibujar_centro(pantalla,pto_rotado)
    return dev

def rotar_punto_horario(pantalla,punto,grados):
    centrada=centrar_puntos(punto)
    xr= int (centrada[0]*math.cos(math.radians(grados)) + centrada[1]*math.sin(math.radians(grados)))
    yr= int ( - centrada[0]*math.sin(math.radians(grados)) + centrada[1]*math.cos(math.radians(grados)))
    pto_rotado=[xr,yr]
    dev=dibujar_centro(pantalla,pto_rotado)
    return dev

def dibujar_plano(pantalla):
        pg.draw.line(pantalla,ROJO,[ANCHO/2,0],[ANCHO/2,ALTO]) #eje Y
        pg.draw.line(pantalla,AZUL,[0,ALTO/2],[ANCHO,ALTO/2])#eje X

if __name__ == '__main__':
    pg.init
    pantalla = pg.display.set_mode([ANCHO,ALTO])
    pg.display.flip()
    ls_puntos=[0,0]
    ls_puntosEscalada=[]
    fin = False
    index=1
    while not fin:
        for event in pg.event.get():
            if event.type ==pg.QUIT:
                fin = True
            pantalla.fill(NEGRO)
            dibujar_plano(pantalla)
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    ls_puntos=event.pos
                    print(ls_puntos)
                dibujar_circulo(pantalla,ls_puntos)
                if event.button == 4:
                    ls_puntos=rotar_punto_antihorario(pantalla,ls_puntos,5)
                    dibujar_circulo_2(pantalla,ls_puntos)
                    pg.display.flip()
                if event.button == 5:
                    ls_puntos=rotar_punto_horario(pantalla,ls_puntos,5)
                    dibujar_circulo_2(pantalla,ls_puntos)
                    pg.display.flip()
