import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	'''control bullets'''
	def __init__(self,ai_settings,screen,ship):
		super(Bullet,self).__init__()
		self.screen=screen

		#creat a bullet at 0,0,then place it at crrect place
		self.rect=pygame.Rect(
			0,0,ai_settings.bullet_width,ai_settings.bullet_height)
		self.rect.centerx=ship.rect.centerx
		self.rect.top=ship.rect.top
		#bullet location in float
		self.y=float(self.rect.y)

		self.color=ai_settings.bullet_color
		self.speed_factor=ai_settings.bullet_speed_factor

	def update(self):
		'''bullet upmoving'''
		#update y
		self.y-=self.speed_factor
		#update real y
		self.rect.y=self.y

	def draw_bullet(self):
		'''draw bullets on screen'''
		pygame.draw.rect(self.screen,self.color,self.rect)