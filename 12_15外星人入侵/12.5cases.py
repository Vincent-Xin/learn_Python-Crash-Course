import sys
import pygame
#12-1
pygame.init()
screen=pygame.display.set_mode((1000,800))
pygame.display.set_caption('12-1 Blue window')
bg_color=(15,15,120)
pic_name='images/wenminghujian.bmp'

def run_game():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		screen.fill(bg_color)
		pic(pic_name,screen)
		pygame.display.flip()


# 12-2
def pic(pic_name,screen):
	pic=pygame.image.load(pic_name)
	pic_rect=pic.get_rect()
	screen_rect=screen.get_rect()

	pic_rect.center=screen_rect.center
	screen.blit(pic,pic_rect)

run_game()


