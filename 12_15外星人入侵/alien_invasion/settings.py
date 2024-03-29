class Settings():
	'''storing all settings of the game'''
	def __init__(self):
		'''initializing the settings'''
		#screen settings
		self.screen_width=1000
		self.screen_height=800
		self.bg_color=(230,230,230)
		
		#ship settings
		# self.ship_speed_factor=10
		self.ship_limit=3

		#bullet settings
		# self.bullet_speed_factor=10
		self.bullet_width=500
		self.bullet_height=20
		self.bullet_color=60,60,60
		self.bullets_allowed=100
		
		#alien settings
		# self.alien_speed_factor=20
		self.fleet_drop_speed=30
		# self.fleet_direction=1

		self.speedup_scale=1.1
		self.score_scale=1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		'''originalizing setting as game playing'''
		self.ship_speed_factor=10
		self.bullet_speed_factor=20
		self.alien_speed_factor=10
		self.alien_points=50

		self.fleet_direction=1

	def increase_speed(self):
		self.ship_speed_factor*=self.speedup_scale
		self.bullet_speed_factor*=self.speedup_scale
		self.alien_speed_factor*=self.speedup_scale

		self.alien_points=int(self.alien_points*self.score_scale)
	
