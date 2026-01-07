import pygame
from game import Game
from highscore import HighscoreManager
from name_input import NameInputScreen
from highscore_screen import HighscoreScreen
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

# Game states
STATE_PLAYING = "playing"
STATE_NAME_INPUT = "name_input"
STATE_HIGHSCORE = "highscore"

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man Grid Based")
clock = pygame.time.Clock()

# Initialize managers
highscore_manager = HighscoreManager()
game = Game(screen)
current_state = STATE_PLAYING
name_input_screen = None
highscore_screen = None

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle events based on current state
        if current_state == STATE_NAME_INPUT and name_input_screen:
            if name_input_screen.handle_event(event):
                # Name input completed
                player_name = name_input_screen.get_name()
                highscore_manager.add_score(player_name, game.score)
                highscore_screen = HighscoreScreen(screen, highscore_manager)
                current_state = STATE_HIGHSCORE
        
        elif current_state == STATE_HIGHSCORE:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Restart game
                    game = Game(screen)
                    current_state = STATE_PLAYING
                elif event.key == pygame.K_ESCAPE:
                    running = False
    
    # Update and draw based on current state
    if current_state == STATE_PLAYING:
        game.update()
        game.draw()
        
        # Check if game is over
        if game.game_over:
            if highscore_manager.is_highscore(game.score):
                # Show name input
                name_input_screen = NameInputScreen(screen, game.score)
                current_state = STATE_NAME_INPUT
            else:
                # Show highscore directly
                highscore_screen = HighscoreScreen(screen, highscore_manager)
                current_state = STATE_HIGHSCORE
    
    elif current_state == STATE_NAME_INPUT:
        name_input_screen.draw()
    
    elif current_state == STATE_HIGHSCORE:
        highscore_screen.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()