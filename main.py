
import pygame
import time

from game import *
from display import *

def main():
    show_menu()
    while True:
        areajuego.fill(black)
        score = game_loop()
        time.sleep(2)
        if (score == -1):
            mensaje = "GAME OVER: GANARON LOS INVASORES!!!!"
            areajuego.fill(black)
            message_display(mensaje, 500, 500)
        else:
            mensaje = "GANASTE!!! ELIMINASTE A LOS INVASORES!!"
            mensaje2 = "EN "+str(score)+" CICLOS"
            areajuego.fill(black)
            message_display(mensaje, 500, 300)
            message_display(mensaje2, 500, 700)

        pygame.display.update()
        time.sleep(4)
        if not ask_play_again():
            break

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
