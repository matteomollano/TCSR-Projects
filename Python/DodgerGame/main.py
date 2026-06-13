import pygame
import random

# --- Setup ---
pygame.init()

WIDTH, HEIGHT = 480, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodger!")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# --- Colors ---
WHITE  = (255, 255, 255)
BLACK  = (0,   0,   0)
BLUE   = (50,  120, 220)
RED    = (220, 50,  50)
YELLOW = (255, 220, 0)
GRAY   = (180, 180, 180)

# --- Player ---
player_width  = 50
player_height = 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 60
player_speed = 6

# --- Falling objects ---
fallers = []
faller_width  = 30
faller_height = 30
faller_speed  = 4   # increases over time

# --- Game state ---
score = 0
lives = 3
game_over = False

# How often a new faller appears (in frames)
SPAWN_RATE = 40
frame_count = 0


def spawn_faller():
    """Create a new falling object at a random x position."""
    x = random.randint(0, WIDTH - faller_width)
    fallers.append([x, -faller_height])


def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, player_width, player_height), border_radius=6)


def draw_fallers():
    for f in fallers:
        pygame.draw.rect(screen, RED, (f[0], f[1], faller_width, faller_height), border_radius=4)


def check_collision(px, py):
    """Return True if any faller overlaps the player."""
    player_rect = pygame.Rect(px, py, player_width, player_height)
    for f in fallers:
        if player_rect.colliderect(pygame.Rect(f[0], f[1], faller_width, faller_height)):
            return True
    return False


def draw_hud():
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, YELLOW)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (WIDTH - 120, 10))


def draw_game_over():
    screen.fill(BLACK)
    msg1 = font.render("GAME OVER", True, RED)
    msg2 = font.render(f"Final Score: {score}", True, WHITE)
    msg3 = font.render("Press R to restart", True, GRAY)
    screen.blit(msg1, (WIDTH // 2 - msg1.get_width() // 2, 200))
    screen.blit(msg2, (WIDTH // 2 - msg2.get_width() // 2, 260))
    screen.blit(msg3, (WIDTH // 2 - msg3.get_width() // 2, 320))


# --- Main loop ---
running = True
while running:

    clock.tick(60)  # 60 frames per second

    # --- Events ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # Reset everything
                fallers.clear()
                score = 0
                lives = 3
                faller_speed = 4
                player_x = WIDTH // 2 - player_width // 2
                frame_count = 0
                game_over = False

    if game_over:
        draw_game_over()
        pygame.display.flip()
        continue

    # --- Move player ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # --- Spawn fallers ---
    frame_count += 1
    if frame_count % SPAWN_RATE == 0:
        spawn_faller()

    # --- Move fallers ---
    for f in fallers:
        f[1] += faller_speed

    # --- Remove fallers that fell off screen and increase score ---
    survived = []
    for f in fallers:
        if f[1] > HEIGHT:
            score += 1
            # Every 5 points, speed up a little
            if score % 5 == 0:
                faller_speed += 0.5
        else:
            survived.append(f)
    fallers[:] = survived

    # --- Collision ---
    if check_collision(player_x, player_y):
        lives -= 1
        fallers.clear()   # clear screen after getting hit
        if lives <= 0:
            game_over = True

    # --- Draw ---
    screen.fill(BLACK)
    draw_player(player_x, player_y)
    draw_fallers()
    draw_hud()

    pygame.display.flip()

pygame.quit()