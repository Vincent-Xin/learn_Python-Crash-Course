import sys
import pygame
#12-3
pygame.init()
screen=pygame.display.set_mode((1000,800))
pygame.display.set_caption('12-3 A ship')
bg_color=(120,120,120)

class Ship():
	def __init__(self,screen):
		self.screen=screen
		self.image=pygame.image.load('images/ship.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=self.screen.get_rect()

		self.rect.centerx=self.screen_rect.centerx
		self.rect.centery=self.screen_rect.centery

		self.moving_right=False
		self.moving_left=False
		self.moving_up=False
		self.moving_down=False
	def move_ship(self):
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.centery+=10
		if self.moving_up and self.rect.top > 0:
			self.rect.centery-=10
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx+=10
		if self.moving_left and self.rect.left > 0:
			self.rect.centerx-=10
	def blit_ship(self):
		self.screen.blit(self.image,self.rect)

def check_keydown_events(event,ship):
	'''react to keydown'''
	if event.key == pygame.K_RIGHT:
		ship.moving_right=True
	elif event.key == pygame.K_LEFT:
		ship.moving_left= True
	elif event.key == pygame.K_UP:
		ship.moving_up= True
	elif event.key == pygame.K_DOWN:
		ship.moving_down= True

def check_keyup_events(event,ship):
	'''react to keyup'''
	if event.key == pygame.K_RIGHT:
		ship.moving_right=False
	elif event.key == pygame.K_LEFT:
		ship.moving_left=False
	elif event.key == pygame.K_UP:
		ship.moving_up=False
	elif event.key == pygame.K_DOWN:
		ship.moving_down=False

def check_events(ship):
	'''react to keyboard and mouse'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ship)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)

ship=Ship(screen)

while True:
	check_events(ship)

	screen.fill(bg_color)
	ship.blit_ship()
	ship.move_ship()

	pygame.display.flip() 





