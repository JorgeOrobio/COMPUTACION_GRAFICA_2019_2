# PARALAJE PARALAX


import pygame as pg
from libreria import*
import random
import configparser as cp

def matriz_sprites(imagen,height,high):
    pass
    datos=imagen.get_rect()
    x,y = 0,0
    matriz=[]
    lista=[]
    print(datos.height)
    print(datos.width)
    for j in range(0,datos.width,high):
        for i in range(0,datos.height,height):
            imag=imagen.subsurface(j,i,height,high)
            lista.append(imag)
        matriz.append(lista)
        lista=[]
    return matriz

if __name__ == '__main__':

    # PANTALLA
    pg.init()
    pantalla = pg.display.set_mode([ancho,alto])
    #CAMBIAR LA IMAGEN A SU RESPECTIVO SITIO DEPENDIENDO DEL PC
    matriz=[]
    reloj= pg.time.Clock()
    infomapa = cp.ConfigParser()
    infomapa.read('mapatr.map')
    x,y=0,0
    archivo = infomapa.get('info','origen')
    imagen=pg.image.load(archivo)
    matriz=matriz_sprites(imagen,32,32)
    s_mapa=infomapa.get('info','mp')
    mapa = s_mapa.split('\n')
    print(mapa)
    i,j=0,0
    for filas in mapa:
        for ele in filas:
            for elemento in infomapa.items(ele):
                if i<(len(filas)*32) and j<(len(mapa)*32):
                    if filas.get(ele)!='pasto':
                        if elemento[0] == 'col':
                            x=int(elemento[1])
                        if elemento[0] == 'fil':
                            y=int(elemento[1])
                        print("")
                        print("x: ",x)
                        print("y: ",y)
                        print("i: ",i)
                        print("j: ",j)
                        print("")
                        pantalla.blit(matriz[x][y],[i,j])
            pg.display.flip()
            i+=32
        i=0
        j+=32
    print("SALIO")
    pantalla.blit(matriz[x][y],[0,0])
    pg.display.flip()
    reloj.tick(1)

    fin = False
    # CICLO PRINCIPAL
    while not fin:
        for event in pg.event.get():
            #EVENTOS
            if event.type ==pg.QUIT:
                fin = True
