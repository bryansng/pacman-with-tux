import pygame
from pygame.sprite import Group
import time
from time import process_time

from settings import Settings
import game_functions as gf
from pacman import Pacman
from ball import Ball
from wall import Wall

def get_process_time():
	# Returns the process time at the time of request or call of this method.
	process_time = time.process_time()
	return process_time

def run_game():
	"""Runs the game, duh."""
	# Initialize pygame and pygame.mixer settings.
	pygame.init()
	pygame.mixer.init()
	
	# Initialize settings as ai_settings.
	ai_settings = Settings()
	
	# Initialize screen using width and height from ai_settings.
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	# Setting the game name
	pygame.display.set_caption("Pac-man with Tux")
	
	# Initialize all other game settings.
	pacman = Pacman(ai_settings, screen)
	balls = Group()
	walls = Group()
	
	# Creates the red brick walls in the game.
	gf.create_walls(ai_settings, screen, walls)
	
	while True:
		# Assigns the time_new with the current time since the start of the game.
		# Then passes it into the game functions for use.
		time_new = float('{:.1f}'.format(get_process_time()))
		
		# Handles all the events in the game and invokes functions based on those events.
		gf.check_events(ai_settings, pacman, time_new)
		
		# Handles all the internals of the objects in the game and invokes functions based on certain events.
		gf.update_internals(ai_settings, screen, pacman, balls, walls)
		
		# Displays all the objects or contents of the game.
		gf.update_screen(ai_settings, screen, pacman, balls, walls)
		
		
# Runs the run_game() function which actually runs the game.
run_game()
