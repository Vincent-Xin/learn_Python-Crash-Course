import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ai_settings,screen,stats,ship,aliens,bullets,sb):
	'''react to keydown'''
	if event.key == pygame.K_RIGHT:
		ship.moving_right=True
	elif event.key == pygame.K_LEFT:
		ship.moving_left=True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
	elif event.key == pygame.K_q:
		sys.exit()
	elif event.key == pygame.K_s and not stats.game_active:
		start_game(ai_settings,screen,stats,ship,aliens,bullets,sb)

def check_keyup_events(event,ship):
	'''react to keyup'''
	if event.key == pygame.K_RIGHT:
		ship.moving_right=False
	elif event.key == pygame.K_LEFT:
		ship.moving_left=False

def check_events(ai_settings,screen,stats,ship,aliens,bullets,sb,play_button):
	'''react to keyboard and mouse'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,
				screen,stats,ship,aliens,bullets,sb)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y=pygame.mouse.get_pos()
			check_play_button(ai_settings,screen,stats,ship,aliens,bullets,sb,
				play_button,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,ship,aliens,bullets,sb,
	play_button,mouse_x,mouse_y):
	button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
	if button_clicked and not stats.game_active:
		start_game(ai_settings,screen,stats,ship,aliens,bullets,sb)
		

def start_game(ai_settings,screen,stats,ship,aliens,bullets,sb):
	ai_settings.initialize_dynamic_settings()
	stats.game_active=True
	pygame.mouse.set_visible(False)

	stats.reset_stats()
	aliens.empty()
	bullets.empty()

	sb.prep_images()

	creat_fleet(ai_settings,screen,ship,aliens)
	ship.center_ship()

def update_screen(ai_settings,screen,stats,ship,aliens,bullets,sb,play_button):
	#每次循环都重绘屏幕
	screen.fill(ai_settings.bg_color)
	
	#draw all bullets behind ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	#code behind screen.fill,so in game before it
	ship.blitme()
	aliens.draw(screen)
	sb.show_score()

	if not stats.game_active:
		play_button.draw_button()

	#让新绘制的屏幕可见
	pygame.display.flip()

def update_bullets(ai_settings,screen,stats,ship,aliens,bullets,sb):
	'''update bullets location,and delete disappearing bullets'''
	#update bullets location
	bullets.update()
	
	#delete bullet
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	check_bullet_alien_collisions(
		ai_settings,screen,stats,ship,aliens,bullets,sb)

def check_bullet_alien_collisions(
	ai_settings,screen,stats,ship,aliens,bullets,sb):
	'''react to collosions'''
	#delete alien and bullet of collosion ,return collisions as a dic
	new_score(ai_settings,stats,aliens,bullets,sb)
	start_new_level(ai_settings,screen,stats,ship,aliens,bullets,sb)

def new_score(ai_settings,stats,aliens,bullets,sb):
	collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
	
	if collisions:
		for aliens in collisions.values():
			stats.score+=ai_settings.alien_points*len(aliens)
			sb.prep_score()
		check_high_score(stats,sb)
		store_high_score(stats)

def start_new_level(ai_settings,screen,stats,ship,aliens,bullets,sb):
	if len(aliens) == 0:
		#delete bullets and creat a new group of aliens
		bullets.empty()
		ai_settings.increase_speed()
		stats.level+=1
		sb.prep_level()

		creat_fleet(ai_settings,screen,ship,aliens)

def fire_bullet(ai_settings,screen,ship,bullets):
	'''if allowed fire a bullet'''
	##creat a new bullet and join it in a group
	if len(bullets) < ai_settings.bullets_allowed:
			new_bullet=Bullet(ai_settings,screen,ship)
			bullets.add(new_bullet)

def creat_fleet(ai_settings,screen,ship,aliens):
	'''creat alien group'''
	#creat an alien and calculate amount
	#distance of an alien is an alien
	alien =Alien(ai_settings,screen)
	alien_width=alien.rect.width
	number_aliens_x=get_number_alien_x(ai_settings,alien_width)
	number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

	for row_number in range(number_rows):
		#creat first line
		for alien_number in range(number_aliens_x):
			#creat an alien and append
			creat_alien(ai_settings,screen,alien_number,aliens,row_number)
		

def get_number_alien_x(ai_settings,alien_width):
	'''calculate number in a line'''
	availabel_space_x=ai_settings.screen_width - alien_width #书中是2*alien_width，似乎不对
	number_aliens_x=int(availabel_space_x/(2*alien_width))
	return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
	'''work out how many rows'''
	available_space_y=ai_settings.screen_height-ship_height-3*alien_height
	number_rows=int(available_space_y/(2*alien_height))
	return number_rows

def creat_alien(ai_settings,screen,alien_number,aliens,row_number):
	'''creat an alien'''
	alien=Alien(ai_settings,screen)
	alien.x=alien.rect.width*2*alien_number+alien.rect.width
	alien.y=alien.rect.height*2*row_number+alien.rect.height
	alien.rect.x=alien.x
	alien.rect.y=alien.y
	aliens.add(alien)

def check_fleet_edges(ai_settings,aliens):
	'''do something if reaching edges'''
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break
def change_fleet_direction(ai_settings,aliens):
	'''drop aliens and change direction'''
	for alien in aliens.sprites():
		alien.rect.y+=ai_settings.fleet_drop_speed
	ai_settings.fleet_direction*=-1

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb):
	'''react to ship hit'''
	if stats.ships_left>0:
		stats.ships_left-=1

		sb.prep_ships()

		aliens.empty()
		bullets.empty()

		creat_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()

		sleep(0.5)
	else:
		stats.game_active=False
		pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,sb):
	'''check alien is at bottom or not'''
	screen_rect=screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb)
			break

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets,sb):
	'''check direction and update'''
	check_fleet_edges(ai_settings,aliens)
	aliens.update()

	#edge and aliens collosions
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb)

	check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,sb)

def check_high_score(stats,sb):
	'''check getting highest score or not'''
	if stats.score > stats.high_score:
		stats.high_score=stats.score
		sb.prep_high_score()

def store_high_score(stats):
	with open('high_score.txt','w') as hs_obj:
		hs_obj.write(str(stats.high_score))

def read_high_score(stats,sb):
	try:
		with open('high_score.txt') as hs_obj:
			high_score=hs_obj.read()
	except:
		pass
	else:
		stats.high_score=int(high_score)
		sb.prep_high_score()






	















