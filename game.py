import pygame
from level import Level
from player import Player
from settings import BLACK

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.level = Level()
        self.player = Player(1, 1, self.level.walls)
        self.score = 0

    def update(self):
        self.player.update()

        player_tile = (int(self.player.grid_pos.x), int(self.player.grid_pos.y))
        if player_tile in self.level.dots:
            self.level.dots.remove(player_tile)
            self.score += 10

    def draw(self):
        self.screen.fill(BLACK)
        self.level.draw(self.screen)
        self.player.draw(self.screen)