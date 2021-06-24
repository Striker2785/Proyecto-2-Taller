# Se importan las librerias a utilizar
import socket, pygame, sys, Sprites, Variables, os, subprocess, json
from Sprites import *
from Variables import *
from pygame import *
from Network import network
pygame.init()

nombre = textbox.text

# Esta clase se va a encargar de ir cambiando entre los diferentes menus				
class Game_State():
	def __init__(self):	
		super().__init__()
		self.state = 'enter_name' # Esta es la pantalla que se despliega al inicio del juego

	# En esta pantalla se ingresa el nombre del jugador
	def enter_name(self):
		for event in pygame.event.get(): # Con este for se obtienen todos los eventos que sucedan
			if event.type == pygame.QUIT: # Si el evento detectado es presionar la x el juego se cierra
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN: # Con este if se detecta si el tipo de evento es presionar una tecla
				btn_sound.play() 
				textbox.add_character(pygame.key.name(event.key)) # Aquí se añaden los caracteres a la pantalla
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
				if event.key == K_SPACE:
					textbox.text += " "
					textbox.update()
				if event.key == K_BACKSPACE:
					textbox.text = textbox.text[:-1]
					textbox.update()
				if event.key == K_RETURN:
					if len(textbox.text) > 0:
						btn_sound.play() # esto reproduce el sonido del boton
						self.state = 'menu' # Cuando se presiona espacio el self.state cambia a 'menu' y se despliega el menu principal
						
		nombre = textbox.text	
		screen.blit(name, [0,0]) # con esto se imprime el fondo de la pantalla
		screen.blit(textbox.image, textbox.rect) # Esta parte se encarga de dibujar el cuadro de texto
		pygame.display.flip() # Esta parte actualiza la pantalla
		
	# Esta pantalla corresponde al menu principal del juego					
	def menu(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
				if event.key == K_1:
					btn_sound.play()
					self.state = 'main_game'
				if event.key == K_2:
					btn_sound.play()
					try: # Con el try se prueba si existe un archivo con este nombre en caso de no existir lo crea
					    with open("clicker_score.txt") as score_file: # Se abre el archivo en el que se guardaran los puntajes
					        score = json.load(score_file)
					except:
					    print("No file created yet")
				if event.key == K_3:
					btn_sound.play()
					self.state = 'instrucciones'
		screen.blit(main, [0,0])
		draw_text(screen, "pyDakarDeath", 65, screen_width // 2, screen_height // 4 - 100) # Esta parte escribe un texto en lo alto de la pantalla
		draw_text(screen, "(1)Nueva Partida", 28, screen_width // 2, screen_height // 2 + 32)
		draw_text(screen, "(2)Cargar Partida", 28, screen_width // 2, screen_height // 2 +32*2)
		draw_text(screen, "(3)Instrucciones", 28, screen_width // 2, screen_width // 2 - 5)
		pygame.display.flip()	


	def main_game(self):
		global score, timer
		timer -= 1 
		p2Pos = read_pos(n.send(make_pos((p.x, p.y)))) # esta variable crea la posicion del jugador 2
		p2.x = p2Pos[0]
		p2.y = p2Pos[1]
		hits = pygame.sprite.groupcollide(players_list, dummycars_list, False, True) # Esta variable se encarga de detectar las colisiones entre objetos
		hits1 = pygame.sprite.groupcollide(p2_list, dummycars_list, False, True)
		hits2 = pygame.sprite.groupcollide(cactus_list, players_list, True, False)
		for hit in hits: # cuando colisionan los objetos estos vuelven a ser agregados a las listas
			dummy = dummycars()
			all_sprites_list.add(dummy)
			dummycars_list.add(dummy)
		for hit in hits1:
			dummy = dummycars()
			all_sprites_list.add(dummy)
			dummycars_list.add(dummy)
		for hit in hits2:
			cac = Cactus()
			all_sprites_list.add(cac)
			cactus_list.add(cac)
		if hits or hits1: 
			score += 1
		if hits2: # en el caso de que el jugador colisione con un cactus el timer se reiniciara 
			timer = 3600
			score -= 1
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_RETURN:
					btn_sound.play()
					self.state = 'pausa'
		print(timer)
		if timer <= 0:
			self.state = 'lvl2'
				
						
		screen.blit(desierto, [0,0])
		players_list.draw(screen)
		p2_list.draw(screen)
		all_sprites_list.draw(screen)
		screen.blit(p.image, p.rect)
		screen.blit(p2.image, p2.rect)
		p.move()
		p2.update()
		draw_text(screen, str(score), 35, screen_width // 2, 10)	
		all_sprites_list.update()
		pygame.display.flip()

	def lvl2(self):
		global score, timer2 
		timer2 -= 1
		p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
		p2.x = p2Pos[0]
		p2.y = p2Pos[1]
		hits = pygame.sprite.groupcollide(players_list, dummy2_list, False, True)
		hits2 = pygame.sprite.groupcollide(cactus_list, players_list, True, False)
		for hit in hits:
			dummy2 = Dummy2()
			all_sprites.add(dummy2)
			dummy2_list.add(dummy2)
		for hit in hits2:
			cac = Cactus()
			all_sprites.add(cac)
			cactus_list.add(cac)
		if hits:
			score += 1
		if hits2:
			score -= 1
			timer2 = 3600
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_RETURN:
					btn_sound.play()
					self.state = 'pausa'
		print(timer2)
		screen.blit(desierto, [0,0])
		players_list.draw(screen)
		p2_list.draw(screen)
		all_sprites.draw(screen)
		screen.blit(p.image, p.rect)
		screen.blit(p2.image, p2.rect)
		draw_text(screen, str(score), 35, screen_width // 2, 10)	
		p.move()
		p2.update()	
		all_sprites.update()
		pygame.display.flip()
		if timer2 <= 0:
			self.state = 'lvl3'


	def lvl3(self):
		global score, timer3, nombre
		timer3 -= 1
		p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
		p2.x = p2Pos[0]
		p2.y = p2Pos[1]
		hits = pygame.sprite.groupcollide(players_list, dummy3_list, False, True)
		hits2 = pygame.sprite.groupcollide(cactus_list, players_list, True, False)
		for hit in hits:
			dummy3 = Dummy3()
			all_sprites3.add(dummy3)
			dummy3_list.add(dummy3)
		for hit in hits2:
			cac = Cactus()
			all_sprites3.add(cac)
			cactus_list.add(cac)
		if hits:
			score += 1
		if hits2:
			score -= 1
			timer3 = 3600
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_RETURN:
					btn_sound.play()
					self.state = 'pausa'
		print(timer3)
		screen.blit(desierto, [0,0])
		players_list.draw(screen)
		p2_list.draw(screen)
		all_sprites3.draw(screen)
		screen.blit(p.image, p.rect)
		screen.blit(p2.image, p2.rect)
		draw_text(screen, str(score), 35, screen_width // 2, 10)	
		p.move()
		p2.update()	
		all_sprites3.update()
		pygame.display.flip()
		if timer3 <= 0:
			nombre = textbox.text
			self.state = 'scores'
			with open("Click_score.txt","a") as score_file:
				if score < 10:
					score = str("00"+str(score))
				elif score < 100:
					score = str("0"+str(score))
				else: pass
				json.dump(str(score),score_file)
				score_file.write(' '+nombre+'\n')

	def instrucciones(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					btn_sound.play()
					self.state = 'menu'
		screen.blit(main, [0,0])
		draw_text(screen, "Instrucciones", 65, screen_width // 2, 50)
		draw_text(screen, "Para moverse utilice las flechas del teclado", 28, (screen_width // 2), (screen_height // 2 + 32*2))
		draw_text(screen, "Para volver al menu de inicio presione la tecla ESC", 28, screen_width // 2, screen_width // 2 + 32)
		draw_text(screen, "Para salir del juego pulse la x o bien presione la tecla ESC", 28, screen_width // 2, screen_height // 2+32*3)
		pygame.display.flip()

	def pausa(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					btn_sound.play()
					self.state = 'main_game'
				if event.key == K_1:
					btn_sound.play()
					self.state = 'main_game'
				if event.key == K_2:
					btn_sound.play()
					with open("Clicker_score.txt","w") as score_file:
					    json.dump(score,score_file)
				if event.key == K_3:
					btn_sound.play()
					self.state = 'menu'
		screen.blit(main, [0,0])
		draw_text(screen, "Pausa", 65, screen_width // 2, screen_height // 4 - 100)
		draw_text(screen, "(1)Reanudar", 28, screen_width // 2, screen_height // 2 + 32)
		draw_text(screen, "(2)Guardar Partida", 28, screen_width // 2, screen_height // 2 +32*2)
		draw_text(screen, "(3)Menu principal", 28, screen_width // 2, screen_width // 2 - 5)
		pygame.display.flip()			

	def Scores(self):
		with open("Click_score.txt","r") as file:
			rf = file.readlines()
			sorD = sorted(rf,reverse=True)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					btn_sound.play()
					pygame.quit()
					sys.exit()
		screen.blit(main, [0,0])
		draw_text(screen, "Scores", 65, screen_width // 2, screen_height // 4 - 100)
		draw_text(screen, "(1)"+" "+sorD[0], 28, screen_width // 2, screen_height // 2 + 32)
		draw_text(screen, "(2)"+" "+sorD[1], 28, screen_width // 2, screen_height // 2 + 32*2)
		draw_text(screen, "(3)"+" "+sorD[2], 28, screen_width // 2, screen_height // 2 +32*3)
		draw_text(screen, "(4)"+" "+sorD[3], 28, screen_width // 2, screen_height // 2 + 32*4)
		draw_text(screen, "(5)"+" "+sorD[4], 28, screen_width // 2, screen_height // 2 + 32*5)
		pygame.display.flip()

	def StateManager(self):
		if self.state == 'main_game':
			self.main_game()
		if self.state == 'enter_name':
			self.enter_name()
		if self.state == 'menu':
			self.menu()
		if self.state == 'instrucciones':
			self.instrucciones()
		if self.state == 'pausa':
			self.pausa()
		if self.state == 'lvl2':
			self.lvl2()
		if self.state == 'lvl3':
			self.lvl3()
		if self.state == 'scores':
			self.Scores()


gamestate = Game_State()
while True:
	gamestate.StateManager()
	clock.tick(60)




