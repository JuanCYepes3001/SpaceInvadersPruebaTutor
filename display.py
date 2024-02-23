
import pygame

pygame.init()
player1 = 1000
player2 = 1000
areajuego = pygame.display.set_mode((player1, player2))
pygame.display.set_caption('Invaders Must Die')
black = (0, 0, 0)
white = (255, 255, 255)
rojo = (255, 0, 0)
jancho = 80
jalto = 80

eancho = 200 
ealto = 80

bloquey = 100
bloque2y = 300
bloque3y = 500
bloque4y = 700

bloquex = [100,300,500,700]
bloque2x = [100,300,500,700]
bloque3x = [100,300,500,700]
bloque4x = [100,300,500,700]


LaserImg = pygame.image.load('laser.png')
barrera = pygame.image.load('proteccion.jpg')
invader = pygame.image.load('invader1.png')

florderelos = pygame.time.Clock()
def text_objects(text,font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
def message_display(text, x, y):
    largetext = pygame.font.Font('freesansbold.ttf', 40)
    TextSurf, TextRect = text_objects(text, largetext)
    TextRect.center = (x, y)
    areajuego.blit(TextSurf, TextRect)
def show_menu():
    areajuego.fill(black)
    mensaje = "Bienvenido a Invaders Must Die!"
    mensaje2 = "Presiona Enter para empezar"
    message_display(mensaje, 500, 300)
    message_display(mensaje2, 500, 700)
    pygame.display.update()
    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting_for_key = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

def ask_play_again():
    mensaje = "¿Quieres jugar de nuevo? (Sí: Enter / No: Esc)"
    message_display(mensaje, 500, 700)
    pygame.display.update()
    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                elif event.key == pygame.K_ESCAPE:
                    return False
# Resto del código relacionado con funciones de pantalla y dibujo
