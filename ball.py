import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
	"""A class to represent the balls eaten by Pacman."""
	def __init__(self, ai_settings, screen):
		"""Initializes Ball settings."""
		super().__init__()
		self.ai_settings = ai_settings
		self.screen = screen
		
		# Loads image and get image rect.
		self.image = pygame.image.load('images/ball.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		
		# Position the ball/image to specified spot.
		self.rect.x, self.rect.y = 0, 0
		
		# Float values to a new variable if not decimals will not be registered.
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		
	def update(self):
		"""Updates the position of the Ball."""
		# Float values are converted to integers and assigned back to the rect.
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery
		
	def blitme(self):
		"""Draws the Ball onto the screen."""
		# Only for individual balls, sprites are prefered to use 
		# self.draw(self.screen) or balls.draw(screen)
		self.screen.blit(self.image, self.rect)
		
	
