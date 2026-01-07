import pygame
from level import Level
from player import Player
from settings import BLACK, WHITE
from highscore import HighscoreManager
from name_input import NameInput
from highscore_screen import HighscoreScreen

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.level = Level()
        self.player = Player(1, 1, self.level.walls)
        self.score = 0
        self.highscore_manager = HighscoreManager()
        self.font = pygame.font.Font(None, 36)
        
        # Game states: "playing", "name_input", "highscore_screen"
        self.state = "playing"
        self.name_input = None
        self.highscore_screen = None

    def update(self):
        if self.state == "playing":
            self.player.update()

            player_tile = (int(self.player.grid_pos.x), int(self.player.grid_pos.y))
            if player_tile in self.level.dots:
                self.level.dots.remove(player_tile)
                self.score += 10
            
            # Check of alle dots zijn verzameld
            if len(self.level.dots) == 0:
                self.state = "name_input"
                self.name_input = NameInput(self.screen, self.score)
        
        elif self.state == "name_input":
            if self.name_input.done:
                # Sla de score op
                self.highscore_manager.add_score(self.name_input.name, self.score)
                self.state = "highscore_screen"
                self.highscore_screen = HighscoreScreen(self.screen, self.highscore_manager)
        
        elif self.state == "highscore_screen":
            if self.highscore_screen.done:
                # Reset het spel
                self.reset_game()

    def draw(self):
        if self.state == "playing":
            self.screen.fill(BLACK)
            self.level.draw(self.screen)
            self.player.draw(self.screen)
            
            # Teken de score
            score_text = self.font.render(f"Score: {self.score}", True, WHITE)
            self.screen.blit(score_text, (10, 10))
        
        elif self.state == "name_input":
            self.name_input.draw()
        
        elif self.state == "highscore_screen":
            self.highscore_screen.draw()
    
    def handle_event(self, event):
        """Verwerk events afhankelijk van de game state"""
        if self.state == "name_input":
            self.name_input.handle_event(event)
        elif self.state == "highscore_screen":
            self.highscore_screen.handle_event(event)
    
    def reset_game(self):
        """Reset het spel voor een nieuwe ronde"""
        self.level = Level()
        self.player = Player(1, 1, self.level.walls)
        self.score = 0
        self.state = "playing"
        self.name_input = None
        self.highscore_screen = None