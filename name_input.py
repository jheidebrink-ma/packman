import pygame
from settings import WHITE, BLACK, SCREEN_WIDTH, SCREEN_HEIGHT

class NameInputScreen:
    def __init__(self, screen, score):
        self.screen = screen
        self.score = score
        self.name = ""
        self.max_length = 15
        self.active = True
        self.font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 28)
        self.instruction_font = pygame.font.Font(None, 24)
    
    def handle_event(self, event):
        """Handle keyboard input for name entry"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and len(self.name) > 0:
                self.active = False
                return True
            elif event.key == pygame.K_BACKSPACE:
                self.name = self.name[:-1]
            elif event.key == pygame.K_ESCAPE:
                self.name = "Anonymous"
                self.active = False
                return True
            elif len(self.name) < self.max_length:
                # Only accept alphanumeric and space
                if event.unicode.isprintable():
                    self.name += event.unicode
        return False
    
    def draw(self):
        """Draw the name input screen"""
        self.screen.fill(BLACK)
        
        # Title
        title_text = self.font.render("NEW HIGHSCORE!", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 100))
        self.screen.blit(title_text, title_rect)
        
        # Score
        score_text = self.small_font.render(f"Score: {self.score}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50))
        self.screen.blit(score_text, score_rect)
        
        # Instruction
        instruction_text = self.instruction_font.render("Enter your name:", True, WHITE)
        instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        self.screen.blit(instruction_text, instruction_rect)
        
        # Input box
        input_box = pygame.Rect(SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2 + 30, 300, 50)
        pygame.draw.rect(self.screen, WHITE, input_box, 2)
        
        # Name text
        name_text = self.small_font.render(self.name + "|", True, WHITE)
        name_rect = name_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 55))
        self.screen.blit(name_text, name_rect)
        
        # Bottom instructions
        enter_text = self.instruction_font.render("Press ENTER to save", True, WHITE)
        enter_rect = enter_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 120))
        self.screen.blit(enter_text, enter_rect)
        
        esc_text = self.instruction_font.render("Press ESC to skip", True, WHITE)
        esc_rect = esc_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 145))
        self.screen.blit(esc_text, esc_rect)
    
    def get_name(self):
        """Return the entered name"""
        return self.name if self.name else "Anonymous"
