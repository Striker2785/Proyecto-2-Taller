# Se importan las librerias a utilizar
import pygame
from pygame import *
pygame.init()

# Variables generales
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PyDakarDeath")
clock = pygame.time.Clock()
caracteresvalidos = "abcdefghijklmnñopqrstuvwxyz"
caracteresvalidosmayus = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
shield = 0
time = 0
score = 0
timer = 3600
timer2 = 3600
timer3 = 3600

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 50, 0)
BlUE = (0, 0, 255)
LIGHT = (170, 170, 170)
DARK = (100, 100, 100)
MAGENTA = (255, 0, 255)
light_green =(1, 254, 0)

# Esta funcion se encarga de leer la posicion de los jugadores y la decodifica
def read_pos(str):  
	str = str.split(",")
	return int(str[0]), int(str[1])
# Esta funcion se encarga de convertir la posisicion de los jugadores a una tupla.
def make_pos(tup):
	return str(tup[0]) + " , " + str(tup[1])

# Funcion para escribir
def draw_text(surface, text, size, x, y):
	font = pygame.font.SysFont("freesansbold.ttf", size)
	text_surface = font.render(text, True, RED)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x,y)
	surface.blit(text_surface, text_rect)

# Fondos
desierto = pygame.image.load("Fondos/Desierto.png")
name = pygame.image.load("Fondos/name.jpg").convert()
main = pygame.image.load("Fondos/main(1).jpg").convert()

# Sprites para los carros
sheet = pygame.image.load("Assets/player1(1).png").convert()
sheet2 = pygame.image.load("Assets/player2(2).png").convert()
dummysheet = pygame.image.load("Assets/player3(3).png").convert()
dummysheet1 = pygame.image.load("Assets/player4(1).png")
dummysheet2 = pygame.image.load("Assets/player5(1).png")
cactussheet = pygame.image.load("Assets/Cactus(4).png").convert()

# Sonidos
btn_sound = pygame.mixer.Sound("Sonidos/button.wav")
pygame.mixer.music.set_volume(0.03)
pygame.mixer.music.load("Sonidos/theme.wav")
pygame.mixer.music.play(loops=-1)


