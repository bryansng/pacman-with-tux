import sys
import pygame

from wall import Wall
from pacman import Pacman

def check_keydown_events(event, ai_settings, screen, pacman, time_new):
	if event.key == pygame.K_q:
		pygame.quit()
		sys.exit()
	if event.key == pygame.K_m:
		pacman.randomize_and_move_to_point(ai_settings, screen, time_new)
	if event.key == pygame.K_w and (not pacman.movement_down and not pacman.movement_left and not pacman.movement_right):
		pacman.movement_up = True
		pacman.face_direction(event, ai_settings, time_new)
		ai_settings.pacman_time_move = time_new
	elif event.key == pygame.K_s and (not pacman.movement_up and not pacman.movement_left and not pacman.movement_right):
		pacman.movement_down = True
		pacman.face_direction(event, ai_settings, time_new)
		ai_settings.pacman_time_move = time_new
	elif event.key == pygame.K_a and (not pacman.movement_up and not pacman.movement_down and not pacman.movement_right):
		pacman.movement_left = True
		pacman.face_direction(event, ai_settings, time_new)
		ai_settings.pacman_time_move = time_new
	elif event.key == pygame.K_d and (not pacman.movement_up and not pacman.movement_down and not pacman.movement_left):
		pacman.movement_right = True
		pacman.face_direction(event, ai_settings, time_new)
		ai_settings.pacman_time_move = time_new
	
def check_keyup_events(event, ai_settings, pacman):
	if event.key == pygame.K_w:
		pacman.movement_up = False
	elif event.key == pygame.K_s:
		pacman.movement_down = False
	elif event.key == pygame.K_a:
		pacman.movement_left = False
	elif event.key == pygame.K_d:
		pacman.movement_right = False
	
def check_events(ai_settings, screen, pacman, time_new):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, pacman, time_new)
		if event.type == pygame.KEYUP:
			check_keyup_events(event, ai_settings, pacman)
		
		

def update_internals(ai_settings, screen, pacman, balls, walls):
	pacman.update()
	balls.update()
	walls.update()





   

def create_walls(ai_settings, screen, walls):
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
	new_wall = Wall(ai_settings, screen)
	new_wall.centerx = wall_get_x(ai_settings, new_wall.rect, column_number, center_wall)
	new_wall.centery = wall_get_y(ai_settings, new_wall.rect, row_number, center_wall)
	walls.add(new_wall)

def get_center_wall(ai_settings, screen):
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
	screen.fill(ai_settings.bg_color)
	
	pacman.blitme()
	balls.draw(screen)
	walls.draw(screen)
	
	pygame.display.flip()


























