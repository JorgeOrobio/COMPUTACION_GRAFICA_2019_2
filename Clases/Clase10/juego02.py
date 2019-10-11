import pygame as pg
from libreria import*
import random


#OJO CUIDADO VERY IMPORTANT
#ls= [1,2,3]
#for i in enumerate(ls):
#    print(i)


class Jugador(pg.sprite.Sprite):
    def __init__(self,pos):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([80,80])
        self.image.fill(verde)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=alto-self.rect.height
        self.velx=0
        self.vely=0
    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely

class Rival(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([60,60])
        self.image.fill(azul)
        self.rect=self.image.get_rect()
        self.velx=5
    def update(self):
        self.rect.x+=self.velx
        if self.rect.x > (ancho-self.rect.width):
            self.velx=-5
        if self.rect.x < 0:
            self.velx=5

if __name__ == '__main__':
    pg.init
    pantalla = pg.display.set_mode([ancho,alto])
    jugadores=pg.sprite.Group()
    rivales=pg.sprite.Group()
    reloj=pg.time.Clock()
    jugador=Jugador([100,350])
    jugadores.add(jugador)
    n=10
    for i in range(n):
        r=Rival()
        r.rect.x=random.randrange(ancho-r.rect.width)
        r.rect.y=random.randrange(alto-200)
        rivales.add(r)
    fin = False
    while not fin:
        for event in pg.event.get():
            #EVENTOS
            if event.type ==pg.QUIT:
                fin = True
            if event.type==pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    jugador.velx=5
                    jugador.vely=0
                if event.key == pg.K_LEFT:
                    jugador.velx=-5
                    jugador.vely=0
                if event.key == pg.K_DOWN:
                    jugador.vely=5
                    jugador.velx=0
                if event.key == pg.K_UP:
                    jugador.vely=-5
                    jugador.velx=0
                if event.key == pg.K_SPACE:
                    jugador.vely=0
                    jugador.velx=0
        #LIMITES DE PANTALLA
        if jugador.rect.x>(ancho-jugador.rect.width):
            jugador.rect.x= ancho-jugador.rect.width
            jugador.velx =0
        elif jugador.rect.x<0:
            jugador.rect.x=0
            jugador.velx=0
        else:
            jugador.update()
        if jugador.rect.y>(alto-jugador.rect.height):
            jugador.rect.y=alto-jugador.rect.height
            jugador.vely=0
        elif jugador.rect.y<0 :
            jugador.rect.y=0
            jugador.vely=0
        else:
            jugador.update()
        #REFRESCO DE PANTALLA

        ls=pg.sprite.spritecollide(jugador,rivales,True)
        print(ls)
        for e in ls:
            print("colision")
        jugadores.update()
        rivales.update()
        pantalla.fill(negro)
        jugadores.draw(pantalla)
        rivales.draw(pantalla)
        pg.display.flip()
        reloj.tick(30)
