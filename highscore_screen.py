import pygame
from settings import WHITE, BLACK, YELLOW, SCREEN_WIDTH, SCREEN_HEIGHT

class HighscoreScreen:
    def __init__(self, screen, highscore_manager):
        self.screen = screen
        self.highscore_manager = highscore_manager
        self.font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 28)
        self.instruction_font = pygame.font.Font(None, 24)
    
    def draw(self):
        """Draw the highscore leaderboard"""
        self.screen.fill(BLACK)
        
        # Title
        title_text = self.font.render("HIGHSCORES", True, YELLOW)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH//2, 50))
        self.screen.blit(title_text, title_rect)
        
        # Get highscores
        highscores = self.highscore_manager.get_highscores()
        
        if not highscores:
            no_scores_text = self.small_font.render("No highscores yet!", True, WHITE)
            no_scores_rect = no_scores_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            self.screen.blit(no_scores_text, no_scores_rect)
        else:
            # Display highscores
            y_offset = 120
            for i, entry in enumerate(highscores[:10], 1):
                # Rank and name
                rank_text = self.small_font.render(f"{i}.", True, YELLOW)
                self.screen.blit(rank_text, (100, y_offset))
                
                name_text = self.small_font.render(entry['name'], True, WHITE)
                self.screen.blit(name_text, (150, y_offset))
                
                # Score (right aligned)
                score_text = self.small_font.render(str(entry['score']), True, WHITE)
                score_rect = score_text.get_rect(right=SCREEN_WIDTH - 100)
                score_rect.y = y_offset
                self.screen.blit(score_text, score_rect)
                
                y_offset += 35
        
        # Instructions
        instruction_text = self.instruction_font.render("Press SPACE to play again or ESC to quit", True, WHITE)
        instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT - 40))
        self.screen.blit(instruction_text, instruction_rect)
