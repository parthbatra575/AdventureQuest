import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen size
WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Adventure Quest")

# Colors
SKY = (135, 206, 235)
WHITE = (255, 255, 255)

# Game clock
clock = pygame.time.Clock()

running = True

while running:

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background
    screen.fill(SKY)

    # Title
    font = pygame.font.SysFont("Arial", 50)
    text = font.render("Adventure Quest", True, WHITE)
    screen.blit(text, (300, 20))

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()
