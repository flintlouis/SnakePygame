import pygame
import sys
import os
from game import *

def draw_grid(surface):
	for x in range(int(GRID_WIDTH)):
		for y in range(int(GRID_HEIGHT)):
			r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
			if (x + y) % 2:
				pygame.draw.rect(surface, (80,165,165), r)
			else:
				pygame.draw.rect(surface, (70,155,155), r)

def handle_keys(snake, setting):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == ord('a') or event.key == pygame.K_LEFT:
				snake.turn(LEFT)
			elif event.key == ord('s') or event.key == pygame.K_DOWN:
				snake.turn(DOWN)
			elif event.key == ord('d') or event.key == pygame.K_RIGHT:
				snake.turn(RIGHT)
			elif event.key == ord('w') or event.key == pygame.K_UP:
				snake.turn(UP)
			elif event.key == ord('m'):
				if setting.mute:
					setting.mute = False
					pygame.mixer.music.unpause()
				else:
					setting.mute = True
					pygame.mixer.music.pause()
			elif event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()

def main():
	os.system("clear")
	print("Loading...")
	pygame.init()
	pygame.display.set_caption('Snake')
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

	surface = pygame.Surface(screen.get_size())
	surface = surface.convert()

	myfont = pygame.font.SysFont("arialblack", 16)

	snake = Snake(3)
	apple = Food()
	setting = Settings()

	bitesound = pygame.mixer.Sound('sounds/bite.wav')
	hit = pygame.mixer.Sound('sounds/hit.wav')
	music = pygame.mixer.music.load('sounds/music.mp3')
	pygame.mixer.music.play(-1)
	os.system("clear")

	score = 0
	while(True):
		clock.tick(setting.fps)
		surface.fill(BLACK)

		snake.move()
		# Check collision
		if snake.head in snake.body[2:]:
			if not setting.mute:
				hit.play()
			snake.reset(3)
			apple.randomize_position()
			setting.fps = 10
			setting.speedup = 5
			score = 0
			pygame.time.delay(1000)
		# Check if apple gets eaten
		elif snake.head == apple.position:
			if not setting.mute:
				bitesound.play()
			snake.add_body()
			while apple.position in snake.body:
				apple.randomize_position()
			score += 1
			# Speed up
			if score == setting.speedup and setting.speedup <= 50:
				setting.speedup += 8
				setting.fps += 2

		snake.draw(surface)
		apple.draw(surface)
		handle_keys(snake, setting)

		screen.blit(surface, (0,0))
		text = myfont.render(f"Score {score}", 1, WHITE)
		screen.blit(text, (5, 10))
		pygame.display.update()

main()
