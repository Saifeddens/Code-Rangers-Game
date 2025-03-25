import pygame
from pygame.math import Vector2
# screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TILE_SIZE = 64

LAYERS = {
	'water': 1,
	'grass': 2,
	'hill': 3,
	'tiles': 4,
	'house_floor': 5,
	'house_walls': 6,
	'fence': 7,
	'trees': 8,
	'mushrooms': 9,
	'flowers': 10,
    'main':0,
	'player_spawn': 11,
    'hit':12
}