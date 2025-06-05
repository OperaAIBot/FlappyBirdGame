import pygame
from random import randint

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRAVITY = 0.5
JUMP_STRENGTH = -12
PIPE_SPEED = 3
PIPE_GAP = 200
PIPE_DISTANCE = 400

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# Game variables
bird_x = 100
bird_y = 300
bird_velocity = 0

pipes = []
score = 0
game_over = False

def create_pipe():
    pipe_height = randint(100, SCREEN_HEIGHT - PIPE_GAP - 100)
    pipes.append({'x': SCREEN_WIDTH + PIPE_DISTANCE, 'height': pipe_height})

def draw_bird():
    pygame.draw.circle(screen, BLUE, (int(bird_x), int(bird_y)), 20)

def draw_pipes():
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, (pipe['x'], 0, 100, pipe['height']))
        pygame.draw.rect(screen, GREEN, (pipe['x'], pipe['height'] + PIPE_GAP, 100, SCREEN_HEIGHT - (pipe['height'] + PIPE_GAP)))

def draw_background():
    screen.fill((50, 205, 50))
    # Draw ground
    pygame.draw.rect(screen, (43, 189, 79), (0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 100))

def reset_game():
    global bird_x, bird_y, bird_velocity, pipes, score, game_over
    bird_x = 100
    bird_y = 300
    bird_velocity = 0
    pipes = []
    score = 0
    game_over = False

running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_SPACE:
                    bird_velocity = JUMP_STRENGTH
            else:
                reset_game()

    # Game logic
    if not game_over:
        # Update bird position
        bird_velocity += GRAVITY
        bird_y += bird_velocity

        # Check collisions
        if bird_y <= 0 or bird_y >= SCREEN_HEIGHT - 20:
            game_over = True

        # Generate pipes
        if len(pipes) == 0 or pipes[-1]['x'] < SCREEN_WIDTH - PIPE_DISTANCE:
            create_pipe()

        # Update pipes
        for pipe in pipes:
            pipe['x'] -= PIPE_SPEED

            # Check collision with bird
            if not game_over and (bird_x + 20 > pipe['x'] and bird_x - 20 < pipe['x'] + 100):
                if bird_y < pipe['height'] or bird_y > pipe['height'] + PIPE_GAP:
                    game_over = True

        # Update score
        for i, pipe in enumerate(pipes[:]):
            if pipe['x'] < bird_x and not pipe.get('scored'):
                pipes[i]['scored'] = True
                score += 1

        # Remove off-screen pipes
        while len(pipes) > 0 and pipes[0]['x'] < -100:
            pipes.pop(0)

    # Draw everything
    draw_background()
    
    if not game_over:
        draw_pipes()
        draw_bird()
        # Draw score
        font = pygame.font.Font(None, 74)
        text = font.render(str(score), True, WHITE)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width()//2, 50))
    else:
        # Game over screen
        font = pygame.font.Font(None, 100)
        text_game_over = font.render("Game Over", True, WHITE)
        text_score = font.render(f"Score: {score}", True, WHITE)
        restart_font = pygame.font.Font(None, 36)
        text_restart = restart_font.render("Press Space to Restart", True, WHITE)
        
        screen.blit(text_game_over, (SCREEN_WIDTH//2 - text_game_over.get_width()//2, 100))
        screen.blit(text_score, (SCREEN_WIDTH//2 - text_score.get_width()//2, 200))
        screen.blit(text_restart, (SCREEN_WIDTH//2 - text_restart.get_width()//2, 350))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
