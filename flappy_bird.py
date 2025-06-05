import pygame
import random
import sys

pygame.init()

# Game constants
WIDTH = 400
HEIGHT = 600
GRAVITY = 0.5
JUMP_STRENGTH = -8
PIPE_SPEED = 2
PIPE_GAP = 150
PIPE_WIDTH = 50

# Colors
BLUE = (0, 70, 255)
GREEN = (34, 139, 34)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Initialize game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

class Bird:
    def __init__(self):
        self.radius = 10
        self.x = WIDTH // 4
        self.y = HEIGHT // 2
        self.velocity = 0
        
    def jump(self):
        self.velocity = JUMP_STRENGTH
        
    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        
        # Floor and ceiling collision
        if self.y >= HEIGHT - self.radius:
            self.y = HEIGHT - self.radius
            return True
        elif self.y <= self.radius:
            self.y = self.radius
            return True
            
        return False

class Pipe:
    def __init__(self, x):
        self.x = x
        self.top_height = random.randint(50, HEIGHT // 2)
        self.bottom_y = self.top_height + PIPE_GAP
        
    def update(self):
        self.x -= PIPE_SPEED
        return True
        
    def get_rects(self):
        top_rect = pygame.Rect(self.x, 0, PIPE_WIDTH, self.top_height)
        bottom_rect = pygame.Rect(self.x, self.bottom_y, PIPE_WIDTH, HEIGHT - self.bottom_y)
        return [top_rect, bottom_rect]

def draw_bird(bird):
    pygame.draw.circle(screen, YELLOW, (int(bird.x), int(bird.y)), bird.radius)

def main():
    bird = Bird()
    pipes = []
    score = 0
    font = pygame.font.Font(None, 36)
    
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame.KEYDOWN and 
                (event.key == pygame.K_SPACE or event.key == pygame.K_UP)) or \
               (event.type == pygame.MOUSEBUTTONDOWN):
                bird.jump()
        
        # Update game state
        bird_dead = bird.update()
        
        # Add new pipes
        if len(pipes) == 0 or pipes[-1].x < WIDTH - PIPE_WIDTH:
            pipes.append(Pipe(WIDTH))
            
        # Remove off-screen pipes and check collisions/score
        for pipe in pipes.copy():
            pipe.update()
            rects = pipe.get_rects()
            for rect in rects:
                if pygame.Rect(bird.x - bird.radius, bird.y - bird.radius,
                              2*bird.radius, 2*bird.radius).colliderect(rect):
                    bird_dead = True
            if pipe.x + PIPE_WIDTH < 0:
                pipes.remove(pipe)
            elif pipe.x < bird.x and not any(p.x == pipe.x for p in passed_pipes):
                score += 1
        
        # Clear screen
        screen.fill(BLUE)
        
        # Draw pipes
        for pipe in pipes:
            top_rect = pygame.Rect(pipe.x, 0, PIPE_WIDTH, pipe.top_height)
            bottom_rect = pygame.Rect(pipe.x, pipe.bottom_y, PIPE_WIDTH, HEIGHT - pipe.bottom_y)
            pygame.draw.rect(screen, GREEN, top_rect)
            pygame.draw.rect(screen, GREEN, bottom_rect)
        
        # Draw bird
        draw_bird(bird)
        
        # Draw score
        text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(text, (10, 10))
        
        # Check if game over
        if bird_dead:
            pygame.time.wait(2000)  # Wait before restarting
            main()  # Reset game
            
        # Update display
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
