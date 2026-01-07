import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, YELLOW, BLACK

class HighscoreScreen:
    def __init__(self, screen, highscore_manager):
        self.screen = screen
        self.highscore_manager = highscore_manager
        self.done = False
        self.font_large = pygame.font.Font(None, 74)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 28)
    
    def handle_event(self, event):
        """Verwerk keyboard input"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                self.done = True
    
    def draw(self):
        """Teken het highscore scherm"""
        self.screen.fill(BLACK)
        
        # Titel
        title_text = self.font_large.render("HIGH SCORES", True, YELLOW)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 50))
        self.screen.blit(title_text, title_rect)
        
        # Highscores
        highscores = self.highscore_manager.get_highscores()
        start_y = 130
        
        if not highscores:
            no_scores_text = self.font_medium.render("Nog geen scores!", True, WHITE)
            no_scores_rect = no_scores_text.get_rect(center=(SCREEN_WIDTH // 2, 250))
            self.screen.blit(no_scores_text, no_scores_rect)
        else:
            for i, entry in enumerate(highscores):
                # Positie nummer
                rank_text = self.font_medium.render(f"{i+1}.", True, WHITE)
                self.screen.blit(rank_text, (100, start_y + i * 35))
                
                # Naam
                name_text = self.font_medium.render(entry["name"], True, YELLOW)
                self.screen.blit(name_text, (150, start_y + i * 35))
                
                # Score
                score_text = self.font_medium.render(str(entry["score"]), True, WHITE)
                score_rect = score_text.get_rect(right=SCREEN_WIDTH - 100)
                self.screen.blit(score_text, (score_rect.x, start_y + i * 35))
        
        # Instructie
        instruction_text = self.font_small.render("Druk op ENTER of SPATIE om te sluiten", True, WHITE)
        instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 40))
        self.screen.blit(instruction_text, instruction_rect)
