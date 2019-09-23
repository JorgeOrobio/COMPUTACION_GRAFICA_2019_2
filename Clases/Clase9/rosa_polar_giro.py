import pygame
from libreria import*
#colores


if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode((ancho,alto))

    Puntos = Puntos_A_Pantalla(Rosa_polar(6,200))

    pygame.draw.polygon(pantalla, color_aleatorio(), Puntos,3)
    pygame.display.flip()
    fin = False

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    Puntos_A_Cartesiano(Puntos)
                    Rotar_Puntos_Horario(Puntos,-3)
                    Puntos_A_Pantalla(Puntos)
                if event.button == 5:
                    Puntos_A_Cartesiano(Puntos)
                    Rotar_Puntos_Horario(Puntos,3)
                    Puntos_A_Pantalla(Puntos)


            pantalla.fill(negro)
            Plano_Cartesiano(pantalla)
            pygame.draw.polygon(pantalla, color_aleatorio(), Puntos, 1)
            pygame.display.flip()
