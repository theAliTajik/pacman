import pygame
import sys

# Initialize Pygame
pygame.init()

# Game constants
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 480
PACMAN_SIZE = 20
PACMAN_SPEED = 5
BACKGROUND_COLOR = (0, 0, 0)
PELLET_COLOR = (255, 255, 255)
PELLET_SIZE = 5

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")

# Load Pac-Man image
pacman_img = pygame.image.load("Pac_.png")
pacman_img = pygame.transform.scale(pacman_img, (PACMAN_SIZE, PACMAN_SIZE))

# Pac-Man starting position
pacman_x, pacman_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

# Movement variables
move_x, move_y = 0, 0

# Pellets
pellets = []
for i in range(0, SCREEN_WIDTH, PACMAN_SIZE):
    for j in range(0, SCREEN_HEIGHT, PACMAN_SIZE):
        pellets.append((i, j))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_x = -PACMAN_SPEED
                move_y = 0
            if event.key == pygame.K_RIGHT:
                move_x = PACMAN_SPEED
                move_y = 0
            if event.key == pygame.K_UP:
                move_x = 0
                move_y = -PACMAN_SPEED
            if event.key == pygame.K_DOWN:
                move_x = 0
                move_y = PACMAN_SPEED

    # Update Pac-Man's position
    pacman_x += move_x
    pacman_y += move_y

    # Prevent Pac-Man from moving outside the screen
    pacman_x = max(0, min(pacman_x, SCREEN_WIDTH - PACMAN_SIZE))
    pacman_y = max(0, min(pacman_y, SCREEN_HEIGHT - PACMAN_SIZE))

    # Collision detection for pellets
    pacman_rect = pygame.Rect(pacman_x, pacman_y, PACMAN_SIZE, PACMAN_SIZE)
    pellets = [pellet for pellet in pellets if not pacman_rect.collidepoint(pellet[0] + PELLET_SIZE // 2, pellet[1] + PELLET_SIZE // 2)]

    # Drawing
    screen.fill(BACKGROUND_COLOR)
    screen.blit(pacman_img, (pacman_x, pacman_y))

    for pellet in pellets:
        pygame.draw.rect(screen, PELLET_COLOR, (pellet[0], pellet[1], PELLET_SIZE, PELLET_SIZE))

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
