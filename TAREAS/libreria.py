import math
import pygame as pg

#colores
blanco = [255,255,255]
negro = [0,0,0]
rojo = [255,0,0]
azul = [0,0,255]
verde = [0,255,0]
#dimensiones pantalla
ancho,alto = [600,600]
#centro de la pantalla
centro_x = ancho//2
centro_y = alto//2
origen = [centro_x,centro_y]

def multicolor():
    pass
#funcion que dibuja el plano cartesiano
def Plano_Cartesiano(pantalla):
    ox=origen[0]
    oy=origen[1]
    pg.draw.line(pantalla,blanco,[ox,0],[ox,alto])
    pg.draw.line(pantalla,blanco,[0,oy],[ancho,oy])

#funcion para dibujar una Recta con el mouse
def Recta(coordenadas,pantalla,a,b):
    pg.draw.line(pantalla,azul,coordenadas[a],coordenadas[b])

def Por_Menos_Uno(puntos):
    ls=[]
    for e in puntos:
        x=e[0]*-1
        y=e[1]*-1
        ls.append([x,y])
    return ls

def Conjunto_Por_MenosUno(lista):
    temp=[]
    temp2=[]
    for i in lista:
        temp=Por_Menos_Uno(i)
        temp2.append(temp)
        temp=[]
    return temp2

#funcion para dibujar un punto con el click
def Punto(coordenada,pantalla):
    pg.draw.circle(pantalla,rojo,coordenada,4)

#dibujar triangulo
def Triangulo_Lineas_Auto(coordenadas,pantalla):
    Recta(coordenadas,pantalla,0,1)
    Recta(coordenadas,pantalla,1,2)
    Recta(coordenadas,pantalla,0,2)

#funcion para dibujar un triangulo con el clicl
def Triangulo(coordenadas,pantalla,cont):
    if cont == 1:
        Recta(coordenadas,pantalla,cont-1,cont)
    if cont == 2:
        Recta(coordenadas,pantalla,cont-1,cont)
    if cont == 3:
        Recta(coordenadas,pantalla,cont-3,cont-1)

#pasar de cartesiano a pantalla
def A_Cartesiano(punto):
    xp=punto[0]-centro_x
    yp=-punto[1]+centro_y
    p=[xp,yp]
    return p

def Esta_Cerca(mouse,punto):
    error=10
    ls=[]
    ls.append(punto[0])
    ls.append(punto[1])
    p1=ls[0]
    p2=ls[1]
    lim_inf_x=p1-error
    lim_inf_y=p2-error
    lim_sup_x=p1+error
    lim_sup_y=p2+error
    if(((mouse[0]<=lim_sup_x)and(mouse[0]>=lim_inf_x)) and
        ((mouse[1]<=lim_sup_y)and(mouse[1]>=lim_inf_y))):
        return True
    else:
        return False


#pasar de pantalla a cartesiano
def A_Pantalla(punto):
    xp= punto[0]+centro_x
    yp= -punto[1]+centro_y
    p=[xp,yp]
    return p

#Escalar
def Escalar(punto,escala):
	xp = punto[0]*escala[0]
	yp = punto[1]*escala[1]
	p=[xp,yp]
	return p

#Rotar
def Rotar_Horario(punto,angulo):
    rad = math.radians(angulo)
    xp = punto[0]*math.cos(rad)-punto[1]*math.sin(rad)
    yp = punto[0]*math.sin(rad)+punto[1]*math.cos(rad)
    p = [xp,yp]
    return p

def Rotar_AntiHorario(punto,angulo):
    rad = math.radians(angulo)
    xp = punto[0]*math.sin(rad)+punto[1]*math.cos(rad)
    yp = -punto[0]*math.cos(rad)+punto[1]*math.sin(rad)
    p = [xp,yp]
    return p
#Trasladar
def Trasladar(punto,traslacion):
	xp=punto[0]+traslacion[0]
	yp=punto[1]+traslacion[1]
	p=[xp,yp]
	return p

#pasa unos puntos de pantalla a cartesiano
def Puntos_A_Pantalla(puntos):
	for i in range(len(puntos)):
		puntos[i] = A_Pantalla(puntos[i])

#pasa unos puntos de cartesiano a pantalla
def Puntos_A_Cartesiano(puntos):
	for i in range(len(puntos)):
		puntos[i] = A_Cartesiano(puntos[i])
	#return puntos

def Escalar_Puntos(puntos,escala):
	for i in range(len(puntos)):
		puntos[i] = Escalar(puntos[i],escala)
	#return puntos

def Trasladar_Puntos(puntos,traslacion):
	for i in range(len(puntos)):
		puntos[i] = Trasladar(puntos[i],traslacion)
    #return puntos

def Rotar_Puntos_Horario(puntos,angulo):
	for i in range(len(puntos)):
		puntos[i] = Rotar_Horario(puntos[i],angulo)
    #return puntos

def Rotar_Puntos_AntiHorario(puntos,angulo):
	for i in range(len(puntos)):
		puntos[i] = Rotar_AntiHorario(puntos[i],angulo)
    #return puntos

def colorear():
    pass
