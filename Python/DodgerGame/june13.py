import pygame
import random

pygame.init()

WIDTH, HEIGHT = 480, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodger")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Colors
WHITE  = (255, 255, 255)
BLACK  = (0,   0,   0)
BLUE   = (50,  120, 220)
RED    = (220, 50,  50)
YELLOW = (255, 220, 0)
GRAY   = (180, 180, 180)

# Player
player_width = 50
player_height = 20
player_x = (WIDTH - player_width) // 2
player_y = HEIGHT - 60
player_speed = 6

def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, player_width, player_height), border_radius=6)
    
# Falling objects
fallers = []
faller_height = 30
faller_width = 30
faller_speed = 4

# How often a new faller appears (in frames)
SPAWN_RATE = 40
frame_count = 0

def spawn_faller():
    x = random.randint(0, WIDTH - faller_width)
    fallers.append([x, 40])

def draw_fallers():
    # [
    #     [x, y], # each individual obstacle
    #     [x, y],
    #     ...
    # ]
    for f in fallers:
        pygame.draw.rect(screen, YELLOW, (f[0], f[1], faller_width, faller_height), border_radius=4)
        
def check_collision(player_x, player_y):
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    for f in fallers:
        faller_rect = pygame.Rect(f[0], f[1], faller_width, faller_height)
        if player_rect.colliderect(faller_rect):
            return True
    return False

# Set a flag to keep the loop running
running = True

# Game Loop
while running:
    
    clock.tick(120) # 1080 FPS
    
    # Look at all events from the user (mouse, keyboard, window clicks)
    for event in pygame.event.get():
        # Check if the user clicked the window's close ("X") button
        if event.type == pygame.QUIT:
            running = False

    # Fill the background black and draw the player
    screen.fill(BLACK)
    draw_player(player_x, player_y)
    draw_fallers()
    
    # --- Move player ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
        
    # --- Spawn fallers every 40 frames ---
    frame_count += 1
    if frame_count % SPAWN_RATE == 0:
        spawn_faller()
    
    # --- Move fallers ---
    for f in fallers:
        # f[1] is y value
        f[1] += faller_speed
    
    if check_collision(player_x, player_y):
        pass # finish next time
    
    # Refresh the display to show changes
    pygame.display.flip()

# 4. Clean up and close everything safely
pygame.quit()