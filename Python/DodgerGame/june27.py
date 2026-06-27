import pygame
import random

pygame.init()

WIDTH, HEIGHT = 480, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodger")

clock = pygame.time.Clock()

BLACK  = (0, 0, 0)
YELLOW = (255, 220, 0)
BLUE   = (50, 120, 220)

player_width = 50
player_height = 20
player_x = (WIDTH - player_width) // 2
player_y = HEIGHT - 50
player_speed = 6

faller_width = 30
faller_height = 30
faller_speed = 6

def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, player_width, player_height))

fallers = []
''' Example:
[
    [17, -50],
    [100, -50],
    [400, -50],
    ...
]
'''

def spawn_faller():
    faller_x = random.randint(0, WIDTH - faller_width)
    faller_y = -faller_height
    fallers.append([faller_x, faller_y])
    
def draw_fallers():
    for faller in fallers:
        faller_x = faller[0]
        faller_y = faller[1]
        pygame.draw.rect(screen, YELLOW, (faller_x, faller_y, faller_width, faller_height))

frame_count = 0
SPAWN_RATE = 40     

running = True
while running:
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK)
    draw_player(player_x, player_y)
    draw_fallers()
    
    frame_count += 1
    if frame_count % SPAWN_RATE == 0:
        spawn_faller()
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
        
    for faller in fallers:
        faller[1] += faller_speed
        
    pygame.display.flip()
    
pygame.quit()