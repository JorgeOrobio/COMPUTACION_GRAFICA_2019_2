import pygame as pg
from libreria import*
import random
import configparser as cp

def matriz_sprites(imagen):
    pass
    x,y = 0,0
    matriz=[]
    lista=[]
    for j in range(0,1024,32):
        for i in range(0,384,32):
            imag=imagen.subsurface(j,i,32,32)
            lista.append(imag)
        matriz.append(lista)
        lista=[]
    return matriz

if __name__ == '__main__':

    # PANTALLA
    pg.init()
    pantalla = pg.display.set_mode([ancho,alto])
    fondo = pg.image.load("/home/jorge/Escritorio/CGrafica/Sprites/Proyecto1/Fondo/terrenogen.png") #CAMBIAR LA IMAGEN A SU RESPECTIVO SITIO DEPENDIENDO DEL PC
    matriz=[]
    reloj= pg.time.Clock()
    matriz=matriz_sprites(fondo)
    infomapa = cp.ConfigParser()
    infomapa.read('mapatr.map')
    x,y=0,0
    # for elemento in infomapa.items('&'):
    #     if elemento[0] == 'col':
    #         x=int(elemento[1])
    #     if elemento[0] == 'fil':
    #         y=int(elemento[1])
    s_mapa=infomapa.get('info','mp')
    mapa = s_mapa.split('\n')
    print(mapa)
    i,j=0,0
    x=[]
    y0=[]
    for filas in mapa:
        for ele in filas:
            for elemento in infomapa.items(ele):
                if i<(len(filas)*32) and j<(len(mapa)*32):
                    print(elemento)
                    if elemento[0] == 'col':
                        x.append(int(elemento[1]))
                    if elemento[0] == 'fil':
                        y.append(int(elemento[1]))
                    # reloj.tick(1)
                    # reloj.tick(10)
            print("")
            print("x: ",x)
            print("y: ",y)
            print("i: ",i)
            print("j: ",j)
            print("")
            pantalla.blit(matriz[x][y],[i,j])
            i+=32
        i=0
        j+=32
        pg.display.flip()
    # CICLO PARA IR MOVIENDO LO ANTERIORMENTE MAPEADO
    for i in range(0,2080):
        for j in range(0,)
    print("SALIO")
    # for i in matriz:
    #     for j in i:
    #         pantalla.blit(j,[0,0])
    #         pg.display.flip()
    #         reloj.tick(1)
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
