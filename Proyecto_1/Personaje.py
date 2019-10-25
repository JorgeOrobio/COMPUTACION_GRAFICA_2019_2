class Jugador(pg.sprite.Sprite):
    """clase jugador"""
    def __init__(self,archivo):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(archivo)
        self.rect=self.image.get_rect()
        self.rect.angulo=centro_x
        self.rect.radio=centro_y
        self.disparo=self.rect.midtop
        self.velrad=0
        self.velang=0
        self.vidas = 10

    def update(self):
        # LIMITES DE PANTALLA PERSONAJE
        if self.rect.angulo > (ancho - self.rect.width):
            self.rect.angulo = ancho - self.rect.width
            self.velang=0
        if self.rect.angulo < 0:
            self.rect.angulo=0
            self.velang=0
        if self.rect.radio > (alto - self.rect.height):
            self.rect.radio = alto - self.rect.height
            self.velrad=0
        if self.rect.radio < 0:
            self.rect.radio=0
            self.velrad=0

        self.image=pg.transform.rotate(self.image,self.rect.angulo)
        self.disparo=Rotar_AntiHorario(self.disparo,self.rect.angulo)
        # CAMBIAR EL MOD DEL RADIO PARA CORREGIR EL AVANCE DE LA NAVE
        self.rect.radio += self.velrad

    def position(self):
        pass
        return [self.rect.angulo,self.rect.radio]
