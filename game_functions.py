import sys
import pygame

from wall import Wall
from pacman import Pacman

def check_keydown_events(event, ai_settings, screen, pacman, time_new):
	"""Deals with all keydown events."""
	# Exits game.
	if event.key == pygame.K_q:
		pygame.quit()
		sys.exit()
	# Get user's destination input, then moves towards it.
	if event.key == pygame.K_m:
		pacman.randomize_and_move_to_point(ai_settings, screen, time_new)
	# Events for WASD, controls the motion of the pacman and changes its
	# face direction.
	# Up
	if event.key == pygame.K_w and (not pacman.movement_down and not pacman.movement_left and not pacman.movement_right):
		pacman.movement_up = True
		pacman.face_direction(event, ai_settings, time_new)
		ai_settings.pacman_time_move = time_new
	# Down
	elif event.key == pygame.K_s and (not pacman.movement_up and not pacman.movement_left and not pacman.movement_right):
		pacman.movement_down = True
		pacman.face_direction(event, ai_settings, time_new)
		ai_settings.pacman_time_move = time_new
	# Left
	elif event.key == pygame.K_a and (not pacman.movement_up and not pacman.movement_down and not pacman.movement_right):
		pacman.movement_left = True
		pacman.face_direction(event, ai_settings, time_new)
		ai_settings.pacman_time_move = time_new
	# Right
	elif event.key == pygame.K_d and (not pacman.movement_up and not pacman.movement_down and not pacman.movement_left):
		pacman.movement_right = True
		pacman.face_direction(event, ai_settings, time_new)
		ai_settings.pacman_time_move = time_new
	
def check_keyup_events(event, ai_settings, pacman):
	"""Deals with all keyup events."""
	# Up
	if event.key == pygame.K_w:
		pacman.movement_up = False
	# Down
	elif event.key == pygame.K_s:
		pacman.movement_down = False
	# Left
	elif event.key == pygame.K_a:
		pacman.movement_left = False
	# Right
	elif event.key == pygame.K_d:
		pacman.movement_right = False
	
def check_events(ai_settings, screen, pacman, time_new):
	"""Deals with all the events."""
	for event in pygame.event.get():
		# Exits game upon cicking the 'x'.
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		# Checks all key down events for the keyboard.
		if event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, pacman, time_new)
		# Checks all key up events for the keyboard.
		if event.type == pygame.KEYUP:
			check_keyup_events(event, ai_settings, pacman)
		
		

def update_internals(ai_settings, screen, pacman, balls, walls):
	"""Update the internals of the objects and projectiles."""
	# Update internals of pacman.
	pacman.update()
	# Update internals of balls.
	balls.update()
	# Update internals of walls.
	walls.update()





   

def create_walls(ai_settings, screen, walls):
	"""Spawns a new set of walls, based on screen size and wall size."""
	center_wall = get_center_wall(ai_settings, screen)
	no_of_columns = int("{:.0f}".format((ai_settings.screen_width / 2) / (center_wall.rect.width * 2)))
	no_of_rows = int("{:.0f}".format((ai_settings.screen_height / 2) / (center_wall.rect.height * 2)))
	for column_number in range(-no_of_columns, no_of_columns+1):
		for row_number in range(-no_of_rows, no_of_rows+1):
			if column_number == 0 or row_number == 0:
				pass
			else:
				create_wall(ai_settings, screen, walls, center_wall, column_number, row_number)

def create_wall(ai_settings, screen, walls, center_wall, column_number, row_number):
	"""Specify the correct coordinates for the individual walls to 
	spawn and Adds the new wall into the list(walls)."""
	new_wall = Wall(ai_settings, screen)
	new_wall.centerx = wall_get_x(ai_settings, new_wall.rect, column_number, center_wall)
	new_wall.centery = wall_get_y(ai_settings, new_wall.rect, row_number, center_wall)
	walls.add(new_wall)

def get_center_wall(ai_settings, screen):
	"""Returns a wall with it's centerx and centery equal to that of the screen's."""
	screen_rect = screen.get_rect()
	center_wall = Wall(ai_settings, screen)
	center_wall.centerx = screen_rect.centerx
	center_wall.centery = screen_rect.centery
	return center_wall
	
def wall_get_x(ai_settings, wall_rect, column_number, center_wall):
	"""Gets the position of x for the wall."""
	if column_number > 0:
		rect_centerx = ((center_wall.centerx + wall_rect.width * (-1)) + (center_wall.rect.width * column_number * 2))
	elif column_number < 0:
		rect_centerx = ((center_wall.centerx + wall_rect.width * (+1)) + (center_wall.rect.width * column_number * 2))
	elif column_number == 0:
		rect_centerx = ((center_wall.centerx) + (center_wall.rect.width * column_number * 2))
	#print("column_number", column_number)
	#print("rect_centerx", rect_centerx)
	return rect_centerx
	
def wall_get_y(ai_settings, wall_rect, row_number, center_wall):
	"""Gets the position of y for the wall."""
	if row_number > 0:
		rect_centery = ((center_wall.centery + wall_rect.height * (-1)) + (center_wall.rect.height * row_number * 2))
	elif row_number < 0:
		rect_centery = ((center_wall.centery + wall_rect.height * (+1)) + (center_wall.rect.height * row_number * 2))
	elif row_number == 0:
		rect_centery = ((center_wall.centery) + (center_wall.rect.height * row_number * 2))
	#print("row_number", row_number)
	#print("rect_centery", rect_centery)
	return rect_centery
	





def update_screen(ai_settings, screen, pacman, balls, walls):
	"""Updates the screen with new data from update_internals 
	and check_events in one iteration of them."""
	
	# Fill the screen with the color specified in ai_settings.
	#screen.fill(ai_settings.bg_color)
	screen.fill(ai_settings.bg_color)
	
	# Draws all the projectiles and objects.
	pacman.blitme()
	balls.draw(screen)
	walls.draw(screen)
	
	# Updates the contents of the entire display.
	pygame.display.flip()


























