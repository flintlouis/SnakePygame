import random
import pygame

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

GRIDSIZE = 20
GRID_WIDTH = SCREEN_HEIGHT / GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH / GRIDSIZE

START_POS = (240, 240)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

WHITE = (255,255,255)
BLACK = (0,0,0)

class Snake(object):
	def __init__(self, len):
		self.colour = (20,100,20)
		self.reset(len)

	def add_body(self):
		self.body.append(self.body[-1])

	def turn(self, dir):
		if (dir[0]*-1, dir[1]*-1) == self.direction or not self.moved:
			return
		self.direction = dir
		self.moved = False

	def move(self):
		x, y = self.direction
		headx, heady = self.head
		newhead = (((x*GRIDSIZE)+headx)%SCREEN_WIDTH, ((y*GRIDSIZE)+heady)%SCREEN_HEIGHT)
		self.body.insert(0, newhead)
		self.body.pop()
		self.head = self.body[0]
		self.moved = True

	def reset(self, len):
		self.moved = True
		self.body = [START_POS]
		self.direction = RIGHT
		for i in range(len-1):
			self.add_body()
		self.head = self.body[0]

	def draw(self, surface):
		for pos in self.body:
			r = pygame.Rect(pos, (GRIDSIZE, GRIDSIZE))
			pygame.draw.rect(surface, self.colour, r)

class Food(object):
	def __init__(self):
		self.colour = (150, 20, 20)
		self.randomize_position()


	def randomize_position(self):
		self.position = (random.randint(0, GRID_WIDTH-1) * GRIDSIZE, random.randint(0, GRID_HEIGHT-1) * GRIDSIZE)

	def draw(self, surface):
		r = pygame.Rect(self.position, (GRIDSIZE, GRIDSIZE))
		pygame.draw.rect(surface, self.colour, r)

class Settings:
	mute = False
	fps = 10
	speedup = 8
