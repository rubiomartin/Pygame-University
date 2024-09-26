import pygame
from funcionesVACIAS import *
from pygame.locals import *
from configuracion import *


def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

def dibujar(screen, ingreseRespuesta, palabraUsuario, palabraActual, puntos, segundos):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontMedio= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_MEDIO)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)
    defaultFontPalabraUsuario= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_USUARIO)
    # ---- DIBUJAMOS UNA LINEA RECTA. ---- #
    pygame.draw.rect(screen, (0,0,0), [0,ALTO-110, ANCHO+110, ALTO-110], 0)
    # ---- INGRESAMOS EL TEXTO "Ingrese la respuesta:" .---- #
    screen.blit(defaultFontMedio.render(ingreseRespuesta, 10, COLOR_PALABRA), (443,568))
    screen.blit(defaultFontMedio.render(ingreseRespuesta, 10, COLOR_TEXTO), (440, 568))
    # ---- MUESTRA LO QUE ESCRIBE EL JUGADOR ---- #
    screen.blit(defaultFontPalabraUsuario.render(palabraUsuario, 10, COLOR_TEXTO), (560, 650))
    # ---- EL COLOR DEL PUNTAJE CAMBIA DEPENDIENDO DE SU PUNTUACION. ---- #
    if(puntos>=1):
        screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_GREEN), (1138, 10))
    if(puntos==0):
        screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_WHITE), (1138, 10))
    if(puntos<0):
        screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_RED), (1138, 10))
    # ---- MUESTRA LOS SEGUNDOS Y CON LA APROXIMIDADA AL 0 CAMBIA AL ROJO. ---- #
    if(segundos<30):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_YELLOW)
        if(segundos<15):
            ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_RED)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_GREEN)
    screen.blit(ren, (10, 10))
    # ---- MUESTRA LA PALABRA. ---- #
    screen.blit(defaultFontGrande.render(palabraActual, 1, COLOR_PALABRA), (ANCHO//2-(len(palabraActual))*TAMANNO_LETRA_GRANDE//3.9,ALTO-480))
    screen.blit(defaultFontGrande.render(palabraActual, 1, COLOR_WHITE), (ANCHO//2-(len(palabraActual))*TAMANNO_LETRA_GRANDE//4,ALTO-480))

screen = pygame.display.set_mode([1280, 720])
clock = pygame.time.Clock()

def facil(lista): #Esta funcion es la misma que nuevaPalabra pero elije palabras faciles.
    azar = random.choice(lista)
    while "ñ" in azar or len(azar)>5:
        azar = random.choice(lista)
    return azar

def medio(lista): #Esta funcion es la misma que nuevaPalabra pero elije palabras .
    azar = random.choice(lista)
    while "ñ" in azar or (len(azar)>9 or len(azar)<5):
        azar = random.choice(lista)
    return azar

def dificil(lista): #Esta funcion es la misma que nuevaPalabra pero elije palabras dificiles.
    azar = random.choice(lista)
    while "ñ" in azar or (len(azar)<10):
        azar = random.choice(lista)
    return azar

def juegoFacil():
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
    pygame.display.set_caption("Bienvenido al juego de las silabas:")
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
    palabraEnPantalla = facil(listaPalabrasDiccionario)
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
                        palabraEnPantalla=facil(listaPalabrasDiccionario)
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
        for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return
    archivo.close()

def juegoMedio():
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
    pygame.display.set_caption("Bienvenido al juego de las silabas:")
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
    palabraEnPantalla = medio(listaPalabrasDiccionario)
    palabraEnPantallaAnterior=""
    dibujar(screen,ingreseRespuesta,palabra,palabraEnPantalla,puntos,segundos)
    # ---- EMPIEZA EL JUEGO ---- #
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
                        # ---- PASAMOS LA PALABRA A SILABAS.---- #
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
                        palabraEnPantalla=medio(listaPalabrasDiccionario)
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
        for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return
    archivo.close()

def juegoDificil():
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
    pygame.display.set_caption("Bienvenido al juego de las silabas:")
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
    palabraEnPantalla = dificil(listaPalabrasDiccionario)
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
                        palabraEnPantalla=dificil(listaPalabrasDiccionario)
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
        for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return
    archivo.close()

