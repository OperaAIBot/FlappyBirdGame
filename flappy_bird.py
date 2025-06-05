import pygame
import random
import math

pygame.init()

# Game window dimensions
WIDTH = 400
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game properties
BIRD_RADIUS = 20
GRAVITY = 0.5
JUMP_STRENGTH = -10
PIPE_WIDTH = 80
PIPE_GAP = 170
PIPE_SPACING = 300

class Bird:
    def __init__(self):
        self.x = WIDTH // 4
        self.y = HEIGHT // 2
        self.velocity = 0
        self.gravity = GRAVITY
    
    def jump(self):
        self.velocity += JUMP_STRENGTH
    
    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
        
        # Floor and ceiling collision
        if self.y - BIRD_RADIUS < 0:
            self.y = BIRD_RADIUS
            self.velocity = 0
        elif self.y + BIRD_RADIUS > HEIGHT:
            self.y = HEIGHT - BIRD_RADIUS
            self.velocity = 0

class Pipe:
    def __init__(self, x):
        self.x = x
        self.top_gap = random.randint(150, 450)
        self.bottom_gap = self.top_gap + PIPE_GAP
    
    def move(self, dx):
        self.x += dx
    
    def get_rects(self):
        return [
            pygame.Rect(self.x, 0, PIPE_WIDTH, self.top_gap),
            pygame.Rect(self.x, self.bottom_gap, PIPE_WIDTH, HEIGHT - self.bottom_gap)
        ]

def draw_bird(bird):
    pygame.draw.circle(window, BLACK, (int(bird.x), int(bird.y)), BIRD_RADIUS)

def draw_pipes(pipes):
    for pipe in pipes:
        for rect in pipe.get_rects():
            pygame.draw.rect(window, BLACK, rect)

def check_collision(bird, pipes):
    bird_x = bird.x
    bird_y = bird.y
    bird_radius = BIRD_RADIUS
    
    # Check if bird hits any pipe
    for pipe in pipes:
        top_pipe = pipe.get_rects()[0]
        bottom_pipe = pipe.get_rects()[1]
        
        # Check collision with top pipe
        if (bird_x - bird_radius <= top_pipe.right and
            bird_x + bird_radius >= top_pipe.left and 
            bird_y - bird_radius <= top_pipe.bottom):
            return True
        
        # Check collision with bottom pipe
        if (bird_x - bird_radius <= bottom_pipe.right and
            bird_x + bird_radius >= bottom_pipe.left and 
            bird_y + bird_radius >= bottom_pipe.top):
            return True
    
    # Check boundaries
    if bird.y <= bird_radius or bird.y >= HEIGHT - bird_radius:
        return True
        
    return False

def main():
    bird = Bird()
    pipes = [Pipe(WIDTH + i * PIPE_SPACING) for i in range(3)]
    
    clock = pygame.time.Clock()
    score = 0
    font = pygame.font.Font(None, 36)
    
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.jump()
        
        # Update game state
        bird.update()
        score += 1
        
        # Move pipes and check if new pipe is needed
        for pipe in pipes:
            pipe.move(-2)
            if pipe.x + PIPE_WIDTH < 0:
                pipes.remove(pipe)
                new_pipe = Pipe(WIDTH)
                pipes.append(new_pipe)
         
        # Draw everything
        window.fill(WHITE)
        
        draw_pipes(pipes)
        draw_bird(bird)
        
        # Update score display
        text_surface = font.render(f"Score: {score // 100}", True, BLACK)
        window.blit(text_surface, (10, 10))
        
        pygame.display.flip()
        
        # Check for collisions
        if check_collision(bird, pipes):
            print("Game Over! Score:", score // 100)
            running = False
        
        clock.tick(60)

if __name__ == "__main__":
    main()
