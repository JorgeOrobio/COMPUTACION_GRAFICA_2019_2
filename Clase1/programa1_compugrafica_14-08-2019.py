import pygame as pg

print ('\n\n hola bebe, se que contigo no sirve la labia \n')
a=12
b=2.5
c=a+b
print c

pg.init()
pantalla=pg.display.set_mode([600,300])
pg.display.flip()
# fin = False
# while not fin:
#    a= a+1
#    if a>1000:
#        fin = True
fin = False
while not fin:
    event=pg.event.get()
    for e in event:
        if e.type == pg.QUIT:
            fin = True
