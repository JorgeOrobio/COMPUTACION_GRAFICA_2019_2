import pygame
from libreria import*

def cartesianas_a_polares(x,y):
    r = int(math.sqrt(x**2 + y **2))
    angulo = math.atan(y/x)
    angulo = angulo* 180 / math.pi
    return r,angulo

def coordenadas_polares1(r,angulo):
    angu1= math.radians(angulo)
    p =(int(r*math.cos(angu1)), int(r*math.sin(angu1)))
    return p

def mover_punto(a,tam):
	R = []
	for i in range(0,360):
		r = tam*(math.cos(a*math.radians(i)))
		p = coordenadas_polares(r,i)
		R.append(p)
		r-=10
	return R

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode((ancho,alto))
    fin = False
    r,angulo = 10,0
    circulos = []
    z = []
    circulos_e = []
    cont = 0
    reloj=pygame.time.Clock()
    while not fin:
        Plano_Cartesiano(pantalla)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x_camb=event.pos[0]
                    y_camb=event.pos[1]
                    if (x_camb>origen[0] and y_camb<origen[1] and len(circulos)<1):
                        x=x_camb
                        y=y_camb
                        circulos.append(event.pos)
                        z=event.pos
                    # r,angulo = coordenadas_polares(0,10)
                    # print(r,angulo)
                if event.button == 3:
                    while (r >= 9):
                        circulos[0] = A_Cartesiano(circulos[0])
                        r,angulo = cartesianas_a_polares(circulos[0][0],circulos[0][1])
                        print(r)
                        print(" ")
                        print(angulo)
                        r -= 10
                        circulos[0] = coordenadas_polares(r,angulo)
                        circulos[0]= A_Pantalla(circulos[0])
                        for tr in circulos:
                            pygame.draw.circle(pantalla,color_aleatorio(),tr,2)
                        Plano_Cartesiano(pantalla)
                        pygame.display.flip()
                        reloj.tick(20)
                    # print("holii")
                    angulo += 120
                    circulos[0]=coordenadas_polares(r,angulo)
                    i=0
                    print(circulos[0])
                    while( circulos[0][0] > -origen[0]):
                        print(r)
                        print(" ")
                        print(angulo)
                        r += 10
                        circulos[0] = coordenadas_polares(r,angulo)
                        circulos[0]= A_Pantalla(circulos[0])
                        for tr in circulos:
                            pygame.draw.circle(pantalla,color_aleatorio(),tr,2)
                        Plano_Cartesiano(pantalla)
                        pygame.display.flip()
                        reloj.tick(20)
