#! /usr/bin/env python
import os, random, sys, math
import pygame
from pygame.locals import *
from configuracion import *
from extras import *
from funcionesSeparador import *
from funcionesVACIAS import *
pygame.init() ## ---- INICIAMOS PYGAME. ---- ##

# ---- FUNCIONES PRINCIPALES. ---- #

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Juego de las silabas")

BG = pygame.image.load("imagenes/background.jpg")

def get_font(size):
    return pygame.font.Font("assets/Neon.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(juegoOriginal())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
        pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        OPTIONS_DIFICULTAD = Button(image=None, pos=(617, 100),
                            text_input="DIFICULTAD", font=get_font(80), base_color="White", hovering_color="Black")
        OPTIONS_DIFICULTAD.update(SCREEN)

        OPTIONS_DIFICULTAD = Button(image=None, pos=(619, 101),
                            text_input="DIFICULTAD", font=get_font(80), base_color="Black", hovering_color="Black")
        OPTIONS_DIFICULTAD.update(SCREEN)

        OPTIONS_FACIL = Button(image=None, pos=(602, 220),
                            text_input="FACIL", font=get_font(80), base_color="White", hovering_color="Black")
        OPTIONS_FACIL.update(SCREEN)

        OPTIONS_MEDIO = Button(image=None, pos=(626, 322),
                            text_input="MEDIO", font=get_font(80), base_color="White", hovering_color="Black")
        OPTIONS_MEDIO.update(SCREEN)

        OPTIONS_DIFICIL = Button(image=None, pos=(629, 424),
                            text_input="DIFICIL", font=get_font(80), base_color="White", hovering_color="Black")
        OPTIONS_DIFICIL.update(SCREEN)

        OPTIONS_VOLVER= Button(image=None, pos=(618, 570),
                            text_input="VOLVER", font=get_font(75), base_color="White", hovering_color="Green")
        OPTIONS_VOLVER.update(SCREEN)

        OPTIONS_FACIL = Button(image=None, pos=(600, 220),
                            text_input="FACIL", font=get_font(80), base_color="Green", hovering_color="Black")
        OPTIONS_FACIL.update(SCREEN)

        OPTIONS_MEDIO = Button(image=None, pos=(622, 322),
                            text_input="MEDIO", font=get_font(80), base_color="Yellow", hovering_color="Black")
        OPTIONS_MEDIO.update(SCREEN)

        OPTIONS_DIFICIL = Button(image=None, pos=(627, 424),
                            text_input="DIFICIL", font=get_font(80), base_color="Red", hovering_color="Black")
        OPTIONS_DIFICIL.update(SCREEN)

        OPTIONS_VOLVER= Button(image=None, pos=(620, 570),
                            text_input="VOLVER", font=get_font(75), base_color="Black", hovering_color="Green")
        OPTIONS_VOLVER.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_VOLVER.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_FACIL.checkForInput(OPTIONS_MOUSE_POS):
                    juegoFacil()
                if OPTIONS_MEDIO.checkForInput(OPTIONS_MOUSE_POS):
                    juegoMedio()
                if OPTIONS_DIFICIL.checkForInput(OPTIONS_MOUSE_POS):
                    juegoDificil()
        pygame.display.update()

def main_menu():
    while True:
        icono = pygame.image.load("imagenes/icon.png")
        pygame.display.set_icon(icono)

        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MENU PRINCIPAL", True, "#000000")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                            text_input="JUGAR", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                            text_input="OPCIONES", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                            text_input="SALIR", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

def juegoOriginal():
    pygame.display.update()
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.mixer.init()
    # ---- SONIDOS. ---- #
    sonidoCorrecto = pygame.mixer.Sound("sonidos/correcto.wav")
    sonidoIncorrecto = pygame.mixer.Sound("sonidos/incorrecto.wav")
    sonidoGanaste = pygame.mixer.Sound("sonidos/ganasteJuego.wav")
    sonidoPerdiste = pygame.mixer.Sound("sonidos/perdisteJuego.wav")
    pygame.mixer.music.set_volume(1.0)
    # ---- FONDO. ---- #
    background = pygame.image.load("imagenes/fondo.jpg")
    pantalla = pygame.display.set_mode((1280, 720))
    # ---- PREPARAMOS LA VENTANA. ---- #
    pygame.display.set_caption("Juego de las silabas")
    screen = pygame.display.set_mode((ANCHO, ALTO))
    # ---- TIEMPO TOTAL DEL JUEGO. ---- #
    gameClock = pygame.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    tInicio = pygame.time.get_ticks()/1000
    fps = FPS_inicial
    puntos = 0
    palabra = ""
    lemarioEnSilabas=[]
    listaPalabrasDiccionario=[]
    ingreseRespuesta = "Ingrese la respuesta:"
    archivo = open("lemario.txt","r", encoding="latin1")
    # ---- LLAMAMOS A LA FUNCION PARA LEER EL ARCHIVO. ---- #
    lectura(archivo, listaPalabrasDiccionario)
    # ---- LLAMAMOS A LA FUNCION PARA ELEJIR UNA PALABRA AL AZAR. ---- #
    palabraEnPantalla = nuevaPalabra(listaPalabrasDiccionario)
    palabraEnPantallaAnterior=""
    dibujar(screen,ingreseRespuesta,palabra,palabraEnPantalla,puntos,segundos)
    # ---- EMPIEZA EL JUEGO. ---- #
    while segundos > fps/1000:
        # ---- 1 FRAME CADA 1/FPS SEGUNDOS. ---- #
            gameClock.tick(fps)
            totaltime += gameClock.get_time()
            if True:
                fps = 60
            for e in pygame.event.get():
                # ---- NOS FIJAMOS SI EL JUGADOR CIERRA LA VENTANA. ---- #
                if e.type == QUIT:
                    pygame.quit()
                    return()
                # ---- NOS FIJAMOS SI EL JUGADOR INGRESO ALGUNA LETRA. ---- #
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    palabra += letra ## PALABRA ES LA LETRA INGRESADA POR EL USUARIO. ##
                    if e.key == K_BACKSPACE:
                        palabra = palabra[0:len(palabra)-1]
                    if e.key == K_RETURN:
                        # ---- PASAMOS LA PALABRA A SILABAS. ---- #
                        palabraEnPantallaEnSilabas=palabraTOsilaba(palabraEnPantalla)
                        # ---- ENTRA SI ES CORRECTA. ---- #
                        if esCorrecta(palabraEnPantallaEnSilabas, palabra):
                            pygame.mixer.Sound.play(sonidoCorrecto)
                            puntos += 4
                            if puntaje(palabraEnPantallaEnSilabas):
                                puntos += 6
                        else:
                            pygame.mixer.Sound.play(sonidoIncorrecto)
                            puntos -= 4
                        # ---- BUSCAMOS UNA NUEVA PALABRA. ---- #
                        palabraEnPantalla=nuevaPalabra(listaPalabrasDiccionario)
                        palabra = ""
            segundos = tInicio + TIEMPO_MAX - pygame.time.get_ticks()/1000
            # ---- LIMPIAMOS LA PANTALLA ANTERIOR. ---- #
            screen.blit(background,[0,0])
            # ---- DIBUJAMOS TODO DE NUEVO. ---- #
            dibujar(screen,ingreseRespuesta,palabra,palabraEnPantalla,puntos,segundos)
            pygame.display.flip()
    while 1:
        if (TIEMPO_MAX - pygame.time.get_ticks()/1000) == 0 and puntos < 0:
            pygame.mixer.Sound.play(sonidoPerdiste)
        if (TIEMPO_MAX - pygame.time.get_ticks()/1000) == 0 and puntos > 0:
            pygame.mixer.Sound.play(sonidoGanaste)
            # ---- ESPERAMOS QUE EL USUARIO QUITEE. ---- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_VOLVER.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
    archivo.close()

# ---- EJECUTAMOS EL PROGRAMA PRINCIPAL. ---- #
if __name__ == "__main__":
    main_menu()

