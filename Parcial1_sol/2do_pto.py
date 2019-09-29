import pygame
from libreria import*

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode((ancho,alto))
    punto = [origen[0]+100,origen[1]]
    velAng=5
    Ang=0
    fin = False
    reloj=pygame.time.Clock()
    while not fin:
        pantalla.fill(negro)
        Plano_Cartesiano(pantalla)
        pygame.draw.circle(pantalla,verde,punto,5)
        pygame.display.flip()
        reloj.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                while( Ang < 270):
                    punto=A_Cartesiano(punto)
                    punto = Rotar_Horario(punto,velAng)
                    Ang += velAng
                    punto=A_Pantalla(punto)
                    pantalla.fill(negro)
                    Plano_Cartesiano(pantalla)
                    pygame.draw.circle(pantalla,verde,punto,1)
                    pygame.display.flip()
                    reloj.tick(20)
                    print(punto)
                while punto[0] < ancho:
                    punto=A_Cartesiano(punto)
                    punto[0]+=velAng
                    punto=A_Pantalla(punto)
                    print(punto)
                    pantalla.fill(negro)
                    Plano_Cartesiano(pantalla)
                    pygame.draw.circle(pantalla,verde,punto,1)
                    pygame.display.flip()
                    reloj.tick(20)
