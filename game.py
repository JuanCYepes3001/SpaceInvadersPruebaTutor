import pygame
import time
import random
from display import *

def game_loop():
    ciclos = 0
    jposx = 460
    jposy = 920

    jmovx = 0

    b1movx = 2
    b2movx = -2

    jdisparox = 100
    jdisparoy = 920

    e1 = True
    e1x = 200
    e1v = 15
    e2 = True
    e2x = 420
    e2v = 15
    e3 = True
    e3x = 640
    e3v = 15

    ey = 820

#PINTAR FONDO
    areajuego.fill(black)
#PINTAR Marco


    termino = False
    eliminado = False

    disparo = False
    disparoe1 = False
    disparoe2 = False
    disparoe3 = False
    disparoe4 = False
    ciclot1 = 20
    ciclot2 = 70
    ciclot3 = 300
    ciclot4 = 150

    disparoe1x = 0
    disparoe1y = 0
    disparoe2x = 0
    disparoe2y = 0
    disparoe3x = 0
    disparoe3y = 0
    disparoe4x = 0
    disparoe4y = 0

    while not termino:
        areajuego.fill(black)
        for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_0:
                            termino = True
                        if event.key == pygame.K_LEFT:
                            jmovx = -8
                            #print("A la izquierda")
                        elif event.key == pygame.K_RIGHT:
                            jmovx = 8
                            #print("A la derecha")
                        if event.key == pygame.K_SPACE:
                            if not disparo:
                                jdisparox = (jposx+40)
                                jdisparoy = 920
                                disparo = True
        
        #Bloque de Colisiones
        #Que el jugador no salga de la pantalla
        if (jmovx < 0):
            if (jposx + jmovx) > 1:
                jposx = jposx + jmovx
        else:
            if (jposx + jmovx) < 920:
                jposx = jposx + jmovx
        #Que los enemigos no salgan de la pantalla
        if bloquex:
            if (b1movx < 0):
                if (bloquex[0]) < 3:
                    b1movx = 2
            elif (b1movx > 0):
                if (bloquex[-1] + 100) > 997:
                    b1movx = -2
        if bloque2x:
            if (b2movx < 0):
                if (bloque2x[0]) < 3:
                    b2movx = 2
            elif (b2movx > 0):
                if (bloque2x[-1] + 100) > 997:
                    b2movx = -2
        if bloque3x:
            if (b1movx < 0):
                if (bloque3x[0]) < 3:
                    b1movx = 2
            elif (b1movx > 0):
                if (bloque3x[-1] + 100) > 997:
                    b1movx = -2
        if bloque4x:
            if (b2movx < 0):
                if (bloque4x[0]) < 3:
                    b2movx = 2
            elif (b2movx > 0):
                if (bloque4x[-1] + 100) > 997:
                    b2movx = -2

        #Que el disparo no salga de la pantalla o le pegue a un enemigo
        if disparo:
            if jdisparoy < 10:
                disparo = False
            if jdisparoy <= (bloquey+20):
                if jdisparoy >= bloquey:
                    for enemigo in bloquex:
                        if ((jdisparox+10) >= enemigo) and (jdisparox <= (enemigo+100)):
                            bloquex.remove(enemigo)
                            disparo = False
            elif jdisparoy <= (bloque2y+20):
                if jdisparoy >= bloque2y:
                    for enemigo in bloque2x:
                        if ((jdisparox+10) >= enemigo) and (jdisparox <= (enemigo+100)):
                            bloque2x.remove(enemigo)
                            disparo = False
            elif jdisparoy <= (bloque3y+20):
                if jdisparoy >= bloque3y:
                    for enemigo in bloque3x:
                        if ((jdisparox+10) >= enemigo) and (jdisparox <= (enemigo+100)):
                            bloque3x.remove(enemigo)
                            disparo = False
            elif jdisparoy <= (bloque4y+20):
                if jdisparoy >= bloque4y:
                    for enemigo in bloque4x:
                        if ((jdisparox+10) >= enemigo) and (jdisparox <= (enemigo+100)):
                            bloque4x.remove(enemigo)
                            disparo = False
            if e1:
                if (jdisparoy <= (ey+80)) and ((jdisparoy+20) >= ey):
                    if ((jdisparox+10) >= e1x) and (jdisparox <= (e1x+160)):
                        disparo = False
                        if e1v <= 0:
                            e1 = False
                        else:
                            e1v = (e1v - 1)
            if e2:
                if (jdisparoy <= (ey+80)) and ((jdisparoy+20) >= ey):
                    if ((jdisparox+10) >= e2x) and (jdisparox <= (e2x+160)):
                        disparo = False
                        if e2v <= 0:
                            e2 = False
                        else:
                            e2v = (e2v - 1)
            if e3:
                if (jdisparoy <= (ey+80)) and ((jdisparoy+20) >= ey):
                    if ((jdisparox+10) >= e3x) and (jdisparox <= (e3x+160)):
                        disparo = False
                        if e3v <= 0:
                            e3 = False
                        else:
                            e3v = (e3v - 1)

        #Si los disparos enemigos salieron de la pantalla o nos eliminaron
        if disparoe1:
            if (disparoe1y > 989):
                disparoe1 = False
                ciclot1 = ciclos + (random.randrange(1,200,10))
            if e1:
                if ((disparoe1y+20) >= ey) and (disparoe1y < (ey+80)):
                    if (((disparoe1x+10) >= e1x) and (disparoe1x <= (e1x+160))):
                        disparoe1 = False
                        if e1v <= 0:
                            e1 = False
                        else:
                            e1v = (e1v - 1)
            if e2:
                if ((disparoe1y+20) >= ey) and (disparoe1y < (ey+80)):
                    if (((disparoe1x+10) >= e2x) and (disparoe1x <= (e2x+160))):
                        disparoe1 = False
                        if e2v <= 0:
                            e2 = False
                        else:
                            e2v = (e2v - 1)
            if e3:
                if ((disparoe1y+20) >= ey) and (disparoe1y < (ey+80)):
                    if (((disparoe1x+10) >= e3x) and (disparoe1x <= (e3x+160))):
                        disparoe1 = False
                        if e3v <= 0:
                            e3 = False
                        else:
                            e3v = (e3v - 1)
            if ((disparoe1y+20) >= jposy) and (disparoe1y < (jposy+jalto)):
                if (((disparoe1x+10) >= jposx) and (disparoe1x <= (jposx+jancho))):
                    disparoe1 = False
                    termino = True
                    eliminado = True
        if disparoe2:
            if (disparoe2y > 989):
                disparoe2 = False
                ciclot2 = ciclos + (random.randrange(1,200,10))
            if e1:
                if ((disparoe2y+20) >= ey) and (disparoe2y < (ey+80)):
                    if (((disparoe2x+10) >= e1x) and (disparoe2x <= (e1x+160))):
                        disparoe2 = False
                        if e1v <= 0:
                            e1 = False
                        else:
                            e1v = (e1v - 1)
            if e2:
                if ((disparoe2y+20) >= ey) and (disparoe2y < (ey+80)):
                    if (((disparoe2x+10) >= e2x) and (disparoe2x <= (e2x+160))):
                        disparoe2 = False
                        if e2v <= 0:
                            e2 = False
                        else:
                            e2v = (e2v - 1)
            if e3:
                if ((disparoe2y+20) >= ey) and (disparoe2y < (ey+80)):
                    if (((disparoe2x+10) >= e3x) and (disparoe2x <= (e3x+160))):
                        disparoe2 = False
                        if e3v <= 0:
                            e3 = False
                        else:
                            e3v = (e3v - 1)
            if ((disparoe2y+20) >= jposy) and (disparoe2y < (jposy+jalto)):
                if (((disparoe2x+10) >= jposx) and (disparoe2x <= (jposx+jancho))):
                    disparoe2 = False
                    termino = True
                    eliminado = True
        if disparoe3:
            if (disparoe3y > 989):
                disparoe3 = False
                ciclot3 = ciclos + (random.randrange(1,200,10))
            if e1:
                if ((disparoe3y+20) >= ey) and (disparoe3y < (ey+80)):
                    if (((disparoe3x+10) >= e1x) and (disparoe3x <= (e1x+160))):
                        disparoe3 = False
                        if e1v <= 0:
                            e1 = False
                        else:
                            e1v = (e1v - 1)
            if e2:
                if ((disparoe3y+20) >= ey) and (disparoe3y < (ey+80)):
                    if (((disparoe3x+10) >= e2x) and (disparoe3x <= (e2x+160))):
                        disparoe3 = False
                        if e2v <= 0:
                            e2 = False
                        else:
                            e2v = (e2v - 1)
            if e3:
                if ((disparoe3y+20) >= ey) and (disparoe3y < (ey+80)):
                    if (((disparoe3x+10) >= e3x) and (disparoe3x <= (e3x+160))):
                        disparoe3 = False
                        if e3v <= 0:
                            e3 = False
                        else:
                            e3v = (e3v - 1)
            if ((disparoe3y+20) >= jposy) and (disparoe3y < (jposy+jalto)):
                if (((disparoe3x+10) >= jposx) and (disparoe3x <= (jposx+jancho))):
                    disparoe3 = False
                    termino = True
                    eliminado = True
        if disparoe4:
            if (disparoe4y > 989):
                disparoe4 = False
                ciclot4 = ciclos + (random.randrange(1,200,10))
            if e1:
                if ((disparoe4y+20) >= ey) and (disparoe4y < (ey+80)):
                    if (((disparoe4x+10) >= e1x) and (disparoe4x <= (e1x+160))):
                        disparoe4 = False
                        if e1v <= 0:
                            e1 = False
                        else:
                            e1v = (e1v - 1)
            if e2:
                if ((disparoe4y+20) >= ey) and (disparoe4y < (ey+80)):
                    if (((disparoe4x+10) >= e2x) and (disparoe4x <= (e2x+160))):
                        disparoe4 = False
                        if e2v <= 0:
                            e2 = False
                        else:
                            e2v = (e2v - 1)
            if e3:
                if ((disparoe4y+20) >= ey) and (disparoe4y < (ey+80)):
                    if (((disparoe4x+10) >= e3x) and (disparoe4x <= (e3x+160))):
                        disparoe4 = False
                        if e3v <= 0:
                            e3 = False
                        else:
                            e3v = (e3v - 1)
            if ((disparoe4y+20) >= jposy) and (disparoe4y < (jposy+jalto)):
                if (((disparoe4x+10) >= jposx) and (disparoe4x <= (jposx+jancho))):
                    disparoe4 = False
                    termino = True
                    eliminado = True


        #Bloque de Movimientos
        if disparo:
            jdisparoy = (jdisparoy-10)
        if disparoe1:
            disparoe1y = (disparoe1y+10)
        if disparoe2:
            disparoe2y = (disparoe2y+10)
        if disparoe3:
            disparoe3y = (disparoe3y+10)
        if disparoe4:
            disparoe4y = (disparoe4y+10)

        if bloquex:
            for x in range(0,len(bloquex)):
                bloquex[x] = (bloquex[x] + b1movx)
        if bloque2x:
            for x in range(0,len(bloque2x)):
                bloque2x[x] = (bloque2x[x] + b2movx)
        if bloque3x:
            for x in range(0,len(bloque3x)):
                bloque3x[x] = (bloque3x[x] + b1movx)
        if bloque4x:
            for x in range(0,len(bloque4x)):
                bloque4x[x] = (bloque4x[x] + b2movx)

        #Edificios?
        if e1:
            areajuego.blit(barrera,(e1x,ey))
        if e2:
            areajuego.blit(barrera,(e2x,ey))
        if e3:
            areajuego.blit(barrera,(e3x,ey))

        #Los Invaders
        for b in bloquex:
            areajuego.blit(invader,(b,bloquey))

        for b2 in bloque2x:
            areajuego.blit(invader,(b2,bloque2y))

        for b3 in bloque3x:
            areajuego.blit(invader,(b3,bloque3y))

        for b4 in bloque4x:
            areajuego.blit(invader,(b4,bloque4y))

        if bloquex:
            if not disparoe1:
                if ciclos > ciclot1:
                    disparoe1 = True
                    if len(bloquex) >= 2:
                        disparoe1x = (bloquex[random.randrange(0,(len(bloquex)-1),1)] + 50)
                    else:
                        disparoex = bloquex[-1]
                    disparoe1y = bloquey
        if bloque2x:
            if not disparoe2:
                if ciclos > ciclot2:
                    disparoe2 = True
                    if len(bloque2x) >= 2:
                        disparoe2x = (bloque2x[random.randrange(0,(len(bloque2x)-1),1)] + 50)
                    else:
                        disparoe2x = bloque2x[-1]
                    disparoe2y = bloque2y
        if bloque3x:
            if not disparoe3:
                if ciclos > ciclot3:
                    disparoe3 = True
                    if len(bloque3x) >= 2:
                        disparoe3x = (bloque3x[random.randrange(0,(len(bloque3x)-1),1)] + 50)
                    else:
                        disparoe3x = bloque3x[-1]
                    disparoe3y = bloque3y
        if bloque4x:
            if not disparoe4:
                if ciclos > ciclot4:
                    disparoe4 = True
                    if len(bloque4x) >= 2:
                        disparoe4x = (bloque4x[random.randrange(0,(len(bloque4x)-1),1)] + 50)
                    else:
                        disparoe4x = bloque4x[-1]
                    disparoe4y = bloque4y
                    

        #El Rasho Laser
        #pygame.draw.rect(areajuego, white, [jposx, jposy, jancho, jalto])
        areajuego.blit(LaserImg,(jposx,jposy))

        #Los tiros del Jugador
        if disparo:
            pygame.draw.rect(areajuego, rojo, [jdisparox, jdisparoy, 10, 20])

        #Los disparos de los enemigos
        if disparoe1:
            pygame.draw.rect(areajuego, (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)), [disparoe1x, disparoe1y, 10, 20])
        if disparoe2:
            pygame.draw.rect(areajuego, (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)), [disparoe2x, disparoe2y, 10, 20])
        if disparoe3:
            pygame.draw.rect(areajuego, (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)), [disparoe3x, disparoe3y, 10, 20])
        if disparoe4:
            pygame.draw.rect(areajuego, (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)), [disparoe4x, disparoe4y, 10, 20])
        
        #Mostrar Score arriba
        message_display("Ciclos utilizados: "+str(ciclos),400,20)

        #Mostrar todo
        pygame.display.update()
        florderelos.tick(60)
        ciclos = ciclos+1

        if not bloquex and not bloque2x and not bloque3x and not bloque4x:
            termino = True
    if eliminado:
        ciclos = -1

    return ciclos
