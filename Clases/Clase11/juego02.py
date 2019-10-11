
# IMPLEMENTA COLISIONES
# IMPLEMENTA UN CONTADOR DE SALUD
# IMPLEMENTA LA DETECCION PERO NO LA ELIMINACION DE LOS RIVALES

import pygame as pg
from libreria import*
import random

class Jugador(pg.sprite.Sprite):
    """clase jugador"""
    def __init__(self,pos,v=3):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([30,30])
        self.image.fill(verde)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.vidas = v

    def update(self):
        # LIMITES DE PANTALLA PERSONAJE
        if self.rect.x > (ancho - self.rect.width):
            self.rect.x = ancho - self.rect.width
            self.velx=0
        if self.rect.x < 0:
            self.rect.x=0
            self.velx=0
        if self.rect.y > (alto - self.rect.height):
            self.rect.y = alto - self.rect.height
            self.vely=0
        if self.rect.y < 0:
            self.rect.y=0
            self.vely=0
        self.rect.x += self.velx
        self.rect.y += self.vely

    def position(self):
        pass
        return [self.rect.x,self.rect.y]

class Rival(pg.sprite.Sprite):
    """clase rival"""
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([40,40])
        self.image.fill(rojo)
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=0
        self.velx=-5
        self.vely=0
        self.tempo=random.randrange(200)

    def update(self):
        # BRASHEO DE RIVALES CONTINUO
        if self.rect.x < 0:
            self.velx= 5
        if self.rect.x > ancho - self.rect.width:
            self.velx= -5
        self.rect.x += self.velx
        self.tempo -=1


class Bala(pg.sprite.Sprite):
    """clase bala"""
    def __init__(self,pos,cl=azul):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([10,20])
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0

    def update(self):
        self.rect.x += self.velx
        self.rect.y +=self.vely


if __name__ == '__main__':

    # PANTALLA
    pg.init()
    pantalla = pg.display.set_mode([ancho,alto])
    fuente=pg.font.Font(None,32)

    # GRUPOS
    jugadores=pg.sprite.Group()
    rivales=pg.sprite.Group()
    balas=pg.sprite.Group()
    balas_r=pg.sprite.Group()

    # JUGADOR
    j=Jugador([origen[0],alto])
    jugadores.add(j)
    # RIVALES
    n=10
    for i in range(n):
        r = Rival()
        r.rect.x=random.randrange(ancho, ancho + 400)
        r.rect.y=random.randrange(alto- r.rect.height)
        rivales.add(r)
    # CONSTANTES
    salud=1000
    reloj=pg.time.Clock()
    fin_de_juego= False
    fin = False
    # CICLO PRINCIPAL
    while (not fin) and (not fin_de_juego):
        for event in pg.event.get():
            #EVENTOS
            if event.type ==pg.QUIT:
                fin = True
            #MOVIMIENTO DIRECCIONADO
            if event.type==pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    j.velx=5
                    j.vely=0
                if event.key == pg.K_LEFT:
                    j.velx=-5
                    j.vely=0
                if event.key == pg.K_DOWN:
                    j.vely=5
                    j.velx=0
                if event.key == pg.K_UP:
                    j.vely=-5
                    j.velx=0
                if event.key== pg.K_SPACE:
                    # CREAR BALA
                    b=Bala(j.rect.midtop,verde)
                    balas.add(b)
                    b.vely=-10
            if event.type==pg.KEYUP:
                if event.key != pg.K_SPACE:
                    j.velx=0
                    j.vely=0

        # CONTROL DEL SISTEMA
        # LIMITES DE PANTALLA BALA
        for b in balas:
            if b.rect.x<0 or b.rect.x>ancho or b.rect.y>alto or b.rect.y<0:
                b.remove()
        for b in balas_r:
            if b.rect.x<0 or b.rect.x>ancho or b.rect.y>alto or b.rect.y<0:
                b.remove()
        # COLISIONES
        for b in balas:
            ls =pg.sprite.spritecollide(b,rivales,True)
            for r in ls:
                balas.remove(b)
        vidas_restantes=j.vidas
        for b in balas_r:
            ls =pg.sprite.spritecollide(b,jugadores,True)
            for r in ls:
                b.remove()
                j.vidas -=1
                vidas_restantes=j.vidas
                x=j.rect.x
                y=j.rect.y
                jugadores.remove(j)
                reloj.tick(0.9)
                j=Jugador([x+100,y],vidas_restantes)
                jugadores.add(j)
                if vidas_restantes == 0:
                    fin_de_juego = True
                    if fin_de_juego:
                        f='FIN DEL JUEGO'
                        while not fin:
                            for event in pg.event.get():
                                #EVENTOS
                                if event.type ==pg.QUIT:
                                    fin = True
                            texto=fuente.render(f,True,blanco)
                            pantalla.fill(negro)
                            pantalla.blit(texto,[250,150])
                            pg.display.flip()
        # SALUD DEL JUGADOR AL TOCAR ENEMIGOS
        ls = pg.sprite.spritecollide(j,rivales,False)
        for r in ls:
            salud-=1
            print(salud)
            if salud==0:
                fin=True
        for r in rivales:
            if r.tempo <= 0:
                b = Bala(r.rect)
                b.vely=5
                balas_r.add(b)
                r.tempo=random.randrange(200)
        # REFRESCO DE PANTALLA
        jugadores.update()
        rivales.update()
        balas.update()
        balas_r.update()
        pantalla.fill(negro)
        s_vidas= "Vidas"+str(vidas_restantes)
        texto=fuente.render(s_vidas, True , blanco)
        pantalla.blit(texto,[50,10])
        jugadores.draw(pantalla)
        rivales.draw(pantalla)
        balas.draw(pantalla)
        balas_r.draw(pantalla)
        pg.display.flip()
        reloj.tick(60)
