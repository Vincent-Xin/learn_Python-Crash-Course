#12-4
import sys
import pygame

screen=pygame.display.set_mode((0,0))
pygame.display.set_caption('12-4 print pygame keydown')

def get_event():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			print(event.key)
pygame.init()
while True:

	get_event()

	pygame.display.flip()