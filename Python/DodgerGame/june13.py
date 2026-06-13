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

# Set a flag to keep the loop running
running = True

# Game Loop
while running:
    
    clock.tick(1080) # 1080 FPS
    
    # Look at all events from the user (mouse, keyboard, window clicks)
    for event in pygame.event.get():
        # Check if the user clicked the window's close ("X") button
        if event.type == pygame.QUIT:
            running = False

    # Fill the background black and draw the player
    screen.fill(BLACK)
    draw_player(player_x, player_y)
    
    # --- Move player ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    
    # Refresh the display to show changes
    pygame.display.flip()

# 4. Clean up and close everything safely
pygame.quit()