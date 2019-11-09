import sys
import pygame

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

def update_screen(ai_settings,screen,ship):
	#每次循环都重绘屏幕？？？？
	screen.fill(ai_settings.bg_color)
	#code behind screen.fill,so in game before it
	ship.blitme()

	#让新绘制的屏幕可见
	pygame.display.flip()