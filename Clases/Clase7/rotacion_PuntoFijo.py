# Se establece pto ifjo
# Se establece la traslacion T=-pf
# Usando T se trasladan los puntos al origen
# Se aplica la rotacion con puntos llevados al origen
# Definimos T = pf y aplicamos la traslacion sobre los puntos rotados
#
#
#
#
#
#
#

import pygame
from libreria import*

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode((ancho,alto))
    fin = False
    pf=[0,0]
    num_lados = 3
    triangulos1 = []
    triangulos = []
    triangulo = []
    s = []
    l = []
    escalar = [2,2]
    lados = 0
    while not fin:
        Plano_Cartesiano(pantalla)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            # if event.type == pygame.MOUSEMOTION:
            #         print(event.pos)
            #             if event.button == 1:

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:#AGREGAR PUNTOS Y FIGURAS
                    if lados < num_lados:
                        triangulo.append(event.pos)
                        lados += 1
                    else:
                         triangulos.append(triangulo)
                         triangulo = []
                         lados = 0
                if event.button == 2:#ROTAR LA FIGURA RESPECTO A UN PUNTO
                    punto_f=event.pos
                    for tr in triangulos:
                        for t in tr:
                            esta=Esta_Cerca(event.pos,t)
                            if esta:
                                pf=t
                                pfn=[]
                                pfn.append(pf[0]*-1)
                                pfn.append(pf[1]*-1)
                                Trasladar_Puntos(tr,pfn)
                                Rotar_Puntos_Horario(tr,4)
                                Trasladar_Puntos(tr,pf)
                                print("ESTA CERCA")
                if event.button == 4: #ROTAR LA FIGURA
                    for tr in triangulos:
                        Puntos_A_Pantalla(tr)
                        Rotar_Puntos_Horario(tr,4)
                        Puntos_A_Cartesiano(tr)
                if event.button == 5: #ROTAR LA FIGURA
                    for tr in triangulos:
                        Puntos_A_Pantalla(tr)
                        Rotar_Puntos_Horario(tr,-4)
                        Puntos_A_Cartesiano(tr)
                if event.button == 3: #ESCALAR FIGURA
                    for tr in triangulos:
                        Puntos_A_Pantalla(tr)
                        s.append(triangulos[0][0][0]*-1)
                        s.append(triangulos [0][0][1] * -1)
                        Trasladar_Puntos(tr,s)
                        Escalar_Puntos(tr,escalar)
                        l.append(s[0]*-1)
                        l.append(s[1]*-1)
                        Trasladar_Puntos(tr,l)
                        Puntos_A_Cartesiano(tr)



        for tr in triangulos:#DIBUJAR
            pygame.draw.polygon(pantalla,azul,tr,0)

        pygame.display.flip()
        pantalla.fill(negro)
