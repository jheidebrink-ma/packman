import pygame
from level import Level
from player import Player
from settings import BLACK, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.level = Level()
        self.player = Player(1, 1, self.level.walls)
        self.score = 0
        self.game_over = False
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)

    def update(self):
        if self.game_over:
            return
            
        self.player.update()

        player_tile = (int(self.player.grid_pos.x), int(self.player.grid_pos.y))
        if player_tile in self.level.dots:
            self.level.dots.remove(player_tile)
            self.score += 10
        
        # Check if all dots are collected
        if len(self.level.dots) == 0:
            self.game_over = True

    def draw(self):
        self.screen.fill(BLACK)
        self.level.draw(self.screen)
        self.player.draw(self.screen)
        
        # Draw score
        score_text = self.small_font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw game over message
        if self.game_over:
            game_over_text = self.font.render("GAME OVER!", True, WHITE)
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 30))
            self.screen.blit(game_over_text, text_rect)
            
            final_score_text = self.small_font.render(f"Final Score: {self.score}", True, WHITE)
            score_rect = final_score_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 10))
            self.screen.blit(final_score_text, score_rect)