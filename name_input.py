import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, YELLOW, BLACK

class NameInput:
    def __init__(self, screen, score):
        self.screen = screen
        self.score = score
        self.name = ""
        self.max_length = 12
        self.done = False
        self.font_large = pygame.font.Font(None, 74)
        self.font_medium = pygame.font.Font(None, 48)
        self.font_small = pygame.font.Font(None, 36)
    
    def handle_event(self, event):
        """Verwerk keyboard input"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and len(self.name) > 0:
                self.done = True
            elif event.key == pygame.K_BACKSPACE:
                self.name = self.name[:-1]
            elif event.unicode.isalnum() or event.unicode == " ":
                if len(self.name) < self.max_length:
                    self.name += event.unicode.upper()
    
    def draw(self):
        """Teken het naam input scherm"""
        self.screen.fill(BLACK)
        
        # Titel
        title_text = self.font_large.render("GAME OVER!", True, YELLOW)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 100))
        self.screen.blit(title_text, title_rect)
        
        # Score
        score_text = self.font_medium.render(f"Score: {self.score}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 200))
        self.screen.blit(score_text, score_rect)
        
        # Instructie
        instruction_text = self.font_small.render("Voer je naam in:", True, WHITE)
        instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH // 2, 280))
        self.screen.blit(instruction_text, instruction_rect)
        
        # Naam input veld
        name_display = self.name if self.name else "_"
        name_text = self.font_medium.render(name_display, True, YELLOW)
        name_rect = name_text.get_rect(center=(SCREEN_WIDTH // 2, 350))
        self.screen.blit(name_text, name_rect)
        
        # Enter instructie
        enter_text = self.font_small.render("Druk op ENTER om op te slaan", True, WHITE)
        enter_rect = enter_text.get_rect(center=(SCREEN_WIDTH // 2, 430))
        self.screen.blit(enter_text, enter_rect)
