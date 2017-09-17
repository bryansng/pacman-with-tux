import pygame
from pygame.sprite import Group

from settings import Settings
import game_functions as gf
from pacman import Pacman
from ball import Ball
from wall import Wall

def run_game():
	pygame.init()
	pygame.mixer.init()
	
	ai_settings = Settings()
	
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Pac-man")
	
	pacman = Pacman(ai_settings, screen)
	balls = Group()
	walls = Group()
	
	gf.create_walls(ai_settings, screen, walls)
	
	while True:
		gf.check_events()
		
		gf.update_internals(ai_settings, screen, pacman, balls, walls)
		
		gf.update_screen(ai_settings, screen, pacman, balls, walls)
		
		
	
run_game()
