import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self,ai_settings,screen):
		'''initialinzing the ship and its location'''
		super(Ship,self).__init__()
		self.screen=screen
		self.ai_settings=ai_settings

		#load the ship.bmp and get a outside rect
		self.image=pygame.image.load('images/ship.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()

		#set the ship at the middle bottom of the screen
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom

		self.center=float(self.rect.centerx)

		#moving flag
		self.moving_right=False
		self.moving_left=False

	def update(self):
		'''adjust the ship location according to the flags'''
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx+=self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.rect.centerx-=self.ai_settings.ship_speed_factor
		# self.rect.centerx=self.center

	def blitme(self):
		'''shape the ship at the specific place'''
		self.screen.blit(self.image,self.rect)

	def center_ship(self):
		self.rect.centerx=self.screen_rect.centerx
