import pygame
from pygame.sprite import Sprite

class Wall(Sprite):
	"""A class to represent the balls eaten by Pacman."""
	def __init__(self, ai_settings, screen):
		"""Initializes Wall settings."""
		super().__init__()
		self.ai_settings = ai_settings
		self.screen = screen
		
		# Loads image and get image rect.
		self.image = pygame.image.load('images/wall.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		
		# Position the wall/image to specified spot.
		self.rect.x, self.rect.y = 0, 0
		
		# Float values to a new variable if not decimals will not be registered.
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		
		#self.x = float(self.rect.x)
		#self.y = float(self.rect.y)
		
	def update(self):
		"""Updates the position of the Wall."""
		# Float values are converted to integers and assigned back to the rect.
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery
		
		#self.rect.x = self.x
		#self.rect.y = self.y
		
	def blitme(self):
		"""Draws the Wall onto the screen."""
		# Only for individual walls, sprites are prefered to use 
		# self.draw(self.screen) or walls.draw(screen)
		self.screen.blit(self.image, self.rect)
