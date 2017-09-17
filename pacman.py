import pygame

class Pacman():
	def __init__(self, ai_settings, screen):
		self.ai_settings = ai_settings
		self.screen = screen
		
		self.image = pygame.image.load('images/pacman_right.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		
		self.rect.x, self.rect.y = 0, 0
		
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		
		self.movement_right = False
		self.movement_left = False
		self.movement_up = False
		self.movement_down = False
		
	def update(self):
		if self.movement_right and self.rect.right < self.screen.rect.right:
			self.centerx += self.ai_settings.pacman_speed_factor
		if self.movement_left and self.rect.left > 0:
			self.centerx -= self.ai_settings.pacman_speed_factor
		if self.movement_up and self.rect.top > 0:
			self.centery -= self.ai_settings.pacman_speed_factor
		if self.movement_down and self.rect.bottom < self.screen_rect.bottom:
			self.centery += self.ai_settings.pacman_speed_factor
		
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
	"""def walk(self):
		
		
	def turn_left(self):
		
	def turn_right(self):"""
		
