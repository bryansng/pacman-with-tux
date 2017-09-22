import pygame

class Pacman():
	def __init__(self, ai_settings, screen):
		self.ai_settings = ai_settings
		self.screen = screen
		
		self.image_right = pygame.image.load('images/pacman_right.bmp')
		self.image_left = pygame.image.load('images/pacman_left.bmp')
		
		self.image_left_up = pygame.image.load('images/pacman_left_up.bmp')
		self.image_right_up = pygame.image.load('images/pacman_right_up.bmp')
		
		self.image_left_down = pygame.image.load('images/pacman_left_down.bmp')
		self.image_right_down = pygame.image.load('images/pacman_right_down.bmp')
		
		self.image = self.image_right
		self.rect = self.image_right.get_rect()
		self.screen_rect = self.screen.get_rect()
		
		self.rect.centerx, self.rect.centery = self.screen_rect.centerx, self.screen_rect.centery
		
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		
		self.movement_right = False
		self.movement_left = False
		self.movement_up = False
		self.movement_down = False
		
	def face_direction(self, event, ai_settings, time_new):
		if event.key == pygame.K_w and (self.image != self.image_left_up or self.image != self.image_right_up):
			self.direction_pivot_w(ai_settings, time_new)
		if event.key == pygame.K_s and (self.image != self.image_left_down or self.image != self.image_right_down):
			self.direction_pivot_s(ai_settings, time_new)
		if event.key == pygame.K_a and (self.image != self.image_left):
			self.direction_pivot_a(ai_settings, time_new)
		if event.key == pygame.K_d and (self.image != self.image_right):
			self.direction_pivot_d(ai_settings, time_new)
			
	def direction_pivot_w(self, ai_settings, time_new):
		time_for_move_2 = ai_settings.pacman_time_move + ai_settings.pacman_time_move_interval
		#time_for_move_3 = ai_settings.pacman_time_move + (ai_settings.pacman_time_move_interval * 2)
		
		if self.image == self.image_right:
			self.image = self.image_right_up
			
		if self.image == self.image_left:
			self.image = self.image_left_up
			
		if self.image == self.image_left_up:
			pass
			
		if self.image == self.image_right_up:
			pass
			
		if self.image == self.image_left_down:
			self.image = self.image_left
			if time_new >= time_for_move_2:
				self.image = self.image_left_up
			
		if self.image == self.image_right_down:
			self.image = self.image_right
			if time_new >= time_for_move_2:
				self.image = self.image_right_up
			
			
	def direction_pivot_s(self, ai_settings, time_new):
		time_for_move_2 = ai_settings.pacman_time_move + ai_settings.pacman_time_move_interval
		#time_for_move_3 = ai_settings.pacman_time_move + (ai_settings.pacman_time_move_interval * 2)
		
		if self.image == self.image_right:
			self.image = self.image_right_down
			
		if self.image == self.image_left:
			self.image = self.image_left_down
			
		if self.image == self.image_left_up:
			self.image = self.image_left
			if time_new >= time_for_move_2:
				self.image = self.image_left_down
			
		if self.image == self.image_right_up:
			self.image = self.image_right
			if time_new >= time_for_move_2:
				self.image = self.image_right_down
			
		if self.image == self.image_left_down:
			pass
			
		if self.image == self.image_right_down:
			pass
			
			
	def direction_pivot_d(self, ai_settings, time_new):
		time_for_move_2 = ai_settings.pacman_time_move + ai_settings.pacman_time_move_interval
		time_for_move_3 = ai_settings.pacman_time_move + (ai_settings.pacman_time_move_interval * 2)
		
		if self.image == self.image_right:
			pass
			
		if self.image == self.image_left:
			self.image = self.image_left_up
			if time_new >= time_for_move_2:
				self.image = self.image_right_up
				if time_new >= time_for_move_3:
					self.image = self.image_right
			
		if self.image == self.image_left_up:
			self.image = self.image_right_up
			if time_new >= time_for_move_2:
				self.image = self.image_right
			
		if self.image == self.image_right_up:
			self.image = self.image_right
			
		if self.image == self.image_left_down:
			self.image = self.image_right_down
			if time_new >= time_for_move_2:
				self.image = self.image_right
			
		if self.image == self.image_right_down:
			self.image = self.image_right
			
			
	def direction_pivot_a(self, ai_settings, time_new):
		time_for_move_2 = ai_settings.pacman_time_move + ai_settings.pacman_time_move_interval
		time_for_move_3 = ai_settings.pacman_time_move + (ai_settings.pacman_time_move_interval * 2)
		
		if self.image == self.image_right:
			self.image = self.image_right_up
			if time_new >= time_for_move_2:
				self.image = self.image_left_up
				if time_new >= time_for_move_3:
					self.image = self.image_left
			
		if self.image == self.image_left:
			pass
			
		if self.image == self.image_left_up:
			self.image = self.image_left
			
		if self.image == self.image_right_up:
			self.image = self.image_left_up
			if time_new >= time_for_move_2:
				self.image = self.image_left
			
		if self.image == self.image_left_down:
			self.image = self.image_left
			
		if self.image == self.image_right_down:
			self.image = self.image_left_down
			if time_new >= time_for_move_2:
				self.image = self.image_left
			
		
	def update(self):
		if self.movement_right and self.rect.right < self.screen_rect.right:
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
		
