import pygame,sys 
from model.settings import * 
from model.player import Player
from model.organisms import *
from pytmx.util_pygame import load_pygame
from model.support import import_folder

class Level:
    def __init__(self):
        #display on the screen
        self.display_surface = pygame.display.get_surface()

        #The organisms
        self.all_organisms = CameraGroup()
        self.collision_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        tmx_data = load_pygame('assets/Easy_map.tmx')
		
        # house 
        for layer in ['house_floor', 'house_walls']:
            for x, y, surf in tmx_data.get_layer_by_name(layer).tiles():
                Generic((x * TILE_SIZE,y * TILE_SIZE), surf, self.all_organisms, LAYERS['house_floor'])

        #fences
        for x, y, surf in tmx_data.get_layer_by_name('fence').tiles():
              Generic((x* TILE_SIZE, y*TILE_SIZE), surf, self.all_organisms)
        
        # water 
        water_frames = import_folder('graphics/water')
        for x, y, surf in tmx_data.get_layer_by_name('water').tiles():
            Water((x * TILE_SIZE,y * TILE_SIZE), water_frames, self.all_organisms)

        # trees 
        for obj in tmx_data.get_layer_by_name('trees'):
            Tree((obj.x, obj.y), obj.image, [self.all_organisms, self.collision_sprites], obj.name)

        # wildflowers 
        for obj in tmx_data.get_layer_by_name('flowers'):
            WildFlower((obj.x, obj.y), obj.image, [self.all_organisms, self.collision_sprites])

        # tiles 
        for x, y, surf in tmx_data.get_layer_by_name('tiles').tiles():
              Generic((x* TILE_SIZE, y*TILE_SIZE), surf, self.all_organisms)

        # mushrooms 
        for obj in tmx_data.get_layer_by_name('mushrooms'):
            WildFlower((obj.x, obj.y), obj.image, [self.all_organisms, self.collision_sprites])

        # collion tiles
        for x, y, surf in tmx_data.get_layer_by_name('hit').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), pygame.Surface((TILE_SIZE, TILE_SIZE)), self.collision_sprites)

        # Player 
        for obj in tmx_data.get_layer_by_name('player_spawn'):
            if obj.name == 'Player':
                self.player = Player((obj.x,obj.y), self.all_organisms, self.collision_sprites)
        Generic(
			pos = (0,0),
			surf = pygame.image.load('assets/Easy_map.png').convert_alpha(),
			groups = self.all_organisms,
			z = LAYERS['grass'])
		
		
    def run(self,dt):
        self.display_surface.fill('black')
        self.all_organisms.custom_draw(self.player)
        self.all_organisms.update(dt)

class CameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.offset = pygame.math.Vector2()

	def custom_draw(self, player):
		self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
		self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

		for layer in LAYERS.values():
			for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
				if sprite.z == layer:
					offset_rect = sprite.rect.copy()
					offset_rect.center -= self.offset
					self.display_surface.blit(sprite.image, offset_rect)