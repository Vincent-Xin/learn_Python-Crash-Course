import pygame
from settings import Settings
from ship import Ship
import game_functions 
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption('Alien Invasion') #game window title	
	ship=Ship(ai_settings,screen) #creat a ship
	bullets=Group()
	aliens=Group()
	stats=GameStats(ai_settings)
	play_button=Button(ai_settings,screen,"Play")
	sb=Scoreboard(ai_settings,screen,stats)

	#creat alien group
	game_functions.creat_fleet(ai_settings,screen,ship,aliens)
	game_functions.read_high_score(stats,sb)

	#游戏主循环
	while True:
		#键盘和鼠标事件
		game_functions.check_events(ai_settings,screen,
			stats,ship,aliens,bullets,sb,play_button)

		if stats.game_active:
			ship.update()
			game_functions.update_bullets(
				ai_settings,screen,stats,ship,aliens,bullets,sb)
			game_functions.update_aliens(
				ai_settings,stats,screen,ship,aliens,bullets,sb)

		game_functions.update_screen(
			ai_settings,screen,stats,ship,aliens,bullets,sb,play_button)
		
run_game()