import pygame
from libreria import*


if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode((ancho,alto))
    Plano_Cartesiano(pantalla)
    Puntos = Puntos_A_Pantalla(Pitagoricas(3,200))
    pygame.draw.polygon(pantalla,color_aleatorio(),Puntos,1)
    pygame.display.flip()
    fin = False
    nlados = 3
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    nlados +=1
                    Puntos = Puntos_A_Pantalla(Pitagoricas(nlados,200))
                if event.button == 5:
                    nlados -=1
                    if nlados <3:
                        nlados = 3
                    Puntos = Puntos_A_Pantalla(Pitagoricas(nlados,200))

        pantalla.fill(negro)
        pygame.draw.polygon(pantalla,color_aleatorio(),Puntos,1)
        pygame.display.flip()
