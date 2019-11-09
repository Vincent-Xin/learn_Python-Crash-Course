import sys
import pygame
from pygame.sprite import Sprite

class Ship():
	def __init__(self,screen):
		self.screen=screen
		self.screen_rect=self.screen.get_rect()

		self.image=pygame.image.load('images/ship.bmp')
		self.rect=self.image.get_rect()

		self.rect.left=self.screen_rect.left
		self.rect.centery=self.screen_rect.centery

		self.moving_up=False
		self.moving_down=False

	def blitme(self):
		self.screen.blit(self.image,self.rect)

	def ship_moving(self):
		if self.moving_up and self.rect.top > 0:
			self.rect.centery-=10
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.centery+=10

class Bullet(Sprite):
	def __init__(self,screen,ship):
		super(Bullet,self).__init__()
		self.screen=screen
		self.screen_rect=self.screen.get_rect()

		self.width=10
		self.height=3
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.centery=ship.rect.centery
		self.rect.right=ship.rect.right
		self.color=(255,255,255)

	def bullet_fly(self):
		self.rect.centerx+=10

	def draw_bullets(self):
		pygame.draw.rect(self.screen,self.color,self.rect)

def bullets_firer(bullets,screen,ship):
	new_bullet=Bullet(screen,ship)
	bullets.append(new_bullet)

def del_bullet(bullets):
	for bullet in bullets[:]:
		if bullet.rect.left >= bullet.screen_rect.right:
			bullets.remove(bullet)

def check_keydown(ship,screen,event,bullets):
	if event.key == pygame.K_UP:
		ship.moving_up=True
	elif event.key == pygame.K_DOWN:
		ship.moving_down=True
	elif event.key == pygame.K_SPACE:
		bullets_firer(bullets,screen,ship)
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup(ship,event):
	if event.key == pygame.K_UP:
		ship.moving_up=False
	elif event.key == pygame.K_DOWN:
		ship.moving_down=False

def check_events(ship,screen,bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown(ship,screen,event,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup(ship,event)

def update_screen(bullets,ship):
	for bullet in bullets:
		bullet.bullet_fly()
		
	del_bullet(bullets)

	for bullet in bullets:
		bullet.draw_bullets()

	ship.blitme()

	pygame.display.flip()

def run_game():
	pygame.init()
	screen=pygame.display.set_mode((1200,800))
	pygame.display.set_caption("12_5 左侧的飞船，右射的子弹")

	screen_color=(0,0,0)

	ship=Ship(screen)
	# bullet=Bullet(screen,ship)
	bullets=[]
	
	while True:
		screen.fill(screen_color)
		check_events(ship,screen,bullets)

		ship.ship_moving()

		update_screen(bullets,ship)
		
		

run_game()

