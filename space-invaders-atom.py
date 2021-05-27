#! /usr/bin/env python
import pygame
import random
import math
from pygame import mixer
import time


pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("space invaders")
icon = pygame.image.load("rocket.png")
pygame.display.set_icon(icon)

glvl = 1
#target text
T_font = pygame.font.Font('freesansbold.ttf', 32)
Targets = 10
#level text
level = 1
L_font = pygame.font.Font('freesansbold.ttf', 80)

by_change = 0

#coins
coins = 450
C_font = pygame.font.Font('freesansbold.ttf', 32)

#bullet speed 2x button
inc_speed = pygame.image.load("2x speed.png")


#no.of enemies text
num_enemy = 6
E_font = pygame.font.Font('freesansbold.ttf', 60)

background = pygame.image.load("background.png")

#screen = pygame.display.set_mode((800, 600))

def lvl1():
	global b_state
	global glvl
	global level
	global num_enemy
	global Targets
	global by_change
	global coins

	bg = pygame.image.load("background.png")

	mixer.music.load("background.wav")
	mixer.music.play(-1)

	#player
	pimg = pygame.image.load("space-invaders.png")
	Px = 370
	Py = 480
	Px_change = 0

	#enemy
	eimg = []
	ex = []
	ey = []
	ex_change = []
	ey_change = []
	num_of_enemies = 6

	for i in range(num_of_enemies):
		eimg.append(pygame.image.load("alien (1).png"))
		ex.append(random.randint(0, 736))
		ey.append(random.randint(50, 150))
		ex_change.append(2)
		ey_change.append(50)

	#bullet
	bimg = pygame.image.load("bullet.png")
	bx = 0
	by = 480
	bx_change = 0
	by_change += 10
	b_state = "ready"

	#score
	score_value = 0
	font = pygame.font.Font('freesansbold.ttf', 32)

	over_font = pygame.font.Font('freesansbold.ttf', 64)

	textx = 10
	texty = 10


	def show_score(x, y):
		score = font.render("score : "+ str(score_value), True, (0,225,0))
		screen.blit(score, (x, y))

	def show_target(x, y):
		target= T_font.render("target : "+ str(Targets), True, (0,225,0))
		screen.blit(target, (x, y))

	def show_coins(x, y):
		coin_draw = C_font.render("Coins : "+ str(coins), True, (0,225,0))
		screen.blit(coin_draw, (x, y))

	def game_over_text():
		over_text = over_font.render("GAMEOVER", True, (0,225,0))
		screen.blit(over_text, (200, 250))

	def player(x,y):
		screen.blit(pimg, (x, y))

	def enemy(x,y,i):
		screen.blit(eimg[i], (x, y))

	def fire(x, y):
		global b_state
		b_state = "fire"
		screen.blit(bimg, (x+16, y+10))

	def collision(ex, ey, bx, by):
		distance = math.sqrt((math.pow(ex-bx,2)) + (math.pow(ey-by,2)))
		if distance <= 27:
			return True
		else:
			return False

	running = True
	while running:
		screen.fill((0, 0, 0))

		screen.blit(bg,(0,0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					Px_change = -4

				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					Px_change = +4

				if event.key == pygame.K_SPACE:
					if b_state is "ready":
						b_sound = mixer.Sound("laser.wav")
						b_sound.play()
						bx = Px
						fire(bx, by)

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					Px_change = 0


		Px += Px_change

		if Px <= 0:
			Px = 0

		if Px >= 735:
			Px = 735

		if score_value == 10:
			#break
			running = False
			glvl += 1
			level += 1
			num_enemy += 2
			Targets += 5
			home_page()
			#running = False



		#game over

		for i in range(num_of_enemies):

			if ey[i] > 440:
				for j in range(num_of_enemies):
					ey[j] = 2000
				game_over_text()
				#pygame.QUIT
				break

			ex[i] += ex_change[i]

			if ex[i] <= 0:
				ex_change[i] = 2
				ey[i] += ey_change[i]

			elif ex[i] >= 736:
				ex_change[i] = -2
				ey[i] += ey_change[i]

			#colllison
			coll = collision(ex[i],ey[i],bx,by)
			if coll:
				by = 480
				b_state = "ready"
				score_value += 1
				kill_sound = mixer.Sound("explosion.wav")
				kill_sound.play()
				ex[i] = random.randint(0, 736)
				ey[i]= random.randint(50, 150)
				coins += 10

			enemy(ex[i], ey[i], i)


		if by <= 0:
			by = 480
			b_state = "ready"

		if b_state is "fire":
			fire(bx, by)
			by -= by_change

		player(Px, Py)
		show_score(textx, texty)
		show_target(textx + 630, texty)
		show_coins(textx + 330 , texty)

		pygame.display.update()

def lvl2():
	global b_state
	global glvl
	global level
	global num_enemy
	global Targets
	global by_change
	global coins

	bg = pygame.image.load("background.png")

	mixer.music.load("background.wav")
	mixer.music.play(-1)

	#player
	pimg = pygame.image.load("space-invaders.png")
	Px = 370
	Py = 480
	Px_change = 0

	#enemy
	eimg = []
	ex = []
	ey = []
	ex_change = []
	ey_change = []
	num_of_enemies = 8

	for i in range(num_of_enemies):
		eimg.append(pygame.image.load("alien (1).png"))
		ex.append(random.randint(0, 736))
		ey.append(random.randint(50, 150))
		ex_change.append(3)
		ey_change.append(60)

	#bullet
	bimg = pygame.image.load("bullet.png")
	bx = 0
	by = 480
	bx_change = 0
	#by_change += 10
	b_state = "ready"

	#score
	score_value = 0
	font = pygame.font.Font('freesansbold.ttf', 32)

	over_font = pygame.font.Font('freesansbold.ttf', 64)

	textx = 10
	texty = 10


	def show_score(x, y):
		score = font.render("score : "+ str(score_value), True, (0,225,0))
		screen.blit(score, (x, y))

	def show_target(x, y):
		target= T_font.render("target : "+ str(Targets), True, (0,225,0))
		screen.blit(target, (x, y))

	def show_coins(x, y):
		coin_draw = C_font.render("Coins : "+ str(coins), True, (0,225,0))
		screen.blit(coin_draw, (x, y))

	def game_over_text():
		over_text = over_font.render("GAMEOVER", True, (0,225,0))
		screen.blit(over_text, (200, 250))

	def player(x,y):
		screen.blit(pimg, (x, y))

	def enemy(x,y,i):
		screen.blit(eimg[i], (x, y))

	def fire(x, y):
		global b_state
		b_state = "fire"
		screen.blit(bimg, (x+16, y+10))

	def collision(ex, ey, bx, by):
		distance = math.sqrt((math.pow(ex-bx,2)) + (math.pow(ey-by,2)))
		if distance <= 27:
			return True
		else:
			return False

	running = True
	while running:
		screen.fill((0, 0, 0))

		screen.blit(bg,(0,0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					Px_change = -4

				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					Px_change = +4

				if event.key == pygame.K_SPACE:
					if b_state is "ready":
						b_sound = mixer.Sound("laser.wav")
						b_sound.play()
						bx = Px
						fire(bx, by)

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					Px_change = 0


		Px += Px_change

		if Px <= 0:
			Px = 0

		if Px >= 735:
			Px = 735

		if score_value == 15:
			#break
			running = False
			glvl += 1
			level += 1
			num_enemy += 2
			Targets += 5
			home_page()

		#game over
		for i in range(num_of_enemies):

			if ey[i] > 440:
				for j in range(num_of_enemies):
					ey[j] = 2000
				game_over_text()
				#pygame.QUIT
				break

			ex[i] += ex_change[i]

			if ex[i] <= 0:
				ex_change[i] = 3
				ey[i] += ey_change[i]

			elif ex[i] >= 736:
				ex_change[i] = -3
				ey[i] += ey_change[i]

			#colllison
			coll = collision(ex[i],ey[i],bx,by)
			if coll:
				by = 480
				b_state = "ready"
				score_value += 1
				kill_sound = mixer.Sound("explosion.wav")
				kill_sound.play()
				ex[i] = random.randint(0, 736)
				ey[i]= random.randint(50, 150)
				coins += 10

			enemy(ex[i], ey[i], i)


		if by <= 0:
			by = 480
			b_state = "ready"

		if b_state is "fire":
			fire(bx, by)
			by -= by_change

		player(Px, Py)
		show_score(textx, texty)
		show_target(textx + 630, texty)
		show_coins(textx + 330 , texty)

		pygame.display.update()

def home_page():
	global by_change
	global inc_speed
	global coins

	pygame.init()
	clock = pygame.time.Clock()
	fps = 60
	size = [200, 200]
	bg = [255, 255, 255]
	bgg = pygame.image.load("play.png")
	screen = pygame.display.set_mode((800,600))
	screen.blit(background,(0,0))
	color = (255,0,0)


	#level text drawing
	level_draw = L_font.render("Level : "+ str(level), True, (0,225,0))
	screen.blit(level_draw, (250,150))


	#num enemies text drawing
	enemy_draw = E_font.render("Enemies : "+ str(num_enemy), True, (0,225,0))
	screen.blit(enemy_draw, (220,250))

	pygame.draw.rect(screen, color, pygame.Rect(362, 493, 81, 81))

	#play button
	button = screen.blit(bgg, (370, 500))

	pygame.draw.rect(screen, color, pygame.Rect(260, 490, 81, 81))

	double_speed = screen.blit(inc_speed, (270,500))

	coin_draw = C_font.render("Coins : "+ str(coins), True, (0,225,0))
	screen.blit(coin_draw, (230,350))

	while True:


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False

			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button
				if button.collidepoint(mouse_pos):
                    # prints current location of mouse
					#print('button was pressed at {0}'.format(mouse_pos))
					if glvl == 1:
						lvl1()

					elif glvl == 2:
						lvl2()
						#lvl2()

				elif double_speed.collidepoint(mouse_pos):
					if coins >= 500:
						by_change += 5
						coins -= 500
						print(coins)

					elif by_change > 25:
						inc_speed = pygame.image.load("maxed.png")



		pygame.display.update()

	pygame.quit()
	sys.exit

home_page()
