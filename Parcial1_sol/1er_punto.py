import pygame
from libreria import*

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode((ancho,alto))
    num_lados = 3
    triangulos = []
    triangulo = []
    escalado=[]
    copia1 = []
    copia2 = []
    copia3 =[]
    escalar = [0.5,0.5]
    lados = 0
    fin = False
    while not fin:
        pantalla.fill(negro)
        Plano_Cartesiano(pantalla)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:#AGREGAR PUNTOS Y FIGURAS
                    if (event.pos[0]<origen[0] and event.pos[1]>origen[1]):
                        if lados < num_lados and len(triangulos)<2:
                            triangulo.append(event.pos)
                            lados += 1
                        elif(len(triangulos)<2):
                            triangulos.append(triangulo)
                            # triangulo = []
                            # lados=0
                        else:
                            pass
                if event.button == 3:#ROTAR LA FIGURA RESPECTO A UN PUNTO
                    escalado=triangulo
                    Puntos_A_Cartesiano(escalado)
                    copia1=triangulo[0]
                    MenosX=copia1[0]*-1
                    MenosY=copia1[1]*-1
                    copia2=[MenosX,MenosY]
                    Trasladar_Puntos(escalado,copia2)
                    Escalar_Puntos(escalado,escalar)
                    MasY=copia1[1]*-1
                    copia3=[copia1[0],MasY]
                    Trasladar_Puntos(escalado,copia3)
                    Puntos_A_Pantalla(escalado)
                    pygame.draw.polygon(pantalla,rojo,escalado,0)
                    for tr in triangulos:#DIBUJAR
                        pygame.draw.polygon(pantalla,azul,tr,0)

                    # MasY=
                    # Trasladar_Puntos(escalado,copia1)
                    # Puntos_A_Pantalla(escalado)


        # print(triangulos)
        for tr in triangulos:#DIBUJAR
            pygame.draw.polygon(pantalla,azul,tr,0)

        pygame.display.flip()
