import pygame
from LibreriaPantalla import* 

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode((ancho,alto))
    fin = False
    #num_lados = 3
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if lados < 3:
                        triangulo.append(event.pos)
                        lados += 1
                    else:
                        triangulos.append(triangulo)
                        triangulo = []
                        lados = 0
                if event.button == 4:
                    for tr in triangulos:
                        Puntos_A_Pantalla(tr)
                        Rotar_Puntos_Horario(tr,4)
                        Puntos_A_Cartesiano(tr)
                if event.button == 5:
                    for tr in triangulos:
                        Puntos_A_Pantalla(tr)
                        Rotar_Puntos_Horario(tr,-4)
                        Puntos_A_Cartesiano(tr)
                if event.button == 3:
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



        for tr in triangulos:
            pygame.draw.polygon(pantalla,azul,tr,0)

        pygame.display.flip()
        pantalla.fill(negro)
