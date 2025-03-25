import pygame, sys
from model.settings import *
from model.level import Level 
from model.player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Code_Rangers')
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update() 
            dt = self.clock.tick() / 1000  # fix this
            self.level.run(dt)

if __name__ == '__main__':
    game = Game()
    game.run()