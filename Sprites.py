# Se importan las librerias a utilizar
import pygame, sys, Variables, random
from pygame import *
from Variables import *
from Network import network


# Clase de caja de texto, con esta clase se ingresa el nombre al inicar la partida
class textbox(pygame.sprite.Sprite):
	def __init__ (self):
		pygame.sprite.Sprite.__init__(self)
		self.text = ""
		self.font = pygame.font.Font(None, 50)
		self.image = self.font.render("Digite su nombre: ", True, RED)
		self.rect = self.image.get_rect()
	# Aquí se añaden los caracteres
	def add_character(self, character):
		if character in caracteresvalidos:
			self.text += character
		if character in caracteresvalidosmayus:
			self.text += character
		self.update()
	# Esta función se encarga de actualizar el texto que se ve en pantalla
	def update(self):
		old_rect_pos = self.rect.center
		self.image = self.font.render(self.text, True, RED)
		self.rect = self.image.get_rect()
		self.rect.center = old_rect_pos	


# Clase del jugador
class player(pygame.sprite.Sprite):
	def __init__(self, x, y, sheet):
		super().__init__()
		self.image = sheet
		self.x = x
		self.y = y
		self.rect = self.image.get_rect(center = (x,y))
		self.rect.x = x
		self.rect.y = y
		self.frame = 0
		self.image.set_colorkey(BLACK)
		self.speed = 5

	# Funcion para mover el jugador
	def move(self):
		self.speed_x = 0
		self.speed_y = 0
		keystate=pygame.key.get_pressed()
		if keystate[K_LEFT]:
			self.x -= 4
		if keystate[K_RIGHT]:
			self.x += 4
		if keystate[K_UP]:
			self.y -= 4
		if keystate[K_DOWN]:
			self.y += 4


		self.update()

	def update(self):
		self.rect = self.image.get_rect(center = (self.x, self.y))		
		

# Clase Dummycars
class dummycars(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = dummysheet
		self.rect = self.image.get_rect(center = (screen_width / 2, screen_height/2))
		self.frame = 0
		self.rect.x = random.randrange(10, 650)
		self.rect.y = random.randrange(-30, 10)
		self.image.set_colorkey(BLACK)
		self.speedy = 2

	# Funcion para mover los dummycars
	def update(self):
		self.rect.y += self.speedy
		if self.rect.top > screen_height:
			self.rect.y = random.randrange(-30, 10)
			self.rect.x = random.randrange(10, 650)
			self.speedy = 2

# Clase Cactus
class Cactus(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = cactussheet
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(10, 650)
		self.rect.y = random.randrange(-30, 10)
		self.frame = 0
		self.speedy = 3
		self.image.set_colorkey(BLACK)

	def update(self):
		self.rect.y += self.speedy
		if self.rect.top > screen_height:
			self.rect.y = random.randrange(-30, 10)
			self.rect.x = random.randrange(10, 650)
			self.speedy = 3


class Dummy2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = dummysheet1
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(10, 680)
		self.rect.y = random.randrange(-30, 10)
		self.speedy = 4
		self.image.set_colorkey(BLACK)

	def update(self):
		self.rect.y += self.speedy
		if self.rect.top > screen_height:
			self.rect.y = random.randrange(-30, 10)
			self.rect.x = random.randrange(10, 650)
			self.speedy = 4

class Dummy3(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = dummysheet2
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(10, 680)
		self.rect.y = random.randrange(-30, 10)
		self.speedy = 5
		self.image.set_colorkey(BLACK)

	def update(self):
		self.rect.y += self.speedy
		if self.rect.top > screen_height:
			self.rect.y = random.randrange(-30, 10)
			self.rect.x = random.randrange(10, 650)
			self.speedy = 5


class CacGod(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = cactussheet
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(10, 650)
		self.rect.y = random.randrange(-30, 10)
		self.frame = 0
		self.speedy = 7
		self.speedx = 7
		self.image.set_colorkey(BLACK)

	def update(self):
		self.rect.y += self.speedy
		self.rect.x += self.speedx
		if self.rect.top > screen_height or self.rect.left < -25 or self.rect.right > 625:
			self.rect.y = random.randrange(-30, 10)
			self.rect.x = random.randrange(10, 650)
			self.speedy = 7
			self.speedx = 7
# Caja de texto
textbox = textbox()
textbox.rect.center = (screen_width / 2, screen_height / 2)

# Jugadores
n = network()
StartPos = read_pos(n.getpos())
p = player(StartPos[0], StartPos[1], sheet)
p2 = player(350, 580, sheet2)

# Listas
all_sprites_list = pygame.sprite.Group()
players_list = pygame.sprite.Group()
p2_list = pygame.sprite.Group()
dummycars_list = pygame.sprite.Group()
cactus_list = pygame.sprite.Group()
dummy2_list = pygame.sprite.Group()
dummy3_list = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites3 = pygame.sprite.Group()
players_list.add(p)
p2_list.add(p2)

# En este apartado se crea un numero definido de dummycars o cactus
for i in range(4):
	dummy = dummycars()
	cac = Cactus()
	all_sprites_list.add(dummy)
	dummycars_list.add(dummy)
	cactus_list.add(cac)
	all_sprites_list.add(cac)

for i in range(5):
	dummy2 = Dummy2()
	cac = Cactus()
	dummy2_list.add(dummy2)
	all_sprites.add(cac, dummy2)
	cactus_list.add(cac)

for i in range(3):
	dummy3 = Dummy3()
	cac = Cactus()
	dummy3_list.add(dummy3)
	all_sprites3.add(dummy3)

for i in range(6):
	cac = CacGod()
	all_sprites3.add(cac)
	cactus_list.add(cac)

