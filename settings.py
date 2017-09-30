class Settings():
	def __init__(self):
		"""Initialize all the static settings of the game."""
		# Screen settings.
		self.screen_width = 600
		self.screen_height = 600
		self.bg_color = (192, 192, 192)
		
		# Pacman settings.
		self.pacman_speed_factor = 0.3
		# Pacman move settings.
		self.pacman_time_move = 0
		self.pacman_time_move_interval = 0.2
		
		
